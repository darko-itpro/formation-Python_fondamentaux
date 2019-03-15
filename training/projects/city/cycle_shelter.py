#!/usr/bin/env python 

class CycleStation:
    def __init__(self, identifier, name, capacity):
        self.identifier = identifier
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return "{} {}".format(self.name, self.capacity)

    def __repr__(self):
        return self.__str__()


def velib_station_processor(data):
    station = CycleStation(data[0], data[1], data[2])
    return station


def file_loader(path: str, processor=None):
    with open(path) as data_file:
        data_file.readline()

        data = []

        for line in data_file:
            if processor:
                data.append(processor(line.split(';')))
            else:
                data.append(line.split(";"))

        return data
