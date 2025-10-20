episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

import exos.base.episode_utils
print( exos.base.episode_utils.is_viewed(episode_viewed) )

from exos.base import episode_utils
print( episode_utils.is_viewed(episode_viewed) )

import exos.base.episode_utils as eu
print( eu.is_viewed(episode_viewed) )

from exos.base.episode_utils import is_viewed
print( is_viewed(episode_viewed) )






network = get_network()

if network:
    import ws_utils as data_util
else:
    import db_utils as data_util

data_util.save(data)









