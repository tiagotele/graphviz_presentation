#!/usr/bin/python
# -*- coding: latin-1 -*-
from graph_tool.all import *
import csv
import os
import copy
import operator

'''
--------------------------
    Funções auxiliares
--------------------------
'''

def carrega_sv(nome_do_arquivo, array_destino):
  with open(nome_do_arquivo, 'r') as f:
    reader = csv.reader(f)
    for r in reader:
      if len(r) == 0:
        continue
      array_destino.append(r)
  f.close()

def carrega_matriz_de_custo_associado(nome_do_arquivo):
  matriz = []
  carrega_sv(nome_do_arquivo, matriz)
  matriz_copia = copy.copy(matriz)
  for indice_linha in range(1, len(matriz)):
    custo_acumulado = 0
    for indice_item in range(1, len(matriz[indice_linha])):
      custo_acumulado += int(matriz[indice_linha][indice_item])
    matriz_copia[indice_linha].append(custo_acumulado)
  return matriz_copia

def ordena_tabela_por_coluna(table, col=0):
  return sorted(table, key=operator.itemgetter(col))

def ordena_matriz_de_custo_associado(matriz_de_custo_associado):
  return ordena_tabela_por_coluna(matriz_de_custo_associado, len(matriz_de_custo_associado))

def constroi_tabela_de_nos_numerados(matriz):
  matriz_de_nos_numerados = []
  for indice_da_matriz in range(0, len(matriz) - 1):
    linha_de_matriz_de_no_numerado = []
    linha_de_matriz_de_no_numerado.append(matriz[indice_da_matriz][0])
    linha_de_matriz_de_no_numerado.append(
        matriz[indice_da_matriz][len(matriz[indice_da_matriz]) - 1])
    linha_de_matriz_de_no_numerado.append(indice_da_matriz + 1)
    matriz_de_nos_numerados.append(linha_de_matriz_de_no_numerado)
  return matriz_de_nos_numerados

def constroi_grafo_bipartido(primeira_parte, segunda_parte, k):

    #Cria grafo com número de vértices
  graph.add_vertex(len(primeira_parte)+len(segunda_parte))

  for indice_primeira_parte in range(len(primeira_parte)):
      for indice_segunda_parte in range(len(segunda_parte)):
          print ("Conectando " , (indice_primeira_parte) , " a " , (indice_segunda_parte) + (k))
          graph.add_edge(indice_primeira_parte,((indice_segunda_parte) + (k)))

#O programa inicia de fato aqui

#Limpa console
os.system('clear')

# Cria instância de objeto do tipo Grafo utilizado no projeto
graph = Graph(directed=False)

#Carrega matriz de custo
matriz_de_custo = carrega_matriz_de_custo_associado('custo_associado.csv')

#Constróio matriz de custo ordenada
matriz_de_custo = ordena_matriz_de_custo_associado(matriz_de_custo)

#Constróio tabelas de nós ordenada por custo acumulado
tabela_de_nos_numerados = []
tabela_de_nos_numerados = constroi_tabela_de_nos_numerados(
    matriz_de_custo)

#Construção do grafo bipartido
# Valor da k conectividade
k = 3

subgraph1 = tabela_de_nos_numerados[0:k]
subgraph2 = tabela_de_nos_numerados[k:len(tabela_de_nos_numerados)]
print ("subgraph1" , subgraph1)
print ("subgraph2" , subgraph2)

constroi_grafo_bipartido(subgraph1,subgraph2,k)

graph.save("grafo_bipartido.dot")

print("Grafo bipartido construído!")
