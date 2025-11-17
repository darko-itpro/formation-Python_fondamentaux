# Configuration du PYTHONPATH dans VSCode

Le bouton *exécuter* de VS Code exécute le script dans son répertoire et non à la racine du projet. 
Les imports absolus sont alors introuvables car Python ne charge pas le répertoire racine comme 
racine des chemins.

## Configuration
Il est nécessaire d'ajouter la configuration du `PYTHONPATH` à VS Code via le fichier 
`settings.json`.

Pour Windows :
```json
{
    "terminal.integrated.env.windows": {"PYTHONPATH": "${workspaceFolder}"}
}
```

Pour Osx :
```json
{
    "terminal.integrated.env.osx": {"PYTHONPATH": "${workspaceFolder}"}
}
```

Pour Linux :
```json
{
    "terminal.integrated.env.linux": {"PYTHONPATH": "${workspaceFolder}"}
}
```

À vérifier que cette syntaxe fonctionne :
```json
{
    "terminal.integrated.env.*": {"PYTHONPATH": "${workspaceFolder}"}
}
```

## Références

 * [Documentation VS Code](https://code.visualstudio.com/docs/python/environments)
 * [Question Stack](https://stackoverflow.com/questions/53653083/how-to-correctly-set-pythonpath-for-visual-studio-code)