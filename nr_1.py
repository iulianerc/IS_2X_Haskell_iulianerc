import functools


def calc_salary(raw_salary, addition, tax):
    tax = functools.reduce(lambda acc, value: float(acc) + float(value), tax)

    without_tax = raw_salary + addition
    final_salary = without_tax - without_tax * tax / 100

    if final_salary > 1000000:
        print('''
        
        Eh luna asta cam putin, ({final_salary}) $ totusi nu-i chiar asa de putin
        
        ''')
    else:
        print('''
        
        Da cum poti sa traiesti cu {final_salary} $ / luna ???? !!!
        
        ''')


def run():
    raw_salary = float(input('Indicati salariul dupa contract: '))
    addition = float(input('Ati primit ceva bonusuri? Ati putea si nou sa ne spuneti: '))
    tax = input('Ce taxe aveti la salariu in  procente, indicati prin virgula: ').split(',')

    calc_salary(raw_salary, addition, tax)

