from exos_correction.base import episode_utils as eu

episode_not_viewed = ['Installing the softwares', 2, 42, 0]

print(eu.is_viewed(episode_not_viewed))
