import exos.base.episode_utils

episode_viewed = ["The new Project", 1, 98, 2]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

exos.base.episode_utils.is_viewed(episode_viewed)

from exos.base import episode_utils

episode_utils.is_viewed(episode_not_viewed)

import exos.base.episode_utils as eu
eu.is_viewed(episode_not_viewed)

from exos.base.episode_utils import is_viewed
is_viewed(episode_not_viewed)

