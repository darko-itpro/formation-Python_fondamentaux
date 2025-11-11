# Les tests paramétrés

Plutôt que d'écrire plusieurs tests pour simplement tester une série de valeurs, il est possible de 
paramétrer les tests.

Commencez par créer une liste contenant une séquences de données d'entrée et de données attendues.

```python
testdata = [
    (datain1, datain2, expected1),
    (datain3, datain4, expected2),
]
```

Le seul test fera appel à un décorateur

```python
import pytest

@pytest.mark.parametrize("a, b, expected", testdata)
def test_something(a, b, expected):
    assert do_some_stuff(a, b) == expected
```