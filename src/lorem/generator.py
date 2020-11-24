from src.lorem.consts import LOREM_POSSIBILITIES
from src.lorem.functions import get_lorem, generate_lorem


class LoremGenerator:
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


    def show_defaults(self):
        items = []
        
        for name in LOREM_POSSIBILITIES:
            items += self.generate_type(name)

        return items
        

    def generate(self, args):
        gen_type = args.pop(0)
        
        for name in LOREM_POSSIBILITIES:
            if name.startswith(gen_type):
                return self.generate_type(name)

        return []