#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

f = open("../../../assets/SNCF/comptage-voyageurs-trains-transilien.csv", 'r')
time_count_matcher = re.compile("Entre ([0-9]*)h et ([0-9]*)h")


def is_afternoon(start_time, end_time):
    return start_time < 13 and end_time > 13 or start_time < 19 and end_time > 13


def is_morning(start_time, end_time):
    return start_time < 8 and end_time > 8 or start_time < 12 and end_time > 8


def get_start_end_time(record, condition):
    res = time_count_matcher.search(record)
    if res:
        start_time = int(res.group(1))
        end_time = int(res.group(2))
        return condition(start_time, end_time)

print(len([line for line in f if get_start_end_time(line, is_afternoon)]))
f.seek(0)
print(len([line for line in f if get_start_end_time(line, is_morning)]))

f.close()
