import random
tah_pocitace = random.choice(['kamen', 'papir', 'nuzky'])
tah_cloveka = input('kamen, nuzky, nebo papir? ')

if tah_pocitace == tah_cloveka:

    print('Plichta')
else:
    if tah_pocitace == 'kamen':
        if tah_cloveka == 'papir':
            print('Vyhrál jsi!')
        else:
            print('Počítač vyhrál.')
    else:
        if tah_cloveka == 'nuzky':
            print('Vyhrál jsi!')
        else:
            if tah_pocitace
    else:
        if tah_pocitace == 'papir':
            if tah_cloveka == 'kamen':
                print('Počítač vyhrál.')
            else:
                print('Vyhrál jsi!')
        else:
            if tah_pocitace == 'nuzky':
                if tah_cloveka == 'kamen':
                    print('Vyhrál jsi!')
                else:
                    print('Počítač vyhrál.')
