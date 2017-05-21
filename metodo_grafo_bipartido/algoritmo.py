#!/usr/bin/python
# -*- coding: latin-1 -*-
from graph_tool.all import *
import csv
import os
import copy
import operator

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
    for indice_linha in range(1,len(matriz)):
        custo_acumulado = 0
        for indice_item in range(1,len(matriz[indice_linha])):
            custo_acumulado += int(matriz[indice_linha][indice_item])
        matriz_copia[indice_linha].append(custo_acumulado)
    return matriz_copia

def sort_table(table, col=0):
    return sorted(table, key=operator.itemgetter(col))

def ordena_matriz_de_custo_associado(matriz_de_custo_associado):
    return sort_table(matriz_de_custo_associado,len(matriz_de_custo_associado))

def constroi_tabela_de_nos_numerados(matriz):
    matriz_de_nos_numerados = []
    for indice_da_matriz in range(0,len(matriz)-1):
        linha_de_matriz_de_no_numerado = []
        linha_de_matriz_de_no_numerado.append(matriz[indice_da_matriz][0])
        linha_de_matriz_de_no_numerado.append(matriz[indice_da_matriz][len(matriz[indice_da_matriz])-1])
        linha_de_matriz_de_no_numerado.append(indice_da_matriz+1)
        print("linha_de_matriz_de_no_numerado" , linha_de_matriz_de_no_numerado)
        matriz_de_nos_numerados.append(linha_de_matriz_de_no_numerado)
        print("matriz_de_nos_numerados" , matriz_de_nos_numerados)
    return matriz_de_nos_numerados

os.system('clear')

matriz_de_custo = matriz_de_custo_associado('custo_associado.csv')
print ("Matriz de custo")
print(matriz_de_custo)
print ("Matriz de custo ordenada")
matriz_de_custo_ordenada = ordena_matriz_de_custo_associado(matriz_de_custo)
print(matriz_de_custo_ordenada)
print("Tabela de nós numerados")
tabela_de_nos_numerados = []
tabela_de_nos_numerados = constroi_tabela_de_nos_numerados(matriz_de_custo_ordenada)
print(tabela_de_nos_numerados)

print("Construção do grafo bipartido")
#Valor da k conectividade
k = 3
sub1 = tabela_de_nos_numerados[0:k]
sub2 = tabela_de_nos_numerados[k:len(tabela_de_nos_numerados)]

print("Sub1")
print(sub1)
print("Sub2")
print(sub2)
