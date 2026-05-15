# Lists

## Working Files
For the exercises in this assignment, you will be working with the following files:

 * `exos/base/exo_02.py`, which is provided to you.

## Background
For a video streaming service project, PyFlix (similar to Netflix but written in Python), we
need to explore data management to represent an episode of a series.

We will represent an episode of Stranger Code (an exclusive series) as follows:

```python
["The new Project", 1, 98, 0]
```

An episode is represented by a list where:

 * The first element is the title
 * The second is the episode number
 * The third is the duration
 * The fourth is a counter representing the number of times the episode has been viewed.

This value is declared and assigned to a variable in the `exo_02.py` file.

---

## Exercise
 * Display the episode title.
 * Display its duration.

See if you can write “readable” code.

Finally:

 * Display the number of times the episode has been viewed
 * Increment this value by 1
 * Display the number of times the episode has been viewed
 * Increment it again several times using the same statement.
