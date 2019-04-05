#!/usr/bin/env python 

"""
Démonstration de la mise en œuvre des properties
"""


class SayHello:
    """
    Cet objet utilise un objet property déclaré
    """

    def __init__(self):
        self._to_who = "World"

    def set_who(self, who):
        self._to_who = ":) {} (:".format(who)

    def get_who(self):
        return self._to_who if self._to_who is not None else "I have no friends"

    def del_who(self):
        self._to_who = None

    who = property(get_who, set_who, del_who)


class SayDecoratedHello:
    """
    Cet objet utilise les properties avec les décorateurs
    """

    def __init__(self):
        self._to_who = "World"

    @property
    def who(self):
        return self._to_who if self._to_who is not None else "I have no friends"

    @who.setter
    def who(self, who):
        self._to_who = ":) {} (:".format(who)

    @who.deleter
    def who(self):
        self._to_who = None


if __name__ == "__main__":
    sh = SayHello()
    print(sh.who)

    sh.who = "Me"
    print(sh.who)

    del sh.who
    print(sh.who)
