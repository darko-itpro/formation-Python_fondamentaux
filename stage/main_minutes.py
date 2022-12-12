import stage.time_utils as tu

user_input = input("Combien de temps en heure ?")

print("Cela fait", tu.to_minutes(user_input), "minutes")