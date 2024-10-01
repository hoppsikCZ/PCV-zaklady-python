import time

body = 0
maximum_bodu = 2

print('Vítám tě u krátkého dotazníku.')
odpoved = input('1. Je toto tvrzení pravdivé: Právě jsi odpověděl NE ')
print(f'Když se znova pořádně koukneš na zadání, tak je tvá odpověď {odpoved} špatně.')

odpoved = input('2. Kolik uběhlo milisekund od 1. ledna 1970 UTC? ')
if (odpoved == time.time() * 1000):
    print('Správně!')
    body += 1
else:
    print('Špatně! To se ani neumíš kouknout na hodiny?')

odpoved = input('3. Líbí se ti tento dotazník? (ano) ')
if (odpoved.lower() == 'ano'):
    print('Tak to je samozřejmé. Dostáváš svůj první (a poslední) bod.')
    body += 1
elif (odpoved.lower() == 'ne'):
    print('Špatná odpověď. Za selhání na takto jednoduché otázce ztrácíš bod.')
    body -= 1
else:
    print('Nerozumím tvé odpovědi. Bez bodu.')

print('Dotazník je u konce. Vaše hodnocení:')

if (body == maximum_bodu):
    print(f'Gratuluji! Nějakým záhadným způsobem jsi získal {body} body, což je maximální možný počet.')
elif (body > 0):
    print(f'Získal jsi {body} bodů. Máš co dohánět.')
else:
    print(f'Jak je vůbec možné, že jsi získal {body} bodů?')

