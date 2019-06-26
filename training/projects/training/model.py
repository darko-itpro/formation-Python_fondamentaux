#!/usr/bin/env python 


class Attendent:
    def __init__(self, name):
        self._name = name


class Training:
    def __init__(self, subject: str, duration: int):
        """
        Describes a training
        :param subject: Subject of the training
        :param duration: Duration in days
        """

        duration = int(duration)
        if duration < 1:
            raise ValueError("Duration should be at least one (1) day")

        self._subject = subject
        self._duration = int(duration)
        self._attendents = []


    def add_attendent(self, attendent: Attendent):
        self._attendents.append(attendent)

if __name__ == '__main__':
    pass
