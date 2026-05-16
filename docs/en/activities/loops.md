# Loops

## Prerequisites
You will need the [pyflix](../pyflix.md) package

## Objectives
In this exercise, we will simulate the behavior of the PyFlix media center.

The `get_season()` function in the `pyflix.datasource` module can take two parameters: the first
is the name of a show, and the second is a user’s name (or ID). The function’s signature is
`get_season(show_name: str = None, user: str = None)`.

We then retrieve the list of episodes. Each episode is a dictionary.

You can retrieve the episodes of The Big Bang Theory as follows:

```python
pyflix.datasource.get_season('The Big Bang Theory', "Sheldon Cooper")
```

First, we want to write a function that takes an entire season as a parameter
and returns the list of episodes left to watch—that is, the portion of the list starting from
the first unwatched episode.

You can retrieve the list of episodes of The Big Bang Theory to create your own datasets.
The return value of this function will serve as “production” data.

## Getting the list of episodes to watch
Write a function `get_playlist_from(season: list) -> list` that returns the list of episodes
you have left to watch. This list starts with the first unwatched episode and goes all the way to 
the end. This function therefore returns a list of episodes, which may be empty if you have no more 
episodes left to watch.

You are encouraged to use tests to, on the one hand, validate your code and, on the other hand, to
help you design the model using a TDD approach. If this process leads you to create
other *intermediate* functions, that is normal. Keep them and use them.

### Stuck?
If you're having trouble answering the question, you can check out the following hints:
The steps in your function should be:
<details>
<summary>Hint 1</summary>
Iterate through the episodes. You can display each episode to verify that you're doing so.
</details>
<details>
<summary>Hint 2</summary>
Identify the episodes you haven’t watched. You can display only those during your
iteration to validate your code.
</details>
<details>
<summary>Hint 3</summary>
Identify the first episode you have left to watch. Then display only that one, or better yet,
write a test that proves you’ve found it. The function then returns this episode.
</details>
<details>
<summary>Hint 4</summary>
Determine the index of this episode
</details>
<details>
<summary>Hint 5</summary>
Use this index to create, using slicing, a new list of episodes that remain to be watched.
</details>

## My Evening…
I have two hours to spare again tonight and I want to watch the episodes I haven’t seen yet. I want
to watch as many full episodes as possible, meaning I need to finish each episode within the
time I have available.

You’ll retrieve all the episodes of a season using the function
`get_season(show_name: str = None, user: str = None)`. Be sure to provide a `name` parameter to
get a list of episodes with watched/unwatched information. Store this collection in a 
variable.

Get the list of episodes I have left to watch using the function from the first part. 
Use a variable named `playlist` to store it.

We will then simulate the operation of a media center. Display the title of the 
next episode by removing it from the playlist. Repeat this for as many episodes as I can watch 
in 2 hours.

Instructions: Start by solving the problem in the simplest way possible. If you write a function, be 
consistent in your choice of parameters.

You can display the lists at the end of the program to verify the processing.

## A bit of an advanced concept…
When you remove an episode from the playlist, set the "watched/unwatched" flag to `True` in the 
reference list.

*Hint*: Remember that in Python, everything is a reference…