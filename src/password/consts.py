PASSWORD_CHARS = {
    'low_alpha': {
        'name': 'Low alpha',
        'regex': 'a-z',
        'value': 'abcdefghijklmnopqrstuvwxyz'
    },
    'up_alpha': {
        'name': 'Up alpha',
        'regex': 'A-Z',
        'value': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    },
    'numeric': {
        'name': 'Numeric',
        'regex': '0-9',
        'value': '0123456789'
    },
    'special': {
        'name': 'Special',
        'regex': ' !#$%&()*+,-./:;=?@[\]^_`{|}~',
        'value': ' !#$%&()*+,-./:;=?@[\]^_`{|}~'
    },
}


PASSWORD_CONFIGS = {
    'all': {
        'low_alpha': True,
        'up_alpha': True,
        'numeric': True,
        'special': True,
    },
    'alpha_num': {
        'low_alpha': True,
        'up_alpha': True,
        'numeric': True,
        'special': False,
    },
    'low_alpha_num': {
        'low_alpha': True,
        'up_alpha': False,
        'numeric': True,
        'special': False,
    },
    'up_alpha_num': {
        'low_alpha': False,
        'up_alpha': True,
        'numeric': True,
        'special': False,
    },
    'alpha': {
        'low_alpha': True,
        'up_alpha': True,
        'numeric': False,
        'special': False,
    },
    'low_alpha': {
        'low_alpha': True,
        'up_alpha': False,
        'numeric': False,
        'special': False,
    },
    'up_alpha': {
        'low_alpha': False,
        'up_alpha': True,
        'numeric': False,
        'special': False,
    },
}