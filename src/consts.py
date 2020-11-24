from src.lorem.generator import LoremGenerator


ICON_DIR = 'images/'
ICON_FILE = ICON_DIR + 'icon.png'

GENERATORS = {
    'lorem': {
        'name': 'Lorem ipsum',
        'description': 'Generate lorem ipsum texts',
        'class': LoremGenerator
    },
}