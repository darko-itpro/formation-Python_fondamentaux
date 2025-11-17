# Les chaines de caractères

## Généralités
Vous pouvez consulter les différentes méthodes des chaînes de caractères avec :
```python
>>> help(str)
```

Beaucoup de méthodes permettent de *modifier* les chaînes de caractères mais le type étant immuable,
ces méthodes retournent une nouvelle donnée.

## Formatage des chaînes de caractères
### La méthode `format()`

```python
pref_string = "Mon langage favori est {}"
print(pref_string.format(name))
```

Les accolades permettent de mettre en forme les données à afficher. Le microlangage étant assez 
complexe, je vous invite à consulter 
[la documentation](https://docs.python.org/3.14/library/string.html#format-string-syntax)  
pour les fonctionnalités exhaustives.

On retiendra les plus courantes :

* **{1}** permet d’afficher le second élément de la liste des données.
* **{:.2f}** permet d’afficher la donnée sous forme de réel avec deux chiffres après la virgule
* **{:10}** réserve 10 espaces pour afficher la donnée
* **{:10.2f}** réserve 10 espaces pour afficher un réel avec deux chiffres après la virgule
* **{1:10.2f}** réserve 10 espaces pour afficher sous forme de réel avec deux chiffres après la 
  virgule le second élément de la liste des données

### Les *f-string*
```python
print(f"Mon langage favori est {name}")
```
Les fonctionnalités de mise en forme de la méthode `.format()` s’appliquent également aux f-strings.

