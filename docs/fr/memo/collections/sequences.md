# Les séquences

Une séquence est une collection d'éléments ordonnés.

 * `str` : chaines de caractères, sont des séquences immuables de chaines d'un seul caractère
 * `list`: listes, sont des séquences d'objets
 *  `tuple`: n-uplets, sont des séquences immuables d'objets

## Création
### Créer une chaine de caractères
```python
my_string = ''
my_string = ""
my_string = str()

king = "Arthur"
```

### Créer une liste
```python
my_list = []
my_list = list()
camelot = ['Arthur', 'Merlin', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
```

### Créer un n-uplet (*tuple*)
```python
my_tuple = tuple() # tuple vide
wizards = 'Merlin',
tavern = 'Perceval', 'Karradoc',
```

---
## Taille
Avec la fonction `len(seq)`
```python
>>> len(king)
6
>>> len(camelot)
7
>>> len(wizards)
1
```

---
## Accès à un élément
Par indexation (*subscript*)
```python
>>> king[2]
't'
>>> camelot[1]
'Merlin'
>>> tavern[0]
'Perceval'
```

```python
>>> king[-1]
'r'
>>> camelot[-2]
'Perceval'
>>> tavern[-1]
'Karradoc'
```

---
## Test élément dans séquence
Avec le mot-clef `in`
```python
>>> 't' in king
True
>>> 'Mordred' in camelot
False
>>> 'Tavernier' in tavern
False
```

---
## Unpacking
Fonctionne avec toute séquence
```python
>>> quest = ['Rabbit of Caerbannog', 'cave', 'Location of the Holly Grail']
>>> opponent_name, location, reward = quest
>>> opponent_name
'Rabbit of Caerbannog'
>>> location
'cave'
>>> reward
'Location of the Holly Grail'
```

---
## Slicing
Structures : `seq[start:stop]` ou `seq[start:stop:step]`
```python
>>> king[2:5]
'thu'
>>> camelot[2:6]
['Lancelot', 'Robin', 'Bohort', 'Perceval']
```

Si `start` et/ou `stop` est omis, le slice ira à l'extrémité.

```python
>>> camelot[:2]
['Arthur', 'Merlin']
>>> camelot[3:]
['Robin', 'Bohort', 'Perceval', 'Karradoc']
>>> camelot[-2:]
['Perceval', 'Karradoc']
>>> camelot[::2]
['Arthur', 'Lancelot', 'Bohort', 'Karradoc']
```
