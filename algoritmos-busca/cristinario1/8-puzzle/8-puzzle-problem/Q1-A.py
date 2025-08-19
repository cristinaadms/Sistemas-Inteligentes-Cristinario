"""
PSEUDOCÓDIGO A*

A*(estado_inicial):
    criar fila de prioridade ordenada por f(n) = g(n) + h(n)
    g(n) é o custo do caminho até o estado atual
    h(n) é a heurística do estado atual (distânica de manhattan)
    adicionar estado_inicial na fila
    criar um conjunto vazio de visitados
    enquanto a fila não estiver vazia:  
        remover estado com menor f(n) na fila
        se estado == estado_objetivo:
            retornar sucesso
        se estado não estiver em visitados:
            marcar estado como visitado
            para cada sucessor:
                calcular g(novo) = g(estado) + 1
                calcular f(novo) = g(novo) + h(novo)
                adicionar sucessor na fila
    retornar falha
        
"""

from aux_sucessores import get_sucessores
from aux_manhattan import heuristica_manhattan
import heapq

def a_star(estado_inicial, estado_objetivo):
    fila = []
    heapq.heappush(fila, (heuristica_manhattan(estado_inicial), 0, estado_inicial))
    visitados = set()
    while fila:
        f, g, estado = heapq.heappop(fila)
        if estado == estado_objetivo:
            return True
        if estado not in visitados:
            visitados.add(estado)
            for sucessor in get_sucessores(estado):
                g_novo = g + 1
                f_novo = g_novo + heuristica_manhattan(sucessor)
                heapq.heappush(fila, (f_novo, g_novo, sucessor))
    return False
