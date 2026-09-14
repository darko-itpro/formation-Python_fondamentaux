daily_duration = 7
training_duration = 5

print(daily_duration)
print(training_duration)

print(daily_duration, training_duration)

# Première possibilité
print(daily_duration * training_duration)


# Seconde possibilité
training_total_duration = daily_duration * training_duration
print(training_total_duration)
del training_total_duration

print("----")

lunch_break = 72

print(lunch_break // 60, lunch_break % 60)

print(divmod(lunch_break, 60))

