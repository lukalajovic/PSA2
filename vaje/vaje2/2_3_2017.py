# Z = [(cost, size)]
from typing import List, Tuple


def greedy_knapsack(Z: List[Tuple[float, float]], V: float) -> float:
    Z.sort(key=lambda x: x[0] / x[1], reverse=True)
    knapsack = 0  # type: float
    for cost, size in Z:
        if size >= V:
            knapsack += size / V * cost
            break
        else:
            V -= size
            knapsack += cost
    return knapsack


# P = [(cost, time)]
def posli(posli: List[Tuple[int, int]]) -> List[int]:
    P = [list(j) for j in posli]  # Copy
    ma, i_ma = P[0]
    for i, (c, _) in enumerate(P, start=1):
        if c > ma:
            ma = c
            i_ma = i

    taken = [0 for j in range(len(P))]
    taken[i_ma] = 1

    tasks = [i_ma]
    cur_time = 1
    while len(tasks) < len(P):
        ma = 0
        i_ma = -1
        for i, (c, t) in enumerate(P, start=1):
            if c > ma and not taken[i] and t >= cur_time:
                ma = c
                i_ma = i
        cur_time += 1
        if i_ma == -1:
            return tasks
        tasks.append(i_ma)
    return tasks


def predavanja2(P: List[Tuple[int, int]]) -> int:
    predavanja = []  # List[int]
    for s, f in P:
        predavanja.append((f, 0))
        predavanja.append((s, 1))
    predavanja.sort()
    tren = 0
    result = 0
    for t, is_start in predavanja:
        if is_start:
            tren += 1
        else:
            result = max(result, tren)
            tren -= 1
    return result


print(predavanja2([(0, 3), (1, 7), (2, 3), (2, 5), (3, 4), (5, 7)]))


# O(n log(n))
def predavanja3(P: List[Tuple[int, int]]) -> Tuple[int, List[int]]:
    from bisect import bisect_left
    predavanja = [(data, i) for i, data in enumerate(P)]
    predavanja.sort()  # Sort by start
    predavanja_start = [s[0] for s, j in predavanja]
    # Dynamic approach from back
    # Idea: For each class, wea either don't take it and proceed with rest of classes, or take it and proceed with
    # classes that start after the end of taken class
    memo = [(0, -1) for _ in range(len(predavanja) + 1)]
    # Add +1 so we can go over the list and treat is as no more classes
    for i, ((s, f), _) in enumerate(reversed(predavanja)):
        # take it
        next_i = bisect_left(predavanja_start, f)
        take = (f - s) + memo[next_i][0]
        dont_take = memo[-(i + 1)][0]
        if take > dont_take:
            memo[-(i + 2)] = take, next_i
        else:
            memo[-(i + 2)] = dont_take, -1

    # See taken classes
    taken = []  # type: List[int]
    i = 0
    while i < len(predavanja):
        if memo[i][1] > 0:
            taken.append(i)
            i = memo[i][1]
        else:
            i += 1
    return memo[0][0], taken


print(predavanja3([(0, 3), (1, 7), (2, 3), (2, 5), (3, 4), (5, 7)])[0])
print(predavanja3([(1, 17), (2, 3), (3, 15)])[0])


def zapisi(L: List[int], n: int) -> List[List[int]]:
    L.sort()
    T = [[] for _ in range(n)]  # type: List[List[int]]
    i = 0
    for l in L:
        T[i].append(l)
        i = (i + 1) % n
    return T
