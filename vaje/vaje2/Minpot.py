def minpot(G):
    pot = list()
    obiskana_vozlisca = set()
    obiskana_vozlisca.add(0)
    pot.append(0)
    origin = 0
    cena = 0
    n = len(G)
    while len(obiskana_vozlisca) < n:
        min_cena = float('inf')
        next_origin = None
        for j,i in enumerate(G[origin]):
            if i < min_cena and j not in obiskana_vozlisca:
                next_origin = j
                min_cena = i
        obiskana_vozlisca.add(next_origin)
        pot.append(next_origin)
        origin = next_origin
        cena += min_cena
    return cena, pot

