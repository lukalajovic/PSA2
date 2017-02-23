from typing import List, Tuple, Dict, Iterable


def urnik(predavanja_non_indexed: List[Tuple[int, int]]) -> List[int]:
    if not predavanja_non_indexed:
        return []
    predavanja = [(s, f, i) for i, (s, f) in enumerate(predavanja_non_indexed)]
    predavanja.sort(key=lambda x: x[1])
    _, current_f, i = predavanja[0]
    result = [i]
    for s, f, i in predavanja:
        if s >= current_f:
            current_f = f
            result.append(i)
    return result


def urnik_rec(predavanja: List[Tuple[int, int]]) -> int:
    if len(predavanja) == 0:
        return 0
    if len(predavanja) == 1:
        return 1
    s_1, f_1 = predavanja[0]
    rest = predavanja[1:]
    P_1 = [(s, f) for s, f in rest if f <= s_1]
    P_2 = [(s, f) for s, f in rest if s >= f_1]
    return max(1 + urnik_rec(P_1) + urnik_rec(P_2), urnik_rec(rest))


def vracilo_kovancev(x: int, kovanci: Iterable[int] = (1, 5, 10, 25, 100)) -> Dict[int, int]:
    vracilo = {}
    for k in sorted(kovanci, reverse=True):
        if x < k:  # Don't return 0
            continue
        vracilo[k] = x // k
        x %= k
    return vracilo


def balansiran(niz: str) -> bool:
    op = 0
    for c in niz:
        if c == "(":
            op += 1
        else:
            if not op:
                return False
            op -= 1
    return op == 0

