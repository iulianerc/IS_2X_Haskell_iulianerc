import functools


def get_sum(n):
    numbers_sum = functools.reduce(lambda acc, value: acc + value, range(n))

    print(f'''
    Suma primelor {n} numere naturale este {numbers_sum}
    
    ''')


def run(): get_sum(int(input('Dati pana la ce numar sa fie calculata suma: ')))
