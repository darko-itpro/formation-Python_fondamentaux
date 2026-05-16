
episode = ["The new Project", 1, 98, 2]

print(episode[0], episode[2])

title, _, duration, _ = episode

print(title, duration)

print(episode[3])
episode[3] = episode[3] + 1
episode[3] += 1
print(episode[3])
