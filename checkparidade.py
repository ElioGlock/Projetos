import os
from decoradores import imprimir_centralizado_com_caixa

def verificar_primo(n):
    count = 0
    lista=[]
    for cada_n in range(1, n + 1):
        if n % cada_n == 0:
            count +=1 
            lista.append(cada_n)
        else:
            pass
    if count == 2:
        return "PRIMO"
    else:
        return "N° COMPOSTO", lista
    
imprimir_centralizado_com_caixa("Bem vindo ao detector de numeros Primos!")
digite = int(input("Digite o numero que deseja verificar\n>>"))
caixa = verificar_primo(digite)
imprimir_centralizado_com_caixa("{}, {} é divisivel por {}".format(caixa[0],digite,caixa[1]))
