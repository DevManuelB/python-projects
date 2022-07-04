from random import choice

def aufgabe(d):
    vokabel = choice(list(d.keys()))

    print()
    print('Nennen Sie ein deutsches Wort für ' + vokabel)
    antwort = input('Deutsches Wort: ')

    if antwort not in d[vokabel]:
        print('Leider Falsch.')
        print(vokabel , ' bedeutet: ', end=' ')
        for wort in d[vokabel]:
            print(wort, end=' ')
    else:
        del d[vokabel]
        print('RICHTIG!')



d = {'sun': ['Sonne'],
     'key': ['Taste', 'Schlüssel'],
     'head': ['Kopf', 'Chef', 'Leiter']}

while d:
    aufgabe(d)

print('Sie haben alle Vokabeln gelernt.')
