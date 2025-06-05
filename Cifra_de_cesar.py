
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"

texto = input("Digite o texto: ")
chave = int(input("Digite a chave: "))
cifrado = ""

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
