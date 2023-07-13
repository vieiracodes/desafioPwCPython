from reverterOrdem import reverterOrdem
from removerCaracDup import removerCaracDup
from palindromeMaisLong import palindromeMaisLong
from letraMaiuscula import letraMaiuscula
from verificarPalindrome import verificarPalindrome

print("    Bem vindo ao Desafio PwC! \nQual exercício você deseja executar?\n")
while True:
    
    option = int(input("""------- Digite o número referente a opção desejada -------\n
Ex [1] - Reverter a ordem das palavras em uma frase
Ex [2] - Remover todos os caracteres duplicados
Ex [3] - Encontrar a palavra palindrome mais longa de uma frase
Ex [4] - Colocar letras maiúsculas em uma frase
Ex [5] - Verificar se a string é palindrome

[9] - Executar casos de teste
[0] - Sair
"""))
    
    if option == 1:
        frase = input("\nDigite uma frase: ")
        output = reverterOrdem(frase)
        print("Resultado: " + output + "\n")
        
    if option == 2:
        frase = input("\nDigite uma frase: ")
        output = removerCaracDup(frase)
        print("Resultado: " + output + "\n")

    if option == 3:
        frase = input("\nDigite uma frase: ")
        output = palindromeMaisLong(frase)
        print("Resultado: " + output + "\n")
        
    if option == 4:
        frase = input("\nDigite uma frase: ")
        output = letraMaiuscula(frase)
        print("Resultado: " + output + "\n")
        
    if option == 5:
        palavra = input("\nDigite uma palavra:")
        output = verificarPalindrome(palavra)
        if output:
            print("É palindrome\n")
        else:  
            print("Não é palindrome\n")

        
    if option == 9:
        print("\nEx 1 - Reverter ordem:")
        output = reverterOrdem("Hello, World! OpenAI is amazing.")
        print(output)
        
        print("\nEx 2 - Remover caracteres duplos:")
        output = removerCaracDup("Hello, World!")
        print(output)
        
        print("\nEx 3 - Palindrome mais longa:")
        output = palindromeMaisLong("babad")
        print(output)
        
        print("\nEx 4 - Letras maiúsculas:")
        output = letraMaiuscula("hello. how are you? i'm fine, thank you.")
        print(output)
        
        print("\nEx 5 - Verificar palindrome: ")
        output = verificarPalindrome("racecar")
        print(output)
        
        
    if option == 0:
        break