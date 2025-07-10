import string
import os
import time

a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation
all = a + b + c + d

def limpar():
    os.system("cls" if os.name == 'nt' else 'clear') 


def imprimir_centralizado_com_caixa(texto):
    try:
        largura_terminal = os.get_terminal_size().columns
    except OSError:
        largura_terminal = 80

    if len(texto) > largura_terminal - 4:
        texto = texto[:largura_terminal - 4]

    texto_centralizado = texto.center(largura_terminal - 2)

    linha_superior = '┌' + '─' * (largura_terminal - 2) + '┐'
    linha_meio = '│' + texto_centralizado + '│'
    linha_inferior = '└' + '─' * (largura_terminal - 2) + '┘'

    print(linha_superior)
    print(linha_meio)
    print(linha_inferior)


def codificar(texto_original, chave_original):
    cifrado = ""
    for letra in texto_original:
        if letra in all:
            posicao = all.find(letra)
            nova_posicao = (posicao + chave_original) % len(all)
            if chave_original % 94 == 0:
                cifrado += all[nova_posicao + 56]
            else:
                cifrado += all[nova_posicao]
        else:
            cifrado += letra
    return cifrado

def descriptografar(texto_cifrado, chave_original): 
    descifrar = ""
    for letra in texto_cifrado:
        if letra in all:
            posicao = all.find(letra)
            nova_posicao = (posicao - chave_original) % len(all)
            if chave_original % 94 == 0:
                descifrar += all[nova_posicao - 56]
            else:
                descifrar += all[nova_posicao]
        else:
            descifrar += letra
    return descifrar 


opcoes = [0,1,""]

while True:
    try:
        limpar()
        # Você também pode usar a função para o menu, se quiser
        imprimir_centralizado_com_caixa("O que deseja fazer hoje?")
        print("0 - Codificar | 1 - Decifrar | 2 - Sair")
        inicio = int(input(">> "))

        if inicio == 0:
            while True:
                try:
                    texto = input("Digite o texto:\n>> ")
                    chave = int(input("Digite uma chave (somente n° Inteiros):\n>> "))
                    resultado_cifrado = codificar(texto, chave)
                    print("\nTexto Criptografado abaixo:")
                    imprimir_centralizado_com_caixa(resultado_cifrado)
                    time.sleep(10)
                    break
                except ValueError:
                    limpar()
                    print("Você só pode usar n° Inteiros para a chave.")
                    continue
        elif inicio == 1:
            while True:
                try:
                    texto = input("Digite o texto:\n>> ")
                    chave = int(input("Digite uma chave (somente n° Inteiros):\n>> "))
                    resultado_descifrado = descriptografar(texto, chave)
                    print("\nTexto descriptografado abaixo:")
                    imprimir_centralizado_com_caixa(resultado_descifrado)
                    time.sleep(10)
                    break
                except ValueError:
                    limpar()
                    print("Você só pode usar n° Inteiros para a chave.")
                    continue
        elif inicio == 2:
            break
    except ValueError:
        continue