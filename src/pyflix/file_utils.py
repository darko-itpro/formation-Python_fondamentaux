import os
from pathlib import Path
import re

def get_media_info(path:str|Path):
    for file_name in get_medias(path):
        yield parse_file_name(file_name)

def parse_file_name(file_name:str): # Usage = parse_file_name("Silicon_Valley-s01e02-The_Cap_Table.avi")
    file_name = os.path.splitext(file_name)[0]

    result = re.search(r'-s(?P<season>\d{2})e(?P<number>\d{2})-', file_name)
    return (file_name[:result.start()].replace('_', ' '),
            file_name[result.end():].replace('_', ' '),
            int(result.group("season")),
            int(result.group("number")))

def get_medias(path:str|Path):
    path = Path(path)
    if not path.is_dir():
        raise ValueError(f"{path} is not a directory")

    for file in os.scandir(path):
        yield file.name


def load_medias_from_csv(path:str|Path, sep:str=";"):
    with open(path, 'r') as file:
        file.readline()
        for line in file:
            show_name, number, season_number, title, duration, year = line.strip().split(sep)
            yield show_name, title, int(season_number), int(number), int(duration), int(year)

if __name__ == '__main__':
    ASSETS_PATH = Path("/Users/dad3zero/Workshop/formations/formation-Python_fondamentaux/assets")
    FILES_PATH = ASSETS_PATH / "files"

    get_medias(FILES_PATH)

    load_medias_from_csv(ASSETS_PATH / "showslist.csv")
