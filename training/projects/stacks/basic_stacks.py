#!/usr/bin/env python 


class Stack:
    def __init__(self, name, *values):
        self.name = name
        self._stack = list(values)

    def enqueue(self, value):
        self._stack.append(value)

    def dequeue(self):
        return self._stack.pop(0)


class MediaStack(Stack):

    def _must_have_duration(self, element):
        if not hasattr(element, 'duration'):
            raise ValueError('Elements should have duration')

    def __init__(self, name, *values):
        for element in values:
            self._must_have_duration(element)
        Stack.__init__(self, name, *values)

    def enqueue(self, value):
        self._must_have_duration(value)

        Stack.enqueue(self, value)


if __name__ == '__main__':
    pass