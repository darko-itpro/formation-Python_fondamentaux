import re
import os
import os.path

def load_from_filenames(path):

    pattern = r"-s(?P<season>[0-9]?)e(?P<episode>[0-9]2)-"

    for item in os.scandir(path):
        file_name = os.path.splitext(item.name)[0]
        found = re.search(pattern, file_name)
        if found:
            number = int(found.group("episode"))
            season = int(found.group("season"))
            show = file_name[:found.start()].replace("_", " ")
            title = file_name[:found.start()].replace("_", " ")

            yield show, season, number, title


def load_from_csv(path):
    with open(path, encoding="utf-8") as episodes_file:
        episodes_file.readline()

        for episode in episodes_file:
            yield tuple(episode.split(";"))
