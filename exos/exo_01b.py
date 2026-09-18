
try:
    duration:int = int(input('Quelle durée (en jours) pour votre formation ? '))
    print(duration * 7)
except ValueError:
    print(f"Saisissez un nombre entier de manière numérique (exemple : 10, 20")

