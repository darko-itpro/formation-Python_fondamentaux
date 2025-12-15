
episode = ["The new Project", 1, 98, 2]

print(episode[0], episode[2])

title, number, duration, viewed = episode
title, _, duration, _ = episode

print(title, duration)

episode[3] = episode[3] + 1
print(episode)
episode[3] += 1
print(episode)