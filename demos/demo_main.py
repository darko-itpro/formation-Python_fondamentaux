episode_viewed = ["The new Project", 1, 98, 2]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

import demos.episodes_utils
print(demos.episodes_utils.is_viewed(episode_viewed))

from demos import episodes_utils
episodes_utils.is_viewed(episode_not_viewed)

import demos.episodes_utils as eu
eu.is_viewed(episode_viewed)

from demos.episodes_utils import is_viewed
is_viewed(episode_viewed)



network = get_network()

if network:
    import ws_utils as service
else:
    import local_cache as service

service.save(data)










