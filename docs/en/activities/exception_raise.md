# Raising exceptions

## Quick Reference
An exception is raised by calling the `raise` statement:

```python
raise ValueError("A what went wrong message")
```

You can find the list of exceptions on [the exceptions documentation page](https://docs.python.org/3/library/exceptions.html).

## Exercise
In [the exercise on lists](lists_2.md), you created a function that calculates the duration of a
list of episodes. This function takes the list and the episode durations as parameters.

This duration must be positive. Modify the function so that if a negative or zero duration is 
passed, the function raises a `ValueError`. 
