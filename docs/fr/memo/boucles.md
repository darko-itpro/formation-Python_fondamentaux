# Structures de contrôle : les boucles

## Itération avec `for`
### Structure
```python
for element in sequence:
    do_something_with(element)
```

### Usage
```python
camelot = ['arthur', 'Merlin', 'Lancelot']

for name in camelot:
    print(name.upper())
```

### Itération en suivant l'indice d'itération
Itération sur un `enumerate(sequence)`

```python
for index, name in enumerate(camelot):
    print(index, name.upper())
```

### Répéter une action n fois
Itération sur le générateur `range(n)`
```python
for _ in range(3):
    print("Hip", end=' ')
    
print('hourra !')
```

---
## Itération avec while
### Structure
```python
while condition:
    do_something()
```

---
## Interruptions
### Interruption de l'itération
avec `continue` qui interrompt l'itération et passe à l'itération suivante.
Structure :
```python
for element in sequence:
    do_something_always()
    if condition:
        continue
    do_something_if_not_condition()
```

### Interruption de la boucle
avec `break` qui interrompt l'itération et sort de la structure.
Structure :
```python
for element in sequence:
    do_something_always()
    if condition:
        break
    do_something_but_not_in_last_iteration()
```

### Cas de la recherche d'un élément
La clause `if else` permet de réaliser une action si un élement n'est pas trouvé.
```python
for element in sequence:
    if found:
        do_something_for_found(element)
        break
else:
    do_something_if_not_found()
```