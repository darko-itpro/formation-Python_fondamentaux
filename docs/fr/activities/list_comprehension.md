# List Comprehension

## Aide mémoire
Une list comprehension permet de créer une liste par transformation d’une liste, par filtre d’une 
autre liste ou les deux.
La structure d’une transformation est :
```
[transformation for element in sequence]
```

Ce qui peut nous donner quelque chose du type :
```py
[len(element) for element in sequence]
```

La structure d’un filtre est:
```
[transformation for element in sequence if condition]
```

Ce qui peut nous donner quelque chose du type :
```py
[len(element) for element in sequence if len(element) > 10]
```

## Outils
Le module `pyflix.datasource`contient une fonction `get_movies()` qui retourne la liste des films 
Harry Potter. Chaque film est représenté par une liste contenant 3 valeurs :

 * le titre
 * la durée
 * si je l’ai vu ou non.

## Exercices
 1. Grâce aux list comprehension, **créez une liste des titres**. Vous devez donc transformer la liste de 
listes en liste de chaines de caractères. 
 2. Ajoutez par la suite la condition suivante : **la liste ne doit contenir que les films qui me restent 
à voir**. 
 3. Il existe en Python une fonction `sum()` qui prend en paramètres une séquence d’entiers et en 
retourne la somme. Calculez donc la durée d’un marathon Harry Potter et un marathon des films qui 
me reste à voir.