"""
PSEUDOCÓDIGO DFS

DFS(estado_inicial):
    criar uma pilha vazia
    adicionar estado_inicial na pilha
    criar um conjunto vazio de visitados
    enquanto a pilha não estiver vazia:
        remover o topo da pilha (estado)
        se estado == estado_objetivo:
            retornar sucesso
        se estado não estiver em visitados:
            marcar estado como visitado
            adicionar todos os sucessores na pilha
    retornar falha
"""
from aux_sucessores import get_sucessores

def dfs(estado_inicial, estado_objetivo):
    pilha = [estado_inicial]
    visitados = set()

    while pilha:
        estado = pilha.pop()
        if estado == estado_objetivo:
            return True
        if estado not in visitados:
            visitados.add(estado)
            pilha.extend(get_sucessores(estado))
    return False
