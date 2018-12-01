koncetina = int(input('Kolik máš končetin: '))
if koncetina < 0:
    print('Ne všichni vstoupíme do nirvány.')
elif koncetina == 0:
    print('I bakterie má právo na život')
elif koncetina <= 2:
    print('Ještě jsi ve vývinu, počkej pár mutací a bude to dobré.')
elif koncetina <= 4:
    print('Gratuluji! Jsi na vrcholu potravního řetězce.')
elif koncetina == 5:
    print('Spočítal/a sis je správně?')
elif koncetina <= 8:
    print('Scary hairy thing. Get away from me!')
else:
    print('I am impressed.')
