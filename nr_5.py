import functools
from itertools import filterfalse


def get_sum(numbers):
    even_numbers = list(filterfalse(lambda number: int(number) % 2, numbers.split(',')))
    numbers_multiplication = functools.reduce(lambda acc, value: acc * int(value), even_numbers, 1)

    print(f'''
    
    Produsul numerelor pare {",".join(list(even_numbers))} dintre cele indicate ({numbers}) este {numbers_multiplication}
    
    ''')


def run(): get_sum(input('Dati numerele separate prin virgula: '))
