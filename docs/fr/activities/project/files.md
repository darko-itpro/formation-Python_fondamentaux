# Traitement de fichiers

Le répertoire `/assets` contient un fichier `showslist.csv`. Ce fichier au format `csv` contient 
une liste de données à propos de séries que nous pouvons intégrer dans nos données.

Nous allons écrire une fonction qui nous permet d'extraire les données de ce fichier.

Écrivez une fonction qui :

 * Ouvre le fichier (le chemin doit être passé en paramètre).
 * Parcourt le fichier ligne à ligne.
 * Décompose le contenu de chaque ligne en une liste.
 * Ordonne la liste selon les données attendues comme paramètres du constructeur `Episode`. 
   Attention, l'information de série doit aussi être présent.
 * Assurez-vous lors de cette conversion que les types de données soient bien respectés.
 * Affichez la liste obtenue (cette partie est temporaire pour vérifier le bon comportement)
