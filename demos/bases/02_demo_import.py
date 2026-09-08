episode_viewed = ["The new Project", 1, 98, True]

from exos.episodes_utils import is_viewed

eu.is_viewed(episode_viewed)





network = get_network()


if network:
    import  webservice as ds
else:
    import localcache as ds

ds.save(data)

