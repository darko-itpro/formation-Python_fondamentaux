from pathlib import Path

from demos import settings
import exos.pyflix.mediatheque as md

file_path = settings.ROOT_PATH / 'assets' / 'showslist.csv'

def load_from_csv(file_path:str|Path):
    with open(file_path) as csv_file:
        csv_file.readline()
        for line in csv_file:
            show_name, season, number, title, duration, year = line.strip().split(";")
            yield show_name, title, int(season), int(number), int(duration), int(year)

my_shows = {}

# Un version "simple" peut être :
# for csv_episode_data in load_from_csv(file_path):
#    show_name = csv_episode_data[0]
#    episode_data = csv_episode_data[1:]

for show_name, *episode_data in load_from_csv(file_path):
    try:
        my_show = my_shows[show_name]
    except KeyError:
        my_show = md.TvShow(show_name)
        my_shows[show_name] = my_show

    my_show.add_episode(*episode_data)

for show in my_shows.values():
    print(show.name, len(show.episodes))