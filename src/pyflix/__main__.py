import sys

import questionary
from rich.console import Console

import pyflix.settings as conf
import pyflix.load_and_display as runner

def load_default_data():
    global working_shows
    working_shows = runner.load_default_data(working_shows)
    print('Ok, data loaded')

def display_shows():
    runner.display_all_shows(working_shows)


def stop_running():
    global running
    running = False

def _setup():
    global running
    global working_shows

    running = True
    working_shows = {}

def main():

    _setup()

    console = Console()
    console.clear()

    console.rule("Pyflix Management Tool !")

    choices = {
        "Charger les données d'exemple": load_default_data,
        "Charger un fichier ou un répertoire": None,
        "Afficher les données": display_shows,
        "Sortir": stop_running
    }

    runner.local_shows_loader(working_shows)

    while running:
        choice = questionary.select(
            "Quelle action ?",
            choices=choices,
        ).ask()

        choices[choice]()

if __name__ == "__main__":
    main()
