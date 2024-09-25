camelot = [("Arthur", "king"), ("Merlin", "wizard"),
           ("Lancelot", "knight"), ("Robin", "knight"),
           ("Perceval", "knight"), ("Karadoc", "knight")]


for name, job in camelot:
    if job == "wizard":
        print("You HAVE a wizard:", name)
        break
else:
    print("You NEED a wizard !!!")