camelot = [("Arthur", "king"), ("Merlin", "wizrd"),
           ("Lancelot", "knight"), ("Robin", "knight"),
           ("Perceval", "knight"), ("Karadoc", "knight")]


for name, job in camelot:
    print(name)
    if job == "wizard":
        print("Cool on a un mage")
        break
else:
    print("You NEED a wiard")