import os
from pathlib import Path

def get_medias(path:str|Path):
    path = Path(path)
    if not path.is_dir():
        raise ValueError(f"{path} is not a directory")

    for file in os.scandir(path):
        print(file.name)


def load_medias_from_csv(path:str|Path, sep:str=";"):
    with open(path, 'r') as file:
        file.readline()
        for line in file:
            show_name, number, season_number, title, duration, year = line.strip().split(sep)
            print(show_name, title, int(season_number), int(number), int(duration), int(year))

if __name__ == '__main__':
    ASSETS_PATH = Path("/Users/dad3zero/Workshop/formations/formation-Python_fondamentaux/assets")
    FILES_PATH = ASSETS_PATH / "files"

    get_medias(FILES_PATH)

    load_medias_from_csv(ASSETS_PATH / "showslist.csv")
