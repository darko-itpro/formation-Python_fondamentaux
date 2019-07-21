#!/usr/bin/env python 

from training.projects.museums import file_parsers as file
from training.projects.museums import museum_model as model

if __name__ == '__main__':
    museums = []

    for id, data in file.load_as_dicts().items():
        museum = model.Museum(data['museum_name'], data['city'],
                              data['region'], id)

        for counting in data['visits']:
            try:
                museum.add_counting(*counting)
            except ValueError as e:
                if "invalid literal" not in e.args[0]:
                    print("Error for value ", counting, "in", museum.name)

        museums.append(museum)

    print("-------------------")
    print(" Musées par région")
    print("-------------------")
    only_regions = [museum.region for museum in museums]
    for region in sorted(set(only_regions)):
        print(" - {} ({:3})".format(region, only_regions.count(region)))
