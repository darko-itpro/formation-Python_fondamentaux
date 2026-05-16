# Conditional statements, part 2

The two exercises are independent.

## Working files
For the exercises in this statement, you will be working with the following files:

 * `exos/base/media_utils.py`, which you created earlier (it is possible that during the training
   a different name may have been chosen).

## Exercise
After going live, we discovered that there could be two data structures for an unwatched episode:

```python
episode_not_viewed = ["The new Project", 1, 98, 0]
episode_not_viewed = ['Installing the softwares', 2, 42]
```

The first structure contains an integer representing the number of views in the fourth position, 
whilst the second has only 3 values.

If you use this second piece of data with your `is_viewed(episode:list)` function, it will raise
an exception.

Update the function so that an episode lacking the ‘viewed’ information (and therefore having only 3
data points) is treated as "unviewed".

You are encouraged to use the tests. You will therefore only need to add one test with this
new data.
