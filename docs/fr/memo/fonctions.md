# Les fonctions

## Structure
```
def nom_fonction(param1, param2):
    do_somerhing()
    return value
```

## Retours
* `return` est optionnel
* `return` avec ou sans paramètre interrompt l'exécution de la fonction
* `return value` retourne la valeur associée à `value`. La fonction *retourne* cette valeur.
* L'absence de `return` entraine un `return None` implicite
* Un `return` sans paramètre correspond à un `return none`

## Paramètres
### Paramètres positionnels
Déclaration :
```python
def func(param1, param2):
    pass
```

Appel :
```python
func('val1', 'val 2')
```
### Paramètres optionnels
Déclaration :
```python
def func(param="value"):
    pass
```

Appels :
```python
func()
func('val')
```

Les paramètres optionnels sont déclarés en dernier.
```python
def func(param_pos, param_opt="value"):
    pass
```

```python
func('val opsitionnelle')
func('val opsitionnelle', 'val optionnelle')
```

### Arguments nommés
```python
def func(param_pos, param_opt="value"):
    pass
```

```python
func('val opsitionnelle', param_opt='val optionnelle')
```

---
## Utilisation des type hints
```python
def func(param_pos:str, param_opt:int = 1) -> str:
    return param_pos * param_opt
```
