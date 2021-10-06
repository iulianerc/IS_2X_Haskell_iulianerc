import math


def area(a, b, c):
    semi_perimeter = (a + b + c) / 2
    area = math.sqrt(semi_perimeter * (a - semi_perimeter) * (semi_perimeter - b) * (semi_perimeter - c))

    print(f'''
    
    Aria triunghiului este de {area}
    
    ''')


def run():
    a = float(input('Dati lungimea laturii a: '))
    b = float(input('Dati lungimea laturii b: '))
    c = float(input('Dati lungimea laturii c: '))

    area(a, b, c)
