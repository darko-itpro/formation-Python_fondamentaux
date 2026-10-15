# Traitement de fichiers

## Le contenu d'un répertoire

Le répertoire `/assets/files/` contient des fichiers média dont le nom est structuré avec les 
informations sur l'épisode.

Écrivez une fonction qui :

 * _Ouvre_ le répertoire (le chemin doit être passé en paramètre).
 * Parcourt le contenu élément par élément.
 * Récupère les noms de fichiers et les affiche

Cette fonction pourra être utilisée avec un autre exercice.

## Le contenu d'un fichier

Le répertoire `/assets` contient un fichier `showslist.csv`. Ce fichier au format `csv` contient 
une liste de données à propos de séries que nous pouvons intégrer dans nos données.

Nous allons écrire une fonction afin d'extraire les données de ce fichier.

Écrivez une fonction qui :

 * Ouvre le fichier (le chemin doit être passé en paramètre).
 * Parcourt le fichier ligne à ligne.
 * Décompose le contenu de chaque ligne en une liste.
 * Ordonne la liste selon les données attendues comme paramètres du constructeur `Episode`. 
   Attention, le titre de la série doit aussi être présent en premier élément.
 * Assurez-vous lors de cette conversion que les types de données soient bien respectés.
 * Affichez la liste obtenue (cette partie est temporaire pour vérifier le bon comportement)
