episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]


import demos.episodes_utils
print( demos.episodes_utils.is_viewed(episode_viewed) )

from demos import episodes_utils
print(episodes_utils.is_viewed(episode_viewed))

import demos.episodes_utils as eu
print(eu.is_viewed(episode_not_viewed))

from demos.episodes_utils import is_viewed
print(is_viewed(episode_viewed))









