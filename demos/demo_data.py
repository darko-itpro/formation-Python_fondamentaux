"""
Ce module est uniquement destiné à fournir des données pour les illustrations afin de
tout récupérer par copier/coller plutôt que de tout resaisir.
"""

camelot = ["Arthur", "Merlin", "Lancelot", "Robin", "Perceval", "Karadoc"]
wizards = ["Merlin", "Tim"]

camelot = [("Arthur", "king"), ("Merlin", "wizard"),
           ("Lancelot", "knight"), ("Robin", "knight"),
           ("Perceval", "knight"), ("Karadoc", "knight")]

camelot = {"king":"Arthur", "wizard":"Merlin",
           "knights":["Lancelot", "Robin", "Perceval", "Karadoc"]}

target = [name.upper()
          for name, job in camelot
          if job != "wizard"]