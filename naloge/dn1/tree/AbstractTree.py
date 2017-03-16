# -*- coding: utf-8 -*-
from typing import Generic, Iterable, TypeVar, Optional

T = TypeVar("T")


class AbstractTree(Generic[T]):
    def __init__(self, data: Optional[Iterable[T]] = None) -> None:
        pass

    def insert(self, item: T) -> None:
        """
        Vstavi element item v iskalno drevo, če ta element že obstaja ga prepišemo z novim
        :param item: Element, ki ga vstavljamo v drevo
        :return: None
        """
        raise NotImplementedError("Not implemented")

    def remove(self, item: T) -> None:
        """
        Odstrani element item iz iskalnega drevesa, če ga ni naj metoda sproži ValueError
        :param item: Element, ki ga brišemo iz drevesa
        :return: None
        """
        raise NotImplementedError("Not implemented")

    def search(self, item: T) -> bool:
        """
        Vrne True, če se item nahaja v drevesu in False, če se ne.
        :param item: Element, ki ga v drevesu iščemo
        :return: True če se item nahaja v drevesu, drugače False.
        """
        raise NotImplementedError("Not implemented")

    def __contains__(self, item: T) -> bool:
        return self.search(item)
