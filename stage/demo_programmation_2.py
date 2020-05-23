"""
Ceci est un script montrant quelque chose de plus complexe.
"""

# L'intéraction avec la fonction input() ne sera pas vue dans la formation
try:
    days = int(input("Combien de jours de formation ? "))
    print(f"Votre formation a une durée de {7 * days} heures")

except ValueError:
    print("Vous auriez dû saisir un nombre")