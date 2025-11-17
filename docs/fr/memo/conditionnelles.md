# Structures de contrôle : les conditionnelles

## Structure générale

Faire quelque chose si une condition
```python
if condition:
    do_something_if_condition_true()
```

Faire quelque chose si une condition, sinon
```python
if condition:
    do_something_if_condition_true()
else:
    do_something_if_condition_false()
```

Faire quelque chose si une condition, sinon faire si autre condition, …, sinon
```python
if condition:
    do_something_if_condition_true()
elif other_condition:
    do_something_if_othercondition_true()
else:
    do_something_if__all_conditions_false()
```
Il peut y avoir plusieurs `elif`.

---
## Les conditions
La structure doit retourner une donnée *vrai* ou *fausse*. Ce peut être :

 * une donnée
 * un opérateur de comparaison
 * un opérateur logique
 * un appel de fonction

### Opérateurs de comparaison

Opérateurs de comparaison : `==`, `!=`, `>`, `<`, `>=`, `<=`
Le test d'identité se fait avec le mot clef `is`

### Opérateurs logiques

| Opérateur | Signification | Exemple                         |
| --------- | ------------- | ------------------------------- |
| `not`     | Négation      | `not expression`                |
| `and`     | Conjonction   | `expression_1 and expression_2` |
| `or`      | Disjonction   | `expression_1 or expression_2`  |

 * `not`retourne un booléen
 * `and` et `or` retournent une des valeur de l'expression.
