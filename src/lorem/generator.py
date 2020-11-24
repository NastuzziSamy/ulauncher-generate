from src.lorem.consts import LOREM_POSSIBILITIES
from src.lorem.functions import get_lorem, generate_lorem


class LoremGenerator:
    def show_defaults(self):
        return LOREM_POSSIBILITIES.values();


    def generate_type(self, name):
        get = get_lorem(name)
        gen = generate_lorem(name)

        return [
            {
                'name': get,
                'description': 'Select to copy classic lorem ' + name,
                'copy': get,
            },
            {
                'name': gen,
                'description': 'Select to copy generated lorem ' + name,
                'copy': gen,
            },
        ]

    def generate(self, args):
        gen_type = args.pop(0)
        
        for (name, data) in LOREM_POSSIBILITIES.items():
            if name.startswith(gen_type):
                return self.generate_type(name)

        return []