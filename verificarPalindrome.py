def verificarPalindrome(frase):
    frase = frase.lower()
    fraseInversa = ""

    for c in range(1, len(frase)+1):
        fraseInversa += frase[-c]
        
    if frase == fraseInversa:
        return True
        
    else: 
        return False