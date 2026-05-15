# Conditional statements

## Cheat sheet
The basic form of a conditional statement is

```python
if <expr>:
    <code>
```

where :
 * `<expr>` is an expression evaluated to a boolan.
 * `<code>` is a code block

With `else` clause

```python
if <expr>:
    <code>
else:
    <code>
```

With _else if_ clause `elif`:

```python
if <expr>:
    <code>
elif <expr>:
    <code>
else:
    <code>
```

## Working files
For the exercises in this set, you will be working with the following files:

 * `exos/base/exo_03_01.py` which is provided. 
 * `exos/base/exo_03_02.py` which is provided.

---

## First exercise
As in the previous activity, we will work on episodes data.

The source file `exo_03_01.py` contains the declaration of two variables to which
episodes are assigned. The first variable references an episode that has been watched, the other an 
episode that has not.

This code also declares a variable `episode` to which one of the previous variables is assigned,
and a commented-out line where the other is assigned. You will be working with the `episode` 
variable, so to test either behavior, you simply need to comment out one or the other line.

* Write the code that will display ‘the episode has been watched’ if the episode… has been watched 
  and nothing if it has not been watched.
* Complete the code so that it displays “the episode has been watched” if the episode has been 
  watched and “the episode has not been watched” if it hasn’t. The code you write may be
  “self-explanatory”.

---

## Second exercice
The source file `exo_03_02.py` contains similar code, but the information on whether an episode has 
been watched or not is represented by an integer indicating the number of times the episode has been
watched.

Repeat the previous questions for this data representation.
