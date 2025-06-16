import os
#os.system('cls' if os.name == 'nt' else 'clear')## limpar o console

opcoes = [0,1,2,""]
carros_disponiveis = [
    ("Chevrolet Tracker" ,120),
    ("Chevrolet Onix" ,90),
    ("Chevrolet Spin" ,150),
    ("Hyundai HB20" ,85),
    ("Hyundai Tucson" ,120),
    ("Fiat Uno" ,60),
    ("Fiat Mobi" ,70),
    ("Fiat Pulse" ,130)
]
alugado = []
def limpar_console():
    os.system("cls")

def catalogo():
    for i , car in enumerate(carros_disponiveis):
        print("[{}] {} - R${} /dia".format(i,car[0], car[1]))
def devolver():
    for i , car in enumerate(alugado):
        print("[{}] {} ".format(i,car[0]))
            
incial = ("----------------------\n Bem vindo à locadora \n----------------------\nOque deseja fazer?\n0 - mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
barra = ("-------------")
while True:
    print(incial)
    oque_deseja = int(input())
    limpar_console()
    if oque_deseja in opcoes:
        if oque_deseja == 0:
            catalogo()
            voltar = int(input("0 - continuar | 1 - sair\n"))
            #voltar pra pag inicial
            if voltar == 0:
                limpar_console()
                continue 
                
            elif voltar == 1:
                print("Você escolheu sair.")
                break
                
        if oque_deseja == 1:
            catalogo()   
            print(barra)
            
            codigo = int(input("Escolha o código do carro:\n"))
            dias = int(input("Por quantos dias quer alugar o carro?\n"))
            
            limpar_console()

            print("Você escolheu {} por {} dias.".format(carros_disponiveis[codigo][0], dias))
            conta = dias * carros_disponiveis[codigo][1]
            
            print(f"O Aluguel totalizaria R${conta}. Deseja alugar?")
            alugar = int(input("0 - Sim | 1 - Não\n"))
            if alugar == 0:
                retirar = carros_disponiveis.pop(codigo)
                alugado.append(retirar)
                print("Você alugou {} por {} dias.".format(retirar[0], dias))
            else:
                continue
            
            print(barra)
            
            voltar = int(input("0 - continuar | 1 - sair\n"))
            #voltar pra pag inicial
            if voltar == 0:
                limpar_console()
                continue 
                
            elif voltar == 1:
                print("Você escolheu sair.")
                break
            
        if oque_deseja == 2:
            if len(alugado) == 0:
                print("Você não devolveu nenhum carro. Deseja voltar para a pagina inicial?")
                voltar = int(input("0 - continuar | 1 - sair\n"))
                #voltar pra pag inicial
                if voltar == 0:
                    limpar_console()
                    continue 
                
                elif voltar == 1:
                    print("Você escolheu sair.")
                    break
            elif alugado:
                print("Segue a lista de carros alugados. Qual você deseja devolver?")
                devolver()
                    
                car_devolver = int(input("Escolha o codigo do carro que deseja devolver:\n"))
                print("Deseja devolver {}?\n0 - Sim | 1- Não".format(alugado[car_devolver][0]))
                decida = int(input())
                if decida == 0:
                    retornar = alugado.pop(car_devolver)
                    carros_disponiveis.append(retornar)
                    print("Você devolveu o {} para a locadora".format(retornar[0]))
                else:
                    print("Você não devolveu nenhum carro")
            
            print(barra)
            
            voltar = int(input("0 - continuar | 1 - sair\n"))
            #voltar pra pag inicial
            if voltar == 0:
                limpar_console()
                continue 
                
            elif voltar == 1:
                print("Você escolheu sair. troxa")
                break
                
    else:
        print("Somente as opções acima")
        continue
    
