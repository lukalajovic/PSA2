# -*- coding: utf-8 -*-

"""Disjoint set"""
from typing import Dict, Callable, Tuple
from typing import TypeVar

T = TypeVar("T")


def disjoint_set(dummy: T) -> Tuple[Callable[[T], None], Callable[[T], T], Callable[[T, T], None]]:
    parent = {}  # type: Dict[T, T]
    rank = {}  # type: Dict[T, int]

    def make_set(a: T) -> None:
        if a in parent:
            return
        parent[a] = a
        rank[a] = 1

    def get_parent(a: T) -> T:
        par = parent[a]
        if par == a:
            return a
        else:
            parent[a] = get_parent(par)
        return parent[a]

    def get_parent_iterative(a: T) -> T:
        par = parent[a]
        fix = [a]
        while par != parent[par]:
            fix.append(par)
            par = parent[par]
        for j in fix:
            parent[j] = par
        return par

    def make_union(a: T, b: T) -> None:
        parA = get_parent(a)
        parB = get_parent(b)
        if parA == parB:
            return
        if rank[parA] < rank[parB]:
            parent[parA] = parB
        elif rank[parA] == rank[parB]:
            parent[parA] = parB
            rank[b] += 1
        else:
            parent[parB] = parA

    return make_set, get_parent, make_union


def main() -> None:
    make_set, get_parent, make_union = disjoint_set(1)

    for j in range(10):
        make_set(j)

    make_union(1, 5)
    make_union(2, 5)
    print(get_parent(2))
    print(get_parent(1))


if __name__ == '__main__':
    main()
