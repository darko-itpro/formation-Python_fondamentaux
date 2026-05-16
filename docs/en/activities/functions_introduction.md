# Functions, an introduction

## Quick Reference
The structure of a function is

```python
def function_name(param1, param2,):
    value = some_code()
    return value
```

A function takes 0 to n parameters. The return value is optional; if omitted, the function returns
`None` by default.

## Working Files
For the exercises in this assignment, you will use the contents of the following two files:

 * `exos/base/exo_03_01.py`, which you have been working on.
 * `exos/base/exo_03_02.py`, which you have been working on.
 * `exos/base/exo_04.py`, which you will create

After creating the file `exos/base/exo_04.py`, copy the data from `exos/base/exo_03_01.py` into it. Those
are the data using a boolean as viewed or not.

```python
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]
```

## Creating a Function
In the previous exercise, we wanted to test the code with multiple data points. To
make this step easier, we will move the code into a function.

### First Version
Write a function `is_viewed(episode)` that returns whether the episode has been viewed or not. For 
an episode titled "Episode 1", the expected output is:

```sh
Episode 1
This episode has been watched
```

or

```sh
Episode 1
This episode hasn't been watched
```

### Best Practices for Functions
A good function does only one thing (and does it well). Our function does two things: it
determines a value and displays it. This is a bad practice because:

 * if we run the function in a headless environment, we cannot see the
   value (on a server, this output is discarded).
 * if we want to retrieve this value to do something with it… well, we can’t.

It is therefore preferable for a function that calculates a value to simply return that value.
Another component will handle doing something else with it.

### Second version
Modify this function so that it returns `True` or `False` depending on the episode's status.
The overall behavior should remain the same.
