episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]


#import demos.episode_util
#demos.episode_util.is_viewed(episode_viewed)

from demos import episode_util
episode_util.is_viewed(episode_not_viewed)

#import demos.episode_util as eu
#eu.is_viewed(episode_not_viewed)

#from demos.episode_util import is_viewed
#is_viewed(episode_not_viewed)


# network = get_network()
#
# if network:
#     import ws_util as data_util
# else:
#     import cache_util as data_util
#
# data_util.save(data)










