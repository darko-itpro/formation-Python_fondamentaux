episode_viewed = ["The new Project", 1, 98, 2]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

import exos.base.media_utils_lists
exos.base.media_utils_lists.is_viewed(episode_viewed)

from exos.base import media_utils_lists
media_utils_lists.is_viewed(episode_not_viewed)

import exos.base.media_utils_lists as mu
mu.is_viewed(episode_not_viewed)

from exos.base.media_utils_lists import is_viewed
is_viewed(episode_viewed)


network = get_network()

if network:
    import ws_utils as datasource
else:
    import local_cache as datasource

datasource.save(data)













