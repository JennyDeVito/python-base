#!/usr/bin/env python3

"""Exibe relatório de criancas por atividade.

Imprime a lista de criancas agrupadas por sala que frequentam cada uma das
atividades extracurriculares.
"""
__version__ = "0.1.0"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

# dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

#lista que vai funcionar só dentro do programa, lista com as listas e label
atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Danca", aula_danca),
]

#listar alunos em cada atividade por sala 

for nome_atividade, atividade in atividades: 

    print(f"\nAlunos da atividade {nome_atividade}")
    print("-" * 50)
    
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
            
    print("Sala 1: ", atividade_sala1)
    print("Sala 2: ", atividade_sala2)
    print("#" * 50)
