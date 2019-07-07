#!/usr/bin/env python 


class Museum:
    def __init__(self, name: str, city: str, region: str, id: str = None):
        self.name = name
        self.city = city
        self.region = region
        self.id = id
        self.visits = []

    def add_counting(self, year, visits, kind):
        new_counting = Counting(year, visits, kind)

        if new_counting in self.visits:
            raise ValueError("Duplicate counting")

        self.visits.append(new_counting)
        self.visits.sort()


class Counting:
    def __init__(self, year: int, visits: int, kind: str):
        self.year = int(year)
        try:
            self.visits = int(visits)
        except TypeError:
            self._visits = None
        self.kind = kind

    def __eq__(self, other):
        if not isinstance(other, Counting):
            return False

        return (self.year, self.kind) == (other.year, other.kind)

    def __lt__(self, other):
        if not isinstance(other, Counting):
            raise ValueError("Can compare only Counting types")

        return (self.year, self.kind) < (other.year, other.kind)


if __name__ == '__main__':
    pass
