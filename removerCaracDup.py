def removerCaracDup(frase):
    semRep = []
    novaFrase = ""
    for c in range(0, len(frase)):
        if frase[c].capitalize() not in semRep:
            semRep.append(frase[c].capitalize())
            novaFrase += frase[c]

    return(novaFrase)