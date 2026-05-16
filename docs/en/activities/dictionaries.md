# Dictionaries

So far, we have been working with data where an episode is represented as a 
list. But we have seen that some data may be missing. Imagine that we might have
the production year listed in the fifth position; when the “watched/not watched” information is 
missing, this can be unmanageable:

```python
episode_not_viewed = ["The new Project", 1, 98, 0]
episode_not_viewed = ['Installing the softwares', 2, 42]
episode_not_viewed_with_year = ["The new Project", 1, 98, 0, 2026]
episode_not_viewed_with_year = ['Installing the softwares', 2, 42, 2026]
```
In some cases, such as when reading CSV files or querying databases, data is represented as a list. 
At that time, we still have information about the _columns_. This structure is “impractical” for 
managing the data.

We will work with data structured as dictionaries. The data has been loaded in list form by a parser
that knows the source and will transform it into a dictionary.

The data structure will be as follows:

```python
{"title": "The Conjugal Configuration",
 "duration": 20,
 "viewed": 0}
```

## Working Files
In a real-world scenario, we would be updating the code to replace the contents of
`exos/base/media_utils.py` with a solution using dictionaries. For the purposes of this training,
to preserve the exercises you’ve completed, rename this file to
`exos/base/media_utils_legacy.py`, along with the associated tests. Don’t forget to update the
imports if your IDE doesn’t do this for you.

## Exercises
### Getting Started with Dictionaries
Start by getting familiar with this data. Copy this data into an interactive shell or
a draft script to perform a few actions:

 * Display the title.
 * Change its status (it should become “viewed”) and display the data. Although the “viewed/unviewed” status
is a boolean, anticipate that it could be something else.

### A function for the status
An unviewed episode has the `viewed` key associated with the value `False` or does not have this key.
Try to determine how to handle this situation.

In the `exos/base/media_utils.py` module, write a function `is_viewed(episode: dict)` that takes a
dictionary as a parameter and returns `True` if the episode has been viewed, otherwise `False`. Feel free
to use a *test-first* approach to write this function using the available data.

Here are two examples of data that provide the test cases.

Viewed episodes:

```python
{"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
{"title": "The Conjugal Configuration", "duration": 20, "viewed": 3}
{"title": "The Conjugal Configuration", "duration": 20, "viewed": 3, "year": 2019}
```

Not viewed episodes:

```python
{"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
{"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}
{"title": "The Conjugal Configuration", "duration": 20}
{"title": "The Conjugal Configuration", "duration": 20, "year":2018}
```
