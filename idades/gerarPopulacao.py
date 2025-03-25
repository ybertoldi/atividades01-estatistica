import random
import csv

def gerar_idade():
    return random.randint(0,110)

idades = []
while len(idades) < 10000:
    idades.append(gerar_idade())


with open(r"exercicios\idades\idades.csv" , "w", newline= '') as f:
    write = csv.writer(f)
    for idade in idades:
        write.writerow([idade])