#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Manipulation intéractive
    ^^^^^^^^^^^^^^^^^^^^^^^^

    #. Demander le nom et l’âge puis affichez-les ( exemple : Yoda a 800 ans )

    #. Il me reste 3 épisodes de 53 minutes de Dardevil à regarder. Combien de
    temps (en heure/minutes) cela représente-t-il ? Sachant qu'il est 20h42 et
    en supposant que je les regarde à la suite, à quelle heure irai-je me
    coucher ?
"""

if __name__ == '__main__':
    name = str(input("Votre nom ? "))
    age = int(input("Votre age ? "))
    print("Vous vous appelez {} et vous avez {} ans"
          .format(name, age))

    print("J'en ai pour {}h{}".format((3 * 53) // 60, (3 * 53) % 60))

    # La fonction divmod permet de récupérer les deux valeurs :
    hour, minutes = divmod(3 * 53, 60)
    print("J'en ai pour {}h{} (divmod)".format(hour, minutes))

    hour, minutes = divmod(42 + (3 * 53), 60)
    print("Je serai au lit à {}h{}".format(20 + hour, minutes))
