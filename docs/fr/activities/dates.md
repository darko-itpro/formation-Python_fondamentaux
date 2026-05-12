# Gestion des dates

## Rappel pour le formatage de dates

Pour [le code formatage, consultez la documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

Vous pouvez utiliser ces codes de formatage dans les templates pour la méthode `str.format()` et 
avec les *f-strings*.

```python
from datetime import datetime
now = datetime.now()

print("We are {:%A %B the %d}".format(now))
print(f"We are {now:%A %B the %d}")
```

## Exercice 1

Nous allons reprendre l'exercice sur le formatage des chaines de caractères mais en utilisant les
objets `datetime` et `timedelta`.

Je veux déterminer à quelle heure j'irai me coucher après avoir regardé quelques épisodes de ma 
série.

**Ce soir**, je regarderai à la suite **7** épisodes de **23 minutes**.

Le début de ma soirée est obtenu par la fonction `pyflix.datasource.get_start_time()`.

Affichez l'heure de coucher sous la forme `"J'irai me coucher à 22h04"`

<details>
<summary>Comment créer l'heure de début ?</summary>
Vous pouvez créer un objet `datetime` avec `datetime.now()` puis adaptez l'heure avec la méthode
`datetime.replace()`.
</details>

## Exercice 2
Je souhaite être au lit à 23h au plus tard. À quelle heure ce soir est-ce que je dois commencer à 
regarder mes épisodes.

## Exercice 3
Je dois me lever à 6h demain matin et souhaite dormir 8h. À quelle heure au plus tard dois-je 
commencer à regarder mes épisodes ?

## Exercice 4
Je dois me lever à 6h du matin ce 29 octobre 2023 et souhaite dormir 8h. À quelle heure au plus 
tard dois-je commencer à regarder mes épisodes ?
