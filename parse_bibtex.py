import pybtex
from pybtex.database.input import bibtex
parser = bibtex.Parser()
bib_data = parser.parse_file('bibliography.bib')
print(list(bib_data.entries.keys()))


def get_title(entry):
    from pybtex.plugin import find_plugin
    style = find_plugin('pybtex.style.formatting', 'plain')()
    backend = find_plugin('pybtex.backends', 'plaintext')()
    sentence = style.format_title(entry, 'title')
    data = {'entry': entry,
            'style': style,
            'bib_data': None}
    T = sentence.f(sentence.children, data)
    title = T.render(backend)
    return title

def write_person(person):
    first = pybtex.textutils.abbreviate("".join(person.get_part('first')))
    middle = pybtex.textutils.abbreviate("".join(person.get_part('middle')))
    last  = "".join(person.get_part('last'))
    return first+middle+" "+last

for k,v in bib_data.entries.items():
    print (k,get_title(v))
    print ("     "+", ".join(write_person(person) for person in v.persons['author']))
