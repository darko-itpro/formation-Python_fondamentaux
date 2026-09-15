
episode = ["The new Project", 1, 98, 2]

print(episode[0], episode[2])

title, _, duration, _ = episode

print(title, duration)

print("----")

print(episode[3])
episode[3] = episode[3] + 1
print(episode)
episode[3] = episode[3] + 1
print(episode)


print("-- marche pas --")

title, _, _, viewed = episode
print(viewed, episode[3])
viewed = viewed + 1
print(viewed, episode[3])