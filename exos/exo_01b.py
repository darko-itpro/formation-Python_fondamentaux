
try:
    duration:int = int(input('Quelle durée (en jours) pour votre formation ? '))
    print(7 * duration)
except ValueError:
    print('Veuillez entrer une valeur numérique valide.')
