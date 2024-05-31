from json import load
from jinja2 import Environment, FileSystemLoader

from spell import Spell

__page_size = 8

def divide_chunks(list, chunk_size):
    for it in range(0, len(list), chunk_size):
        yield list[it:it + chunk_size]

spells = {
    'cantrips': [], '1st': [], '2nd': [], '3rd': [], '4th': [], '5th': [], '6th': [], '7th': [], '8th': [], '9th': []
}

# Load spells data from json files.
for key in spells.keys():
    with open(f'data/{key}.json') as file:
        json_spells = [Spell(spell_json) for spell_json in load(file)]
        spells[key] = list(divide_chunks(json_spells, __page_size))

# Setup Jinja2 templates
jinja_env = Environment(loader=FileSystemLoader('templates'))
spell_page_template = jinja_env.get_template('page.j2')
spellbook_template = jinja_env.get_template('spellbook.j2')

pages = []
for level in spells.keys():
    pages.append(''.join([spell_page_template.render(spells=spells) for spells in spells[level]]))

with open('spellbook/spellbook.html', 'w', encoding='utf-8') as file:
    file.writelines(spellbook_template.render(pages=pages))
