from re import findall

class Spell:

    # Initialize spell from JSON data.
    def __init__(self, json):
        self.name = json['name'].title()
        self.school = json['school']
        self.level = json['level']
        self.casting_time = json['casting_time']
        self.is_ritual = json['is_ritual']
        self.range = json['range']
        self.has_verbal = json['components']['has_verbal']
        self.has_somatic = json['components']['has_somatic']
        self.has_material = json['components']['has_material']
        self.consumes_material = json['components']['consumes_material']
        self.components_description = json['components']['description']
        self.duration = json['duration']
        self.require_concentration = json['require_concentration']
        self.description = json['description']
        self.at_higher_levels = json['at_higher_levels']
        self.has_long_description = json['has_long_description']

    # Get spell school and level description.
    # Eg. "Abjuration - 2nd Level"
    def school_slot_string(self):
        return f"{self.school.title()} — {self._level_string()}"

    # Get spell level description.
    # Eg. "3rd Level"
    def _level_string(self):
        match int(self.level):
            case 0: return 'Cantrip'
            case 1: return '1st Level'
            case 2: return '2nd Level'
            case 3: return '3rd Level'
            case _: return f'{self.level}th Level'

    # Get spell casting time description.
    # Eg. "1 Action (ritual)"
    def cast_time_string(self):
        cast_time = self.casting_time.title()
        ritual = f' (ritual)' if self.is_ritual else ''
        return f'{cast_time}{ritual}'

    # Get spell range description.
    # Eg. "120 ft"
    def range_string(self):
        match self.range.lower():
            case 'touch' | 'self' | 'unlimited': return self.range.capitalize()
            case _: return f'{self.range} ft'

    # Get spell components description.
    # Eg. "VS"
    def components_string(self):
        components = ''
        if self.has_verbal: components += 'V'
        if self.has_somatic: components += 'S'
        if self.has_material: components += 'M'
        return components

    # Get spell material components description.
    # Eg. "(pinch of talc and silver)"
    def material_components_string(self):
        if not self.has_material: return ''
        return f'({self.components_description}){"*" if self.consumes_material else ""}'

    # Get spell duration description.
    # Eg. "1 Minute"
    def duration_string(self):
        return self.duration.title() if not self.require_concentration else "Concentration"

    # Get spell concentration description.
    # Eg. "(up to 10 minutes)"
    def concentration_time_string(self):
        if not self.require_concentration: return ''
        return f"(up to {self.duration.lower()})"

    # Get spell description with HTML formatters.
    # Eg. replaces "**text**" with "<b>text</b>"
    def _formatted_text(self, text):
        formatted_text = text
        regexes = [(r'\*\*(.*?)\*\*', '**', 'b'), (r'__(.*?)__', '__', 'u')]
        for regex, md_tag, html_tag in regexes:
            for find in findall(regex, formatted_text):
                formatted_text = formatted_text.replace(f'{md_tag}{find}{md_tag}', f'<{html_tag}>{find}</{html_tag}>')

        formatted_text = formatted_text.replace('\n', '<br>')
        return formatted_text

    # Get spell description with HTML formatters.
    def formatted_description(self):
        return self._formatted_text(self.description)

    # Get spell scaling with HTML formatters.
    def formatted_scaling(self):
        return self._formatted_text(self.at_higher_levels)

    def has_material_components_description(self):
        return self.material_components_string() != ''

    def has_level_scaling(self):
        return self.at_higher_levels != ''

    # HTML classes helpers

    def html_add_divshort(self):
        return self.require_concentration or self.has_material_components_description()

    def html_add_descriptionLong(self):
        return self.has_long_description

    def html_add_components_topText(self):
        return self.require_concentration and not self.has_material_components_description()

    def html_add_duration_topText(self):
        return not self.require_concentration and self.has_material_components_description()

    def html_add_rightBorder(self):
        return not self.require_concentration or self.has_material_components_description()

    def html_add_leftBorder(self):
        return self.require_concentration and not self.has_material_components_description()
