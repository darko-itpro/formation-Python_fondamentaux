#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import datetime


def is_standard_day(sncf_data):
    return True


def is_weekend_day(sncf_data):
    return sncf_data.split(';')[2] != 'JOB'


def is_not_thursday(sncf_data):
    return datetime.datetime.strptime(sncf_data.split(';')[3], '%Y-%m-%d').weekday() != 3

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Comptage max montants")
    parser.add_argument('file_path', help='Chemin vers le fichier de données')
    parser.add_argument('--data_type', choices=['all', 'weekend', 'not_td'] ,help='Type de donnée')
    args = parser.parse_args()

    sncf_file = open(args.file_path, 'r')

    matches_condition = {'all': is_standard_day,
                         'weekend': is_weekend_day,
                         'not_td': is_not_thursday}.get(args.data_type, is_standard_day)

    sncf_file.readline()

    max_value = 0
    data_of_interest = ""

    for element in sncf_file:
        if matches_condition(element):
            value = int(element.split(';')[-1])
            if max_value < value:
                max_value = value
                data_of_interest = element[:-1]

    print(data_of_interest)

    sncf_file.close()
