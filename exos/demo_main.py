episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

#import exos.episode_utils
#print(exos.episode_utils.is_viewed(episode_viewed))

#from exos import episode_utils
#print(episode_utils.is_viewed(episode_viewed))

import exos.episode_utils as eu
print(eu.is_viewed(episode_viewed))

#from exos.episode_utils import is_viewed
#print(is_viewed(episode_viewed))


