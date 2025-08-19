"""
PSEUDOCÓDIGO GREEDY BEST FIRST

GREEDY(estado_inicial):
    criar fila de prioridade ordenada pela heurística
    adicionar estado_inicial na fila
    criar um conjunto vazio de visitados
    enquanto a fila não estiver vazia:  
        remover estado com menor heuristica (custo) na fila
        se estado == estado_objetivo:
            retornar sucesso
        se estado não estiver em visitados:
            marcar estado como visitado
            adicionar os sucessores com valor da heurística na fila
    retornar falha
"""
from aux_sucessores import get_sucessores
from aux_manhattan import heuristica_manhattan
import heapq

def greedy(estado_inicial, estado_objetivo):
    fila = []
    heapq.heappush(fila, (heuristica_manhattan(estado_inicial), estado_inicial))
    visitados = set()
    while fila:
        _, estado = heapq.heappop(fila)
        if estado == estado_objetivo:
            return True
        if estado not in visitados:
            visitados.add(estado)
            for sucessor in get_sucessores(estado):
                heapq.heappush(fila, (heuristica_manhattan(sucessor), sucessor))
    return False
