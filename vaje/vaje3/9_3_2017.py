# -*- coding: utf-8 -*-
from typing import List
from typing import Optional
from typing import Tuple

from disjoint_set import disjoint_set
from kopica import BinaryHeap

Graph = List[List[Tuple[int, float]]]
Edges = List[Tuple[int, int, float]]


def kruskall(G: Graph) -> Edges:
    make_set, get_parent, make_union = disjoint_set(dummy=0)
    for j in range(len(G)):
        make_set(j)

    edges = []  # type: List[Tuple[float, int, int]]
    for j in range(len(G)):
        for end, cost in G[j]:
            if end > j:  # Add just one edge
                edges.append((cost, j, end))

    rtr = []  # type: Edges

    for cost, start, end in sorted(edges):
        if get_parent(start) != get_parent(end):
            rtr.append((start, end, cost))
            make_union(start, end)

    return rtr


def prim(G: Graph) -> Edges:
    parent = [None for _ in range(len(G))]  # type: List[Optional[int]]

    heap = BinaryHeap({j: float("inf") for j in range(len(G))})

    # Select one
    heap[0] = 0

    mst = []  # type: Edges

    while len(heap):
        u, cur_cost = heap.pop()  # type: Tuple[int, float]
        par = parent[u]
        if par is not None:  # do not take first edge
            mst.append((par, u, cur_cost))
        for v, cost in G[u]:
            if v in heap and cost < heap[v]:
                parent[v] = u
                heap[v] = cost

    return mst


def main() -> None:
    G1 = [
        [(1, 7), (3, 5)],
        [(0, 7), (2, 8), (3, 9), (4, 7)],
        [(1, 8), (4, 5)],
        [(0, 5), (1, 9), (4, 15), (5, 6)],
        [(1, 7), (2, 5), (5, 8), (6, 9)],
        [(3, 6), (4, 8), (6, 11)],
        [(5, 11), (4, 9)]
    ]  # type: Graph

    print(kruskall(G1))
    print(prim(G1))

    G2 = [
        [(1, 10), (2, 6), (3, 5)],
        [(0, 10), (3, 15)],
        [(0, 6), (3, 4)],
        [(0, 5), (1, 15), (2, 4)]
    ]  # type: Graph

    print(kruskall(G2))
    print(prim(G2))


if __name__ == '__main__':
    main()
