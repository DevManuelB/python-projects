def nachricht(text:str ="", an:str ="Mensch") -> str:
    '''Ausgeben eines Textes mit Namen und Aussage

    Der Parameter Text hat die Voreinstellung nichts
    auszugeben, kann aber auch einen zugewiesenen text 
    ausgeben.
    Der Parameter an hat die Voreinstellung Mensch als
    Namen auszugeben , kann aber auch einen zugewiesenen
    Namen ausgeben.
    Letzte Änderung: 16.04.2022'''
    return "Hallo " + an + "! " + text

print(nachricht(an="Manuel", text="Ich hoffe dir geht es gut!"))
