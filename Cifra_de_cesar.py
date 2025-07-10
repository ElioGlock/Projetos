import string
import os
import time

a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation
all = a + b + c + d
# minusculas = string.ascii_lowercase
# numeros = string.digits

def limpar():
    os.system("cls")
    
def codificar(cifrado):
    for letra in texto:
        if letra in all:
            posicao = all.find(letra)
            nova_posicao = (posicao + chave) % len(all)#O % faz com que volte para a identação da listam,usando com exemplo caso o valor seja 56 e passe da lista(26), essa função faz retornar.
            if chave % 94 == 0:
                cifrado += all[nova_posicao + 56] 
            else:
                cifrado += all[nova_posicao]  

        else:
            cifrado += letra
    print(cifrado)
    
def descriptografar(descifrar):
    for letra in texto:
        if letra in all:
            posicao = all.find(letra)
            nova_posicao = (posicao - chave) % len(all)
            if chave % 94 == 0:
                descifrar += all[nova_posicao - 56] 
            else:
                descifrar += all[nova_posicao]               
        else:
            descifrar += letra
    print(descifrar)


    
opcoes = [0,1,""]

while True:
    try:
        limpar()
        inicio = int(input("Oque deseja fazer hoje?\n0 - codificar 1 - decifrar\n"))
        if inicio == 0:
            while True:
                try:
                    texto = input("Digite o texto:\n")
                    chave = int(input("Digite uma chave, somente n° Inteiros:\n"))
                    cifrado = ""
                    print("Texto Criptografado abaixo:")
                    codificar(cifrado)
                    time.sleep(5)
                    break
                except ValueError:
                    limpar()
                    print("Você só pode usar n° Inteiros")
                    continue
        elif inicio == 1:
            while True:
                try:
                    texto = input("Digite o texto:\n")
                    chave = int(input("Digite uma chave, somente n° Inteiros:\n"))
                    descifrado = ""
                    print("Texto descriptografado abaixo:")
                    codificar(descifrado)
                    time.sleep(5)
                    break
                except ValueError:
                    limpar()
                    print("Você só pode usar n° Inteiros")
                    continue
    except ValueError:
        continue
    
    
    
    

    
    

