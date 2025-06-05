import os
import math

while True:
    print("0 - soma \n1 - subtração \n2 - multiplicação \n3 - divisão \n4 - exponenciação \n5 - radiciação")

    operacao = int(input("Qual operação quer realizar?"))


    a = float(input("Qual o 1° valor? "))
    b = float(input("Qual o 2° valor? "))

    operacoes = {
        0: lambda a, b: a + b,
        1: lambda a, b: a - b,
        2: lambda a, b: a * b,
        3: lambda a, b: a / b if b != 0 else "Erro: divisão por zero",
        4: lambda a, b: a ** b,
        5: lambda a, b: a ** (1 / b) if b != 0 else "Erro: radiciação com expoente zero"
    }

    if operacao in operacoes:
        resultado = operacoes[operacao](a, b)
        print(f"Resultado: {round(resultado, 2)}")
    else:
        print("Operação inválida.")
        
    
    while True:
        continuar = input("Deseja continuar?(S/N)") 
        if continuar != "S" and continuar != "N":
            print("Você só pode digitar (S/N)")
            continue
        else:
            break
    if continuar == "S":
        os.system('cls' if os.name == 'nt' else 'clear')## limpar o console
        continue
    else:
        os.system('cls' if os.name == 'nt' else 'clear')## limpar o console
        break
   
        

        
    
