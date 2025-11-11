# Les bases des tests avec pytest

Les tests sont un outil fondamental pour tout bon développement. Vous allez compléter les fonctions 
écrites précédemment par des tests.

## Aide mémoire
Dans la suite
- `tested_function(fixed_params)` représente la fonction testée à laquelle on fourni des arguments 
- *fixés*.
- `value` représente le retour de cette fonction.
- `expected_value` représente la valeur attendue.

### Écrire un test
Créer un fichier `test_nom_ce_qui_est_teste.py`.
Créer des fonctions de test du type :
```python
def test_tested_case():
    value = tested_function(fixed_params)
    assert expected_value == value
```

### Tester la levée d’exception
```python
def test_exception_raised():
    with pytest.raises(ExpectedError):
        tested_function(fixed_params)
```