import random
from colorama import Fore
# use ">pip install colorama" ou simplesmente apague o import.
# se estiver no vscode, adicione  "code-runner.runInTerminal": true no settings.json

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
    n = jogarDado()
    print(f"você tirou {n}!")
    
    if casa_jogador < tabuleiro[fila_jogador]:
        casa_jogador = min(casa_jogador + n, tabuleiro[fila_jogador])
    else:
        if n == 4:
            print("você passou para a próxima fila!")
            fila_jogador = 0 if fila_jogador + 1 >= len(tabuleiro) else fila_jogador+1
            if (fila_jogador == 0):
                pontuacao += 1
                print("você deu uma volta no tabuleiro!")
        else:
            print("você voltou para o começo da fila!")
        casa_jogador = 1
        
    pontuacao_fracionada = pontuacao + (fila_jogador / len(tabuleiro))
    print(f"pontuação atual: {pontuacao} | pontuação fracionada: {pontuacao_fracionada:.2f}")
    print()
        

tabuleiro = [9, 8, 10, 12, 7, 5]
fila_jogador = 0
casa_jogador = 1
pontuacao = 0

mostraTabuleiro(tabuleiro, fila_jogador, casa_jogador)

t = input("quantas jogadas você que fazer? ")
for i in range(int(t)):
    print("---------------------------------------------------------------------------------") 
    print(f"JOGADA {i+1}")
    print("---------------------------------------------------------------------------------")
    
    jogada()
    mostraTabuleiro(tabuleiro, fila_jogador, casa_jogador)

### se quiser fazer cada jogada com enter ###

# t = input("aperte enter para rodar um dado (\"q\" para sair)") 
# i = 1
# while t != "q":
#     print("---------------------------------------------------------------------------------") 
#     print(f"JOGADA {i+1}")
#     print("---------------------------------------------------------------------------------")
#     i += 1     
#   
#     jogada()
#     mostraTabuleiro(tabuleiro, fila_jogador, casa_jogador)
#     t = input("aperte enter para rodar um dado (\"q\" para sair)")
