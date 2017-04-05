# -*- coding: utf-8 -*-
from tree.AbstractTree import AbstractTree
from tree.vzorec.NaiveTree import NaiveTree

from time import process_time
import random


def test_adding(tree: AbstractTree, n: int = 10**4, shuffle: bool = True) -> None:
    ran = list(range(n))
    if shuffle:
        random.shuffle(ran)
    for j in ran:
        tree.insert(j)
    tree.insert(-1)
    tree.insert(-1)
    tree.insert(-1)
    for j in range(n):
        assert j in tree
    assert -1 in tree
    for j in range(n):
        tree.remove(j)
    for j in range(n):
        assert j not in tree
    tree.remove(-1)
    assert -1 not in tree


def main() -> None:
    start = process_time()
    test_adding(NaiveTree())
    print("Simple test: {time} s".format(time=(process_time() - start)))


if __name__ == '__main__':
    main()
