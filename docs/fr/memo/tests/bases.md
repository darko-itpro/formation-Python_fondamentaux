# Aide mémoire des bases avec pytest

## Rappel du principe et des phases de test

Tester consiste à exécuter son code (appel à un callable) avec des données spécifiques au test et
observer que l'état du système est tel qu'attendu.

Tester comporte 4 phases :

 1. Arrange
 2. Act
 3. Assert
 4. Cleanup

## Principe des tests avec Pytest
Les tests sont des fonctions déclarées dans un package `tests` à la racine du projet.

Le code de test est dans un fichier source Python préfixé par `test_`.

Un test avec Pytest est une simple fonction dont le nom est préfixé par `test_` et possédant au
moins une expression `assert`.

```python
def test_something():
    assert 5 + 5 == 10
```

## Tester la levée d'exception

La levée d'exception se test avec le context manager fourni par pytest.

```python
import pytest

def test_must_raise():
    with pytest.raises(ValueError):
        int("toto")
```

La discrimination des exceptions levées peut se faire avec le paramètre optionnel `match=''`.
