import nr_1
import nr_2
import nr_3
import nr_4
import nr_5

programs = {
    '1': nr_1.run,
    '2': nr_2.run,
    '3': nr_3.run,  # todo: Finish
    '4': nr_4.run,
    '5': nr_5.run,
}

while True:
    print('''
    
    1: Determinarea salariului.
    2: Determinarea ariei unui triunghi.
    3: Determinarea tipului unui caracter introdus. !!!(Progressing)!!!
    4: Suma primelor (n) numere naturale.
    5: Produsul numerelor pare introduse.
    
    ''')

    exercise_nr = input('Care excercitiu doriti sa testati? Indicati un numar din cele prezente sau tapati cancel: ')

    if exercise_nr == 'cancel':
        break

    try:
        programs[exercise_nr]()
    except Exception as e:
        # raise e
        print('''
        ___________________________________________________________________________
        A intervenit o eroare in program, incercati din nou!
        ___________________________________________________________________________
        ''')

        continue
