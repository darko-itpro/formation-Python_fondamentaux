# Le module Pyflix

Pour les exercices, il vous sera demandé d’utiliser le module `pyflix.datasource`. Il existe en 
réalité plusieurs *versions* de ce module :

 - `datasource` pour un usage débutant.
 - `datasource_standard` est destiné aux formations Python _standard_.
 - `datasource_xpert` fournit des données plus complexes.
 - `datasource_hacker` est un niveau offrant plus de challenge. Ce niveau est en cours de 
   développement.

Toutes ces versions offrent les mêmes ressources. Vous pouvez donc les charger via un alias :
```python
import pyflix.datasource as ds
```
puis pour essayer avec une version plus complexe, modifiez la ligne par :
```python
import pyflix.datasource_xpert as ds
```

## Quels comportements ?
### Fonction `get_start_time()`
La fonction `get_start_time() -> str` aura des comportements différents en fonction du niveau 
activé.

 - En `datasource`, son retour sera toujours `"20h42"`.
 - En `datasource_standard`, son retour sera une valeur comprise entre `"19h00"` et `"21h38"`.
 - En `datasource_xpert`, le comportement est celui du `datasource_standard` mais le séparateur de 
  la chaine sera soit `"h"` soit `":"`.

### Fonction `get_season(user)`
La probabilité standard (`datasource` et `datasource_standard`) pour qu’un épisode soit vu est de 
8/10. Lorsqu’un épisode n’est pas vu, tous les suivants ne sont pas vu.  Un épisode non vu a 4 
chances sur 10 de ne pas avoir la clef `‘viewed’`.

Avec `datasource_xpert`, il y a 1 chance sur 20 que la fonction retourne une liste vide. Sinon, la 
probabilité qu’un épisode ne soit pas vu tombe également à 1 sur 20.