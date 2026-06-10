# Les règles de gestion

Ajouter un épisode ne doit pas entrainer l'ajout de doublon.

 * Améliorez la méthode `add_episode()` pour qu'elle lève une `ValueError` si l'épisode à ajouter 
   existe déjà dans la série.

## Rappel : tester la levée d'exception

Avec Pytest, tester la levée d'exception se fait avec un contexte manager :

```python
import pytest

def test_raise():
    with pytest.raises(ValueError):
        int("quarante deux")
```
