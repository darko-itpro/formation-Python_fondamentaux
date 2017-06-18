#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class SayHello:

    def __init__(self):
        self._to_who = "World"

    def set_who(self, who):
        self._to_who = who

    def get_who(self):
        return self._to_who if self._to_who else "I have no friends"

    def del_who(self):
        self._to_who = None

    who = property(get_who, set_who, del_who)

if __name__ == "__main__":
    sh = SayHello()
    print(sh.who)

    sh.who = "Me"
    print(sh.who)

    del sh.who
    print(sh.who)
