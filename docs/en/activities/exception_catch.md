# Exception Handling

## Quick Reference
To catch an exception, use the following structure:

```python
try:
    ...
except ValueError:
    do_something_for_exception()
```

Here, the code knows how to handle a `ValueError`.

The `finally` clause allows code to be executed in all cases.

```python
try:
    ...
except ValueError:
    do_something_for_exception()
finally:
    cleanup()
```

## Working Files
For the exercises in this assignment, you will return to one of the initial files:

 * `exos/base/exo_01b.py`, which is provided to you.

## Exercise
To practice exception handling, we will simply modify the code for this exercise.

Go back to the code in the `exo_01b.py` script.

Handle the exception when the user enters a string that cannot be converted 
to an integer, and inform them that they entered incorrect data.
