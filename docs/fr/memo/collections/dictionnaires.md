# Les dictionnaires

## Création
```python
my_dict = {}
my_dict = dict()

my_dict = {'key_1': 'value_1', 'key_2': 'value_2'}
my_dict = dict(key_1='value_1', key_2='value_2')
```

Par la suite, le dictionnaire de référence pour ces exemples est :
```python
>>> camelot = {'king': 'Arthur', 'wizard': 'Merlin'}
```

## Taille du dictionnaire
```python
>>> len(camelot)
2
```

## Tester l'existence d'une clef
```python
>>> "king" in camelot
True
>>> "queen" in camelot
False
```

## Accès à un élément
```python
>>> camelot['king']
'Pendragon'
```

L'absence de la clef lève une `KeyError`.

## Remplacement d'un élément
```python
>>> camelot['king'] = 'Pendragon'
>>> camelot
{'king': 'Pendragon', 'wizard': 'Merlin'}
```

L'absence de la clef entraine sa création.

## Ajout d'un élément
```pythion
>>> camelot['knights'] = []
>>> camelot
{'king': 'Arthur', 'wizard': 'Merlin', 'knights': []}
```

## Suppression d'un élément
```python
>>> del camelot['wizard']
>>> camelot
{'king': 'Arthur'}
```

L'absence de la clef lève une `KeyError`.

## Suppression et retour d'un élément
```python
>>> camelot.pop('wizard')
'Merlin'
>>> camelot
{'king': 'Arthur'}
```
