import string
import os

maiusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase

def limpar():
    os.system("cls")
    
def codificar(cifrado):
    for letra in texto:
        if letra in maiusculas:
            posicao = maiusculas.find(letra)
            nova_posicao = (posicao + chave) % len(maiusculas)#O % faz com que volte para a identação da listam,usando com exemplo caso o valor 
            cifrado += maiusculas[nova_posicao]               #seja 56 e passe da lista(26), essa função faz retornar.
        elif letra in minusculas:
            posicao = minusculas.find(letra)
            nova_posicao = (posicao + chave) % len(minusculas)
            cifrado += minusculas[nova_posicao]
        else:
            cifrado += letra
    print(cifrado)
    
def descifrar(descifrar):
    for letra in texto:
        if letra in maiusculas:
            posicao = maiusculas.find(letra)
            nova_posicao = (posicao - chave) % len(maiusculas)#O % faz com que volte para a identação da listam,usando com exemplo caso o valor 
            descifrar += maiusculas[nova_posicao]               #seja 56 e passe da lista(26), essa função faz retornar.
        elif letra in minusculas:
            posicao = minusculas.find(letra)
            nova_posicao = (posicao - chave) % len(minusculas)
            descifrar += minusculas[nova_posicao]
        else:
            descifrar += letra
    print(descifrar)

    
    
opcoes = [0,1,""]

while True:
    inicio = int(input("Oque deseja fazer hoje?\n0 - codificar 1 - decifrar\n"))
    limpar()
    if inicio in opcoes:
        if inicio == 0:
            texto = input("Digite o texto: ")
            chave = int(input("Digite a chave: "))
            cifrado = ""
            codificar(cifrado)
            
        elif inicio == 1:
            texto = input("Digite o texto: ")
            chave = int(input("Digite a chave: "))
            descifrado = ""
            descifrar(descifrado)
        break
    else:
        continue
