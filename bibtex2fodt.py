import pybtex
import pylatexenc.latex2text
import numpy as np
from pybtex.database.input import bibtex
import template
parser1 = bibtex.Parser()
parser2 = bibtex.Parser()
fout_name = "bibliography_tables.fodt"
start_year = 2017
highlight_author = "Tsirkin"
bibfile="tsirkin-wos-2023-11-17.bib"
bibfile_conf="conferences.bib"
default_quartile=2

def write_person(person):
    first = pybtex.textutils.abbreviate("".join(person.get_part('first'))).strip(" {}")
    middle = pybtex.textutils.abbreviate("".join(person.get_part('middle'))).strip(" {}")
    last  = "".join(person.get_part('last')).strip(" {}")
    fullname =  pylatexenc.latex2text.latex2text(first+middle+" "+last)
    if highlight_author.lower() in fullname.lower():
        return template.text_highlight(fullname)
    else:
        return fullname


def getyearint(entry):
    return int(entry.fields['year'].strip(" {}"))

def getjournal(entry):
    if 'journal' in entry.fields:
        return entry.fields['journal'].strip(" {} ")
    else:
        return "" # we exclude arxivs here

def getquartile(entry):
    if 'quartile' in entry.fields:
        return int(entry.fields['quartile'].strip(" {} "))
    else:
        journal = getjournal(entry).lower()
        if journal =="" :
            return ""
        elif journal in ["phys. rev. lett.", "physical review letters"]:
            return 1
        elif "npj" in journal:
            return 1
        elif "nature" in journal:
            return 1
        else:
            return default_quartile

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

def getmonthint(entry):
    if 'month' in entry.fields:
        return months.index(entry.fields['month'].strip(" {}").lower()[:3] )
    else:
        return 12


def getpages(entry):
    if 'pages' in entry.fields:
        pages = entry.fields['pages'].strip("{} ")
        if "-" in pages:
            pages = pages.split("-")
            return pages[0],pages[-1]
        else:
            return pages,""
    elif "Article-Number" in entry.fields:
        return entry.fields["Article-Number"].strip("{} "),""
    else:
        return "",""

def getplace(entry):
    if 'publisher' in entry.fields:
        return entry.fields['publisher'].strip("{} ")
    elif 'place' in entry.fields:
        return entry.fields['place'].strip("{} ")
    else:
        return ""

def getissn(entry):
    if 'issn' in entry.fields:
        return entry.fields['issn'].strip("{} ")
    else:
        return ""

def getcitations(entry):
    res = None
    if 'times-cited' in entry.fields:
        res = int(entry.fields['times-cited'].strip("{} "))
    elif 'cited' in entry.fields:
        res = int(entry.fields['cited'].strip("{} "))

    # do not write zero citations
    if res is not None and res<=0:
        res=None

    return res

bib_data = parser1.parse_file(bibfile)
print("Articles:",list(bib_data.entries.keys()))
publications = [entry for entry  in bib_data.entries.values() if getyearint(entry)>=start_year and getjournal(entry)!=""]
publications = sorted(publications, key = lambda entry: (getyearint(entry),getmonthint(entry)) )


def isinvited(entry):
    if 'type' in entry.fields:
        if "invited" in entry.fields['type'].lower():
            return True
    return False

def isoral(entry):
    if isinvited(entry):
        return True
    if 'type' in entry.fields:
        if "oral" in entry.fields['type'].lower():
            return True
    return False



bib_data_c = parser2.parse_file(bibfile_conf)
print("conferences:",list(bib_data_c.entries.keys()))
conferences = [entry for entry  in bib_data_c.entries.values() if getyearint(entry)>=start_year and isoral(entry)]
conferences = sorted(conferences, key = lambda entry: (not isinvited(entry),getyearint(entry),getmonthint(entry)) )



def write_entry_as_table_paper(i,entry):
    authors = ", ".join(write_person(person) for person in entry.persons['author'])
    pages = getpages(entry)
    return template.write_table(
        list_index=i,
        title=entry.fields['title'].strip("{} }"),
        journal=getjournal(entry),
        authors=authors,
        quartile=getquartile(entry),
        year=getyearint(entry),
        volume= entry.fields['volume'].strip("{} }"),
        initial_pag=pages[0],
        final_pag=pages[1],
        place=getplace(entry),
        issn=getissn(entry),
        num_citations = getcitations(entry)
        )

def write_entry_as_table_conf(i,entry):
    authors = ", ".join(write_person(person) for person in entry.persons['author'])
    pages = getpages(entry)
    return template.write_table_conf(
        list_index=i,
        title=entry.fields['title'].strip("{} }"),
        authors=authors,
        place=getplace(entry),
        conference=entry.fields['conference'],
        type_contrib=entry.fields['type'],
        date=entry.fields['month']+", "+str(getyearint(entry)),
            )


#                type_contrib="",
#                conference="",
#                date="",
#                place="",
#                publication=""):



fout = open(fout_name, "w")
fout.write(template.header)
for i,entry in enumerate(publications):
    print (entry.fields['title'])
    print ("     "+", ".join(write_person(person) for person in entry.persons['author']))
    print (entry)
    print ("     "+str((getyearint(entry),getmonthint(entry))))
    fout.write(write_entry_as_table_paper(i+1,entry))

#fout.write(template.write_table(list_index = 1))
#fout.write(template.write_table(list_index = 2,num_citations=10))
for i,entry in enumerate(conferences):
    print (entry.fields['title'])
    print ("     "+", ".join(write_person(person) for person in entry.persons['author']))
    print (entry)
    print ("     "+str((getyearint(entry),getmonthint(entry))))
    fout.write(write_entry_as_table_conf(i+1,entry))

fout.write(template.footer)
fout.close()
