

def heuristica_manhattan(estado):
    distancia = 0
    for i, valor in enumerate(estado):
        if valor == 0:
            continue
        posicao_atual = (i // 3, i % 3)
        posicao_objetivo = ((valor - 1) // 3, (valor - 1) % 3)
        distancia += abs(posicao_atual[0] - posicao_objetivo[0]) + abs(posicao_atual[1] - posicao_objetivo[1])
    return distancia
