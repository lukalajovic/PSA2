# -*- coding: utf-8 -*-
from tree.AbstractTree import AbstractTree
from tree.vzorec.NaiveTree import NaiveTree

from time import process_time
import random


def test_adding(tree: AbstractTree, n: int = 10 ** 4) -> None:
    for j in range(n):
        tree.insert(j)
    for j in range(n):
        assert j in tree
    for j in range(n):
        tree.remove(j)


def main() -> None:
    start = process_time()
    test_adding(NaiveTree())
    print("Simple test: {time} s".format(time=(process_time() - start)))


if __name__ == '__main__':
    main()
