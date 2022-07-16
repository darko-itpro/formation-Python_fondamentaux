from pathlib import Path
import re


def load_from_filenames(dir_path):
    """
    Creates an iterator to return filename data
    """
    pattern = "-s(?P<season>[0-9]{2})e(?P<episode>[0-9]{2})-"
    p = Path(dir_path)
    for media_file in p.iterdir():
        episode_name = media_file.stem
        result = re.search(pattern, episode_name)

        if result:
            yield episode_name[:result.start()].replace("_", " "), \
                  result.group("season"), result.group("episode"), \
                  episode_name[result.end():].replace("_", " ")

def load_from_csv(file_path):
    """
    Creates an iterator to return show csv file data.
    """
    with open(file_path) as csv_file:
        csv_file.readline()

        for episode in csv_file:
            yield tuple(episode.split(";"))
