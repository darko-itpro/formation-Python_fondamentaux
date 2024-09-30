
episode = ["The new Project", 1, 98, 2]

title, _, duration, viewed = episode

print(title, duration)

print(episode)

episode[3] = episode[3] + 1
episode[3] += 1
print(episode)
