# Les listes

Cet aide mémoire complète celui des [séquences](sequences.md)

De manière générale, l'absence de l'indice lorsqu'utilisé lève une `IndexError`.

La liste de référence pour ces exemples est :
```python
>>> camelot = ['Arthur', 'Merlin', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
```

## Remplacement d'un élément
```python
>>> camelot
['Arthur', 'Merlin', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
>>> camelot[1] = 'Tim'
>>> camelot
['Arthur', 'Tim', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
```

## Suppression d'un élément
```python
>>> camelot
['Arthur', 'Merlin', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
>>> del camelot[1]
>>> camelot
['Arthur', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
```

## Ajout d'un élément
```python
>>> camelot
['Arthur', 'Merlin', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
>>> camelot.append('Bedivere')
>>> camelot
['Arthur', 'Merlin', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc', 'Bedivere']
```

## Insertion d'un élément
```python
>>> camelot
['Arthur', 'Merlin', 'Lancelot', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
>>> camelot.insert(3, 'Bedivere')
>>> camelot
['Arthur', 'Merlin', 'Lancelot', 'Bedivere', 'Robin', 'Bohort', 'Perceval', 'Karradoc']
```


