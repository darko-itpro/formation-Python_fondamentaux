# Lists, second part

## Before You Begin
For this exercise (and some of the following exercises), you will need an 
additional resource: the [pyflix](../pyflix.md) package

## Overview
We are going to launch a video streaming service, PyFlix, similar to Netflix but written in Python. 
We will therefore be managing a catalog.

The `pyflix.datasource` module contains a function named `get_season()` that returns the list of
episode titles for season 12 of "The Big Bang Theory". We’re going to extract information from
this list.

The easiest way to use this function is as follow:

```python
import pyflix.datasource as ds

ds.get_season()
```

To use this function, you can consult 
[the dedicated page on the wiki](https://github.com/darko-itpro/pyschool-lib/wiki/Le-module-pyflix.datasource)

### Create a reference to the data
Assign the return value of this function to a variable named `bbt_s12`. This is the reference
to the season loaded into memory in your module.

We will use this variable for the following questions (you should not call the
function again to avoid overloading the server). The following questions are independent of one another.

### Tip: Displaying collections
To display the collection, you’ll see that the `print()` function isn’t suitable. It displays
the list’s contents on a single line, which isn’t *practical* for viewing its contents.
To view the list’s contents, I suggest using the
`pprint()` function from the `pprint` module:

```python
from pprint import pprint

pprint(bbt_s12)
```

This function has a name that won’t conflict with the `print()` function, so you can
import it directly.

### Calculate the season’s duration

Assuming each episode lasts 23 minutes, how long is the season?

To do this, write a function that takes (at least) a list of episodes as an argument and returns
the duration of that list of episodes.

### Manage your evening playlist
We want to obtain a list of the first episodes whose total duration is less than or equal to a 
given duration.

To do this, you must create a function with (at least) a list of episodes
(ep_list) and the maximum duration (max_duration). This function must return the list of the first N
episodes from `ep_list`, where `N` is the maximum number of episodes to watch. N is a maximum.

**Note**: `ep_list` and `max_duration` are used here to reference the data; you can use more 
appropriate names as parameters.

Use this function with `bbt_s12` as the argument and a duration of 2 hours.

### The User Playlist
Users want to track their progress through a series, so we'll handle this using a *playlist* that 
is a copy of the season. The next episode to watch is the first one in the playlist. Once it's been 
watched, it's removed from the playlist.

Create  a copy of the Season 12 list (`bbt_s12`) in a variable `playlist` (it doesn’t matter
if the name was already used for the previous list).

To simulate watching an episode (the first one in the playlist), simply display its title. At the
same time, remove it from the playlist. You can, of course, use a function for this, a function 
that takes a list of episodes as an argument.

The playlist contains only the episodes left to watch (currently one fewer than the complete 
series). Use the function that calculates the duration to display the duration of the remaining 
episodes and the complete season to compare the two values.

What do you notice?
