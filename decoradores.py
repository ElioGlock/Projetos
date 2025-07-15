import os

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
