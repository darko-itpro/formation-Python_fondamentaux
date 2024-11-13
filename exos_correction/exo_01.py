
duration:int

duration = int(input('Quelle durée (en jours) pour votre formation ? '))

print(duration  * 7)

lunch_break = 72
short_break = 17

total_duration = ((60 * 7) + lunch_break + (2 * short_break) ) * duration

print(total_duration)

print(total_duration // 60, total_duration % 60)

