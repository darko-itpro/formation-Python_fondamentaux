# La capture d'exceptions

## Aide mémoire
Capturer une exception se fait avec la structure :
```python
try:
    …
except ValueError:
    do_something_for_exception()
```

Ici, le code sait gérer une `ValueError`.

La clause `finally` permet d'exécuter du code dans tous les cas.
```python
try:
    …
except ValueError:
    do_something_for_exception()
finally:
    cleanup()
```

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez revenir sur un des premiers fichiers :

 * `exos/base/exo_01b.py`qui vous est fourni.

## Exercice
Pour la mise en pratique de la capture des exceptions, nous allons simplement modifier le code de 
cet exercice.

Revenez sur le code du script `exo_01b.py`.

Capturez l’exception lorsque l’utilisateur saisit une chaine de caractère qui ne se convertit pas 
en entier et l’informe qu’il a fait une mauvaise saisie.