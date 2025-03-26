import random
import statistics as stat

def achaTamanhoAmostra(erro_toleravel, tamanho_populacao):
    n0 = 1/(erro_toleravel ** 2)
    n = (tamanho_populacao * n0) / (tamanho_populacao + n0)
    return n

def geraIdxAleatorio(limite):
    global achados
    
    rand = random.randint(0, limite - 1)
    while rand in achados:
        rand = random.randint(0, limite - 1)
    achados.add(rand)
    return rand

def gerarIdade():
    return random.randint(0,110)



NUMERO_DE_TESTES = 50 
ERRO_TOLERAVEL = 0.05
TAMANHO_POPULACAO = 10000
tamanho_amostra = achaTamanhoAmostra(ERRO_TOLERAVEL, TAMANHO_POPULACAO)

soma = 0
achados = set()
for i in range(NUMERO_DE_TESTES):
    populacao = []
    amostra = []
    achados = set()
    
    for j in range(TAMANHO_POPULACAO):
        populacao.append(gerarIdade())
    
    while len(amostra) < tamanho_amostra:
        val = populacao[geraIdxAleatorio(TAMANHO_POPULACAO)]
        amostra.append(val)
    
    med_populacao =  stat.mean(populacao)
    med_amostra = stat.mean(amostra)
    dif = (med_amostra / med_populacao - 1) * 100
    soma += abs(dif)
    
    print(f"teste {i+1}\nmedia população: {med_populacao:.2f}\nmedia da amostra: {med_amostra:.2f}\ndiferença das médias: {dif:.2f}%\n")
    
print("---------------------------------------------------")
print(f"diferença média: {soma/NUMERO_DE_TESTES:.2f}%")
