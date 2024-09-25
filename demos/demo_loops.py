#camelot = [("Arthur", "king"), ("Merlin", "wizard"),
#           ("Lancelot", "knight"), ("Robin", "knight"),
#           ("Perceval", "knight"), ("Karadoc", "knight")]


camelot = ["Arthur", "Merlin", "Lancelot", "Robin", "Perceval", "Karadoc"]

for index, knight in enumerate(camelot):
    if index % 2:
        print(knight.upper())
    else:
        print(knight.lower())


for _ in range(4):
    print("turn left")
