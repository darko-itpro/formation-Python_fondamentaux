
try:
    duration: int = int(input('Quelle durée (en jours) pour votre formation ? '))

    print(duration * 7)
except ValueError:
    print("Veuillez entrer une durée valide en jours.")
