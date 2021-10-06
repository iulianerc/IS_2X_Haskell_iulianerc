def run():
    print('Progressing!')
    # find_type(input('Indicati caracterul: '))


def find_type(char: str):
    print('''
        1: If
        2: Array
        3: Switch (hasn't been released yet)
    ''')

    methods[input('Selectați metoda dorita: ')](char)


def by_if(char: str):
    if char.isupper():
        return 'Characterul dat este o litera mare'

    if char.islower():
        return 'Characterul dat este o litera mica'

    if char.isnumeric():
        return 'Characterul dat este o cifra'

    return 'Characterul dat este un symbol'


# def by_switch(char: str):
#     x = 'test'
#     match x:
#         case 'test':
#             print("hasn't been released yet")


def by_array(char: str):
    available_methods_name = available_checks_methods.keys()

    # for check_method_index in range(len(available_checks_methods)):
    print('')
    # method_name = available_methods_name.check_method_index
    # if char[method_name]:
    #     print(available_checks_methods[])
    print(available_checks_methods.keys())


available_checks_methods = {
    'islower': {
        'check': lambda char: char.islower,
        'text': 'Characterul dat este o litera mica'
    },
    'isupper': {
        'check': lambda char: char.isupper,
        'text': 'Characterul dat este o litera mare'
    },
    'isnumeric': {
        'check': lambda char: char.isnumeric,
        'text': 'Characterul dat este o cifra'
    },
    'is_symbol': {
        'check': True,
        'text': 'Characterul dat este un symbol'
    }
}

methods = {
    '1': by_if,
    '2': by_array,
    # '3': by_switch,
}
