# Les tests paramétrés

Plutôt que d'écrire plusieurs tests pour simplement tester une série de valeurs, il est possible de 
paramétrer les tests.

1. Déclarer une liste de paramètre(s) et valeur(s) attendue(s)
```python
test_data = [
    (input1, expected1),
    (input2, expected2),
    (input3, expected3),
    …
    (inputn, expectedn),
]
```

 2. Déclarer le test les utilisant en le décorant avec le décorateur `@pytest.mark.parametrized`
```python
@pytest.mark.parametrized("param, expected", test_data):
def test_something(param, expected):
    assert func_to_test(param) == expected
```

Le décorateur `@pytest.mark.parametrized` prends 2 paramètres :

 * Une chaine de caractère décrivant le contenu des paramètres. Chaque élément décrit est identifié 
   par un nom python compatible.
 * Un itérable contenant les paramètres à utiliser.

La fonction de test déclare alors en paramètres les paramètres attendus pour le test en reprenant 
les noms utilisés dans le décorateur.
