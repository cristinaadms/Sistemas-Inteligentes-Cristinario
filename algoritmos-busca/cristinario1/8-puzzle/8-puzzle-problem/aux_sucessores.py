
MOVIMENTOS = {
    'cima': -3,
    'baixo': 3,
    'esquerda': -1,
    'direita': 1
}

def get_sucessores(estado):

    sucessores = []
    posicao_zero = estado.index(0)

    for movimento, delta in MOVIMENTOS.items():
        nova_posicao = posicao_zero + delta

        if movimento == 'esquerda' and posicao_zero % 3 == 0:
            continue
        if movimento == 'direita' and posicao_zero % 3 == 2:
            continue
        if movimento == 'cima' and posicao_zero < 3:
            continue
        if movimento == 'baixo' and posicao_zero > 5:
            continue

        novo_estado = list(estado)
        novo_estado[posicao_zero], novo_estado[nova_posicao] = novo_estado[nova_posicao], novo_estado[posicao_zero]
        sucessores.append(tuple(novo_estado))   

    return sucessores
