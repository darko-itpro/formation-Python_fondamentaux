<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>

</head>
<body>
    <H1>{{title}}</H1>
    <a href="/">Home</a> - <a href="/show/{{title.replace(' ', '_')}}/add">Add Episode</a>
    % if episodes:
    <ul>
        % for episode in episodes:
        <li>{{episode.title}}</li>
        % end
    </ul>
    % else:
    <p>Pas d'épisode pour l'instant.</p>
    % end

</body>
</html>