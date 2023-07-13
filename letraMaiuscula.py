def letraMaiuscula(frase):
    novaFrase = ""
    for c in range(0, len(frase)+1):
        if c - 2 >= 0:
            if frase[c-2] == " ":
                if frase[c-3] == "?" or frase[c-3] == "!" or frase[c-3] == ".":
                    novaFrase += frase[c-1].capitalize()
                else:
                    novaFrase += frase[c-1]
            else:
                novaFrase += frase[c-1]    
        if c - 1 == 0:
            novaFrase += frase[c-1].capitalize()
            
    return(novaFrase)