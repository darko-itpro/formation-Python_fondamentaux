"""
Ceci est un script montrant quelque chose de plus complexe.
"""
ma_formation_ref = 0
budget = 2300

trainings = [
    {"name": "Python, Programmation Objet",
     "duration": 5,
     "max seats": 12,
     "price": 2500},
    {"name": "Django",
     "duration": 4,
     "max seats": 12,
     "price": 2000}
]

ma_formation = trainings[ma_formation_ref]

print(f"Vous avez une formation {ma_formation['name']} de {ma_formation['duration']} jours")

if ma_formation['price'] <= budget:
    print("Ok vous êtes inscrit")
else:
    print("Désolé, pas le budget")
