# Les paramètres optionnels

Notre fonction créée précédemment, `add_to_playlist(episode: dict, playlist: list)`, devrait 
pouvoir permettre de créer une playlist. Elle devrait donc pouvoir être appelée sans le second 
paramètre.

Modifiez cette fonction pour que le paramètre `playlist: list` devienne optionnel. Si il n'est pas 
fourni, une nouvelle liste est créée.

Modifiez la fonction pour que son comportement respecte bien l'idiome Python.