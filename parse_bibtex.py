import pybtex
import pylatexenc.latex2text
import numpy as np
from pybtex.database.input import bibtex
import template
parser = bibtex.Parser()
bib_data = parser.parse_file('tsirkin.bib')
print(list(bib_data.entries.keys()))


fout_name = "bibliography_tables.fodt"

def write_person(person):
    first = pybtex.textutils.abbreviate("".join(person.get_part('first'))).strip(" {}")
    middle = pybtex.textutils.abbreviate("".join(person.get_part('middle'))).strip(" {}")
    last  = "".join(person.get_part('last')).strip(" {}")
    return pylatexenc.latex2text.latex2text(first+middle+" "+last)

def getyearint(entry):
    return int(entry.fields['year'].strip("{}"))


months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

def getmonthint(entry):
    if 'month' in entry.fields:
        return months.index(entry.fields['month'].strip("{}").lower()[:3] )
    else:
        return 12

publications = [entry for entry  in bib_data.entries.values() if getyearint(entry)>=2017]
publications = sorted(publications, key = lambda entry: (getyearint(entry),getmonthint(entry)) )
#sort_key = [(getyearint(entry),getmonthint(entry)) for entry in publications]
#sort_index  = np.argsort(sort_key)
#print (sort_key, sort_index)
#publications = publications[sort_index]

for entry in publications:
    print (entry.fields['title'])
    print ("     "+", ".join(write_person(person) for person in entry.persons['author']))
#    print (entry)
    print ("     "+str((getyearint(entry),getmonthint(entry))))





fout = open(fout_name, "w")
fout.write(template.header)
fout.write(template.write_table(list_index = 1))
fout.write(template.write_table(list_index = 2,num_citations=10))
fout.write(template.footer)
fout.close()
