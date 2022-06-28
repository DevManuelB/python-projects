print('(T)elefonnummer suchen')
print('(N)ame suchen')
print('(E)nde')

speicher = [('Manuel', '49585858'), ('Darnell', '14565656'), ('Kevin', '45989898')]

def suche_nummern(suchwort):
    for name, nummer in speicher:
        if suchwort in name:
            print(name, nummer)

def suche_namen(ziffern):
    for name, nummer in speicher:
        if ziffern in nummer:
            print(name, nummer)

eingabe = input('Auswahl (t, n, e): ')

while eingabe != 'e':
    if eingabe == 't':
        suchwort = input('Suchwort: ')
        suche_nummern(suchwort)
    elif eingabe == 'n':
        ziffern = input('Ziffern: ')
        suche_namen(ziffern)

    print('(T)elefonnummer suchen')
    print('(N)ame suchen')
    print('(E)nde')

    eingabe = input('Auswahl (t, n, e): ')

print('Bis bald!')
