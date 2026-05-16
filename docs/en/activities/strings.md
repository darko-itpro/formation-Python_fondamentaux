# Formatting Strings

## Quick Reference
Any data we’re going to work with must be *formatted* in order to be displayed to the user.
This can be done using the `format()` method for strings:

```python
pref_string = "My favorite language is {}"
print(pref_string.format(name))
```
Curly braces are used to format the data to be displayed. Since the micro-language is quite 
complex, I encourage you to consult  
[the documentation](https://docs.python.org/3.14/library/string.html#format-string-syntax) for a 
comprehensive overview of its features.

Here are the most common ones:

* **{1}** displays the second item in the data list.
* **{:.2f}** displays the data as a floating-point number with two decimal places
* **{:10}** reserves 10 spaces to display the data
* **{:10.2f}** reserves 10 spaces to display a floating-point number with two decimal places
* **{1:10.2f}** reserves 10 spaces to display the second element of the data list as a 
  floating-point number with two decimal places

Python also supports *f-strings*, which have the following syntax:

```python
print(f"My favorite language is {name}")
```

The formatting features of the `.format()` method also apply to f-strings.

## First Exercise
A quick speed calculation. I traveled **19.7 meters** in **6.892 seconds**. Display the 
speed with its unit, rounding to two decimal places.

---
## Second Exercise
You will need the [pyflix](../pyflix.md) package

I want to determine what time I’ll go to bed after watching a few episodes of my 
series.

I’ll watch 7 consecutive 23-minute episodes.

The start of my evening is obtained using the `pyflix.datasource.get_start_time()` function.

Display the bedtime in the format `"I’ll go to bed at 22:04"`.
