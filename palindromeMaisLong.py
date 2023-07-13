def palindromeMaisLong(frase):

    from verificarPalindrome import verificarPalindrome
    maior = ""
    palindromes = []

    for c in range(0, len(frase)):
        esquerda = c-1
        direita = c+1
        
        if esquerda > -1 and direita < len(frase):
            palavra = ""
            palavra += frase[esquerda] + frase[c] + frase[direita]
            
            if verificarPalindrome(palavra):
                palindromes.append(palavra)

                while True:
                    direita += 1
                    if direita < len(frase):
                        palavra = palavra + frase[direita]
                        if verificarPalindrome(palavra):
                            esquerda -= 1
                            if esquerda > -1:
                                palavra = frase[esquerda] + palavra
                                if verificarPalindrome(palavra):
                                    palindromes.append(palavra)
                                    continue
                                else:
                                    break
                            else:
                                break
                        else:
                            esquerda -= 1
                            if esquerda > -1:
                                palavra = frase[esquerda] + palavra
                                if verificarPalindrome(palavra):
                                    palindromes.append(palavra)
                                    continue
                                else:
                                    break
                    else:
                        break            

    if len(palindromes) > 0:
        for c in range(0, len(palindromes)):
            if len(palindromes[c]) > len(maior):
                maior = palindromes[c]
                    
    return(maior)
                    