def reverterOrdem(frase):

    palavras = frase.split()
    inversao = ""
    for c in range (1, len(palavras)+1):
        inversao +=  palavras[-c] + " "
        
    return inversao