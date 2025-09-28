import logging
import sys

import questionary

import demos.settings as conf
import demos.pyflix.load_and_display as runner

print("Gestion de mediathèque")

working_shows = {}

if not conf.DATA_PATH.exists():
    create_data_folder = (questionary.confirm("Le répertoire de données n'existe pas, le créer ?")
                          .ask())

    if create_data_folder:
        conf.DATA_PATH.mkdir()
        print(f"Ok, répertoire {conf.DATA_PATH} créé.")
    else:
        print("Impossible de faire fonctionner ce programme sans ce répertoire.")
        print("Vous pouvez modifier le répertoire dans le fichier demos.settings.")
        sys.exit(0)


def load_default_data():
    global working_shows
    working_shows = runner.load_default_data(working_shows)
    print('Ok, data loaded')

def display_shows():
    runner.display_all_shows(working_shows)

def stop_running():
    global running
    running = False

choices = {
    "Charger les données d'exemple": load_default_data,
    "Charger un fichier ou un répertoire": None,
    "Afficher les données": display_shows,
    "Sortir": stop_running
}

running = True

while running:

    choice = questionary.select(
        "Quelle action ?",
        choices=choices,
    ).ask()

    choices[choice]()

print("By")
