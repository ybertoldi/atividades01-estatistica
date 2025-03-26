import csv
import random

def achaTamanhoAmostra(erro_toleravel, tamanho_populacao):
    n0 = 1/(erro_toleravel ** 2)
    n = (tamanho_populacao * n0) / (tamanho_populacao + n0)
    return n

def geraAleatorio(limite):
    global achados
    
    rand = random.randint(0, limite)
    while rand in achados:
        rand = random.randint(0, limite)
    achados.add(rand)
    
    return rand

achados = set()
path_populacao = r"idades.csv"
path_amostra = r"amostra_idades.csv"

ERRO_TOLERAVEL = 0.05
TAMANHO_POPULACAO = 10000
tamanho_amostra = achaTamanhoAmostra(ERRO_TOLERAVEL, TAMANHO_POPULACAO)
print(tamanho_amostra)

pop = []
with open(path_populacao, "r") as f:
    reader = csv.reader(f)
    for line in reader:
        pop.append(line[0])

amostra = []
while len(amostra) < tamanho_amostra:
    val = pop[geraAleatorio(TAMANHO_POPULACAO)]
    amostra.append(val)           

with open(path_amostra, "w", newline='') as f:
    writer = csv.writer(f)
    for idade in amostra:
        writer.writerow([idade])

