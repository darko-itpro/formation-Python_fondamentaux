import logging

import demos.settings


episode_viewed = ["The new Project", 1, 98, 2]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

episode = episode_viewed
# episode = episode_not_viewed

if episode[3]:
    print("Vu")
else:
    print("Vu")

logging.info("Programme fini")