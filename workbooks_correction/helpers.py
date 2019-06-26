#!/usr/bin/env python 


def duration_for(how_many: int , unit_duration=7):
    return int(how_many) * int(unit_duration)


def to_minutes(hours: int, minutes=0):
    return int(hours) * 60 + int(minutes)
