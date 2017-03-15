# -*- coding: utf-8 -*-
from collections import Counter
from typing import Dict, Iterable
from typing import List, TypeVar
from typing import Optional
from typing import Tuple

from disjoint_set import disjoint_set
from kopica import BinaryHeap

import heapq

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


T = TypeVar("T")


def Huffman(items: Iterable[Tuple[T, float]]) -> List[Tuple[T, str]]:
    class Node:
        def __init__(self, freq: float, value: Optional[T], left: Optional["Node"] = None,
                     right: Optional["Node"] = None) -> None:
            self.freq = freq
            self.value = value
            self.left = left
            self.right = right

        def __lt__(self, other: "Node") -> bool:
            return self.freq < other.freq

        def __repr__(self) -> str:
            return "Node(freq={freq}, value='{value}', left={left}, right={right})". \
                format(freq=self.freq, value=str(self.value) if self.value else "", left=str(self.left),
                       right=str(self.right))

    heap = [Node(freq, item) for item, freq in items]
    heapq.heapify(heap)

    while len(heap) > 1:
        fst = heapq.heappop(heap)
        snd = heapq.heappop(heap)

        new = Node(fst.freq + snd.freq, None, fst, snd)
        heapq.heappush(heap, new)

    codes = []  # type: List[Tuple[T, str]]

    def get_codes(root: Node, prefix: str = "") -> None:
        if root.value is not None:  # Leaf
            codes.append((root.value, prefix))
        else:
            assert root.left is not None
            assert root.right is not None
            get_codes(root.left, prefix + "0")
            get_codes(root.right, prefix + "1")

    get_codes(heap[0])

    codes.sort(key=lambda x: (len(x[1]), x[0]))

    return codes


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

    data = [("a", 5), ("b", 9), ("c", 12), ("d", 13), ("e", 16), ("f", 45)]  # type: List[Tuple[str, float]]

    print(Huffman(data))

    wiki_text = "this is an example of a huffman tree"
    counter = {}  # type: Dict[str, float]

    for c in wiki_text:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    wiki_huff = Huffman(counter.items())
    print(wiki_huff)
    wiki_dict = dict(wiki_huff)
    print(sum(len(wiki_dict[c]) for c in wiki_text))


if __name__ == '__main__':
    main()
