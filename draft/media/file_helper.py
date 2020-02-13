def load_from_csv(path):
    with open(path) as shows_file:
        shows_file.readline()

        for line in shows_file:
            try:
                show, season, episode, title, duration, year = line.split(';')
            except ValueError:
                yield None

            yield show, int(season), int(episode), title, int(duration), int(year)


for infos in load_from_csv("/Users/dad3zero/Workshop/Trainings/training-python/assets/showslist_bad.csv"):
    print(infos)