#!/usr/bin/env python3

"""Exibe relatório de criancas por atividade.

Imprime a lista de criancas agrupadas por sala que frequentam cada uma das
atividades extracurriculares.
"""
__version__ = "0.1.2"
__author__ = "Jenny DeVito"
__license__ = "Unlicense"

# dados

sala = {
    1 : ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    2 : ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aula = {
    "Inglês" : ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica" : ["Erik", "Carlos", "Maria"],
    "Danca" : ["Gustavo", "Sofia", "Joana", "Antonio"]
}

#dict que vai funcionar só dentro do programa, dict com as listas e label

atividades = {
    "Inglês" : aula["Inglês"],
    "Musica" : aula["Musica"],
    "Danca" : aula["Danca"]
}

#listar alunos em cada atividade por sala iterando as keys e os values pelos 
#itens da dict 

for key, value in atividades.items(): 

    print(f"\nAlunos da atividade {key}")
    print("-" * 50)

    #sala que tem interseccão com a atividade a mantem criacao do set
    #não tem porque mexer nessa parte da logica
    atividade_sala1 = set(sala[1]) & set(value)
    atividade_sala2 = set(sala[2]) & set(value)
    
    print("Sala 1: ", atividade_sala1)
    print("Sala 2: ", atividade_sala2)
    print("#" * 50)
