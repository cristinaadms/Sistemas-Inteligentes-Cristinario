"""
PSEUDOCÓDIGO BFS

BFS(estado_inicial):
    criar uma fila vazia
    enfileirar(estado_inicial) na fila
    criar um conjunto vazio de visitados
    enquanto a fila não estiver vazia:  
        remover o primeiro elemento da fila
        se estado == estado_objetivo:
            retornar sucesso
        se estado não estiver em visitados:
            marcar estado como visitado
            adicionar todos os sucessores na fila
    retornar falha
"""

from collections import deque
from aux_sucessores import get_sucessores 

def bfs(estado_inicial, estado_objetivo):
    fila = deque([estado_inicial])
    visitados = set()

    while fila:
        estado = fila.popleft()
        if estado == estado_objetivo:
            return True
        if estado not in visitados:
            visitados.add(estado)
            fila.extend(get_sucessores(estado))
    return False
    
