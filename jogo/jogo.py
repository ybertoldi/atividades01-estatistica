import random
from colorama import Fore

def mostraTabuleiro(tabuleiro, fila_jogador, casa_jogador):
    
    for i in range(len(tabuleiro)):
        print(f"fila {i+1}\t", end="")
        tamanho_fila = tabuleiro[i]
        
        for j in range(1, tamanho_fila + 1):
            if fila_jogador == i and casa_jogador == j:
                print(Fore.GREEN + "|P|" + Fore.WHITE, end="")
            else:
                print(f"|{j}|", end="")
            
            
            if j < tamanho_fila:
                print("-", end="")
        print()
    print()

def jogarDado():
    return random.randint(1,6)

def jogada():
    global tabuleiro, fila_jogador, casa_jogador, pontuacao
    print("---------------------------------------------------------------------------------")    
    n = jogarDado()
    print(f"você tirou {n}!\n")
    
    if casa_jogador < tabuleiro[fila_jogador]:
        casa_jogador = min(casa_jogador + n, tabuleiro[fila_jogador])
    else:
        if n == 4:
            fila_jogador = 0 if fila_jogador + 1 >= len(tabuleiro) else fila_jogador+1
            if (fila_jogador == 0):
                pontuacao += 1
        casa_jogador = 1
        

tabuleiro = [9, 8, 10, 12, 7, 5]
fila_jogador = 0
casa_jogador = 1
pontuacao = 0

mostraTabuleiro(tabuleiro, fila_jogador, casa_jogador)

t = input("quantas jogadas você que fazer? ")

for i in range(int(t)):
    jogada()
    mostraTabuleiro(tabuleiro, fila_jogador, casa_jogador)


### se quiser fazer cada jogada com enter ###
#     
# t = input("aperte enter para rodar um dado (\"q\" para sair)") 
#
# while t != "q":
#     jogada()
#     mostraTabuleiro(tabuleiro, fila_jogador, casa_jogador)
#     t = input("aperte enter para rodar um dado (\"q\" para sair)")