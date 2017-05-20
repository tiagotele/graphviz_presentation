#!/usr/bin/python
# -*- coding: latin-1 -*-
#from graph_tool.all import *
import csv
import os
import copy

#Funções auxiliares
def load_csv(nome_do_arquivo, array_destino):
    with open(nome_do_arquivo, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) == 0: continue
            array_destino.append(r)
    f.close()

def matriz_de_custo_associado(nome_do_arquivo):
    matriz = []
    load_csv(nome_do_arquivo, matriz)
    matriz_copia = copy.copy(matriz)
    for indice_linha in range(len(matriz)):
        custo_acumulado = 0
        for indice_item in range(len(matriz[indice_linha])):
            custo_acumulado += int(matriz[indice_linha][indice_item])
        print ("Custo acumulado" , custo_acumulado)
        matriz_copia[indice_linha].append(custo_acumulado)
    return matriz_copia

os.system('clear')

#def adiciona_numero_do_no_ordenado():

def numeracao_de_nos(matriz_de_custo):
    matriz_numeracao_de_no = []
    linha_numeracao_de_no = []
    for indice_linha in range(len(matriz_de_custo)):
        linha_numeracao_de_no.append(indice_linha)
        for indice_item in range(len(matriz_de_custo[indice_linha])):
            linha_numeracao_de_no.append(matriz_de_custo[indice_linha][len(matriz_de_custo)])
        matriz_numeracao_de_no.append(linha_numeracao_de_no)



#Carrega n nós da rede

#Carrega matriz custo associado com cada nó
#matriz_de_custo = carrega_matriz_de_custo()

#Carrega k conectividade


matriz_de_custo=matriz_de_custo_associado('custo_associado.csv')
print(matriz_de_custo)
