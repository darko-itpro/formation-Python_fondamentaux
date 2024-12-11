episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]


import demos.episodes_utils_lists
print(demos.episodes_utils_lists.is_viewed(episode_viewed))

from demos import episodes_utils_lists
print(episodes_utils.is_viewed(""))

import demos.episodes_utils_lists as eu
print(eu.is_viewed(episode_not_viewed))

from demos.episodes_utils_lists import is_viewed
print(is_viewed(episode_viewed))









