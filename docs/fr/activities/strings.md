# Mise en forme de chaînes de caractères

## Rappels
Une donnée que nous allons gérer doit être *formatée* afin d’être présentée à l’utilisateur.
Ceci peut être réalisé par la méthode `format()` des chaines de caractères :

```python
pref_string = "Mon langage favori est {}"
print(pref_string.format(name))
```

Les accolades permettent de mettre en forme les données à afficher. Le microlangage étant assez 
complexe, je vous invite à consulter  
[la documentation](https://docs.python.org/3.14/library/string.html#format-string-syntax)  pour les 
fonctionnalités exhaustives.

On retiendra les plus courantes :

* **{1}** permet d’afficher le second élément de la liste des données.
* **{:.2f}** permet d’afficher la donnée sous forme de réel avec deux chiffres après la virgule
* **{:10}** réserve 10 espaces pour afficher la donnée
* **{:10.2f}** réserve 10 espaces pour afficher un réel avec deux chiffres après la virgule
* **{1:10.2f}** réserve 10 espaces pour afficher sous forme de réel avec deux chiffres après la 
  virgule le second élément de la liste des données

Python dispose également des *f-string* dont la syntaxe est la suivante :
```python
print(f"Mon langage favori est {name}")
```
Les fonctionnalités de mise en forme de la méthode `.format()` s’appliquent également aux f-string.

## Premier exercice
Un petit calcul de vitesse. J’ai parcouru **19, 7 mètres** en **6,892 secondes**. Affichez la 
vitesse avec son unité en imposant deux chiffres après le point décimal.

---
## Second exercice
Reprenez votre fonction levant une exception et mettez à jour le message d'erreur lors de la levée 
de l'exception pour être plus informatif.

---
## Troisième exercice
Je veux déterminer à quelle heure j'irai me coucher après avoir regardé quelques épisodes de ma 
série.

Je regarderai à la suite 7 épisodes de 23 minutes.

Le début de ma soirée est obtenu par la fonction `pyflix.datasource.get_start_time()`.

Affichez l'heure de coucher sous la forme `"J'irai me coucher à 22h04"`
