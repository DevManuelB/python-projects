def fak(n:int) -> int:
    '''Rechnet die Fakultät der angegebene Zahl aus
    
    Der Parameter n ist die angegebene Zahl,
    von der die Fakultät berechnet wird
    Letzte Änderung: 25.04.2022'''

    if n == 0:
        return 1
    else:
        return n * fak(n-1)

'''
eingabe = input("Natürliche Zahl: ")                       <-das wird als kommentar angezeigt, damit ich den 
while eingabe:                                             Rechner in anderen Dateien im Programm nutzen
    fakultät = fak(int(eingabe))                           kann. Die ausgabe wird somit nicht benötigt.
    print("Fakultät von", eingabe + ":", fakultät)
    print()
    eingabe = input("Natürliche Zahl: ")
'''