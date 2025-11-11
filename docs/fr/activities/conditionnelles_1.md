# Les conditionnelles

## Aide mémoire
La structure d’une conditionnelle est

```python
if condition:
    code
```

Celle du si…sinon

```python
if condition:
    code
else:
    code
```

Enfin, le si…sinon si…()…sinon

```python
if condition:
    code
elif condition:
    code
else:
    code
```

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec les fichiers suivants :

 * `exos/base/exo_03_01.py` qui vous est fourni. 
 * `exos/base/exo_03_02.py` qui vous est fourni.

---

## Premier exercice
Le fichier source `exo_03_01.py` contient la déclaration de deux variables auxquelles sont affectées
des données correspondant à deux épisodes : un épisode vu et un non vu.

Ce code déclare également une variable episode à laquelle est affectée une des variable précédente
et une ligne en commentaire où c’est l’autre. Vous allez travailler sur la variable episode, ainsi,
pour tester l’un ou l’autre comportement, il vous suffira de commenter l’une ou l’autre ligne.

* Ecrivez le code qui affichera « l’épisode a été vu » si l’épisode… a été vu et rien si il n’a pas
  été vu.
* Complétez le code pour qu’il affiche « l’épisode a été vu » si l’épisode a été vu et « l’épisode
  n’a pas été vu » si il ne l’a pas été. Le code que vous écrirez pourra être « parlant ».

---

## Second exercice
Le ficher source `exo_03_02.py` contient un code similaire mais l’information vu ou non est
représentée par un entier représentant le nombre de fois où l’épisode a été vu.

Reprenez les questions précédentes pour cette représentation de données.