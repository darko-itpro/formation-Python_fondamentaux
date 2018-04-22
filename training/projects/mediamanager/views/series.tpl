<html>
    <head>
        <title>Gestion Médiathèque</title>
    </head>
    <body>
    <h1>Ma médiathèque</h1>
    <p>You can <a href="/">go back</a></p>
    <br />
    Mes series
    % if series:
    <ul>
        % for name in series:
        <li><a href="/hello/{{name}}">{{name}}</a> </li>
        % end
    </ul>
    % else:
    <p>Pas de série pour l'instant.</p>
    % end
    Ajouter une série :
    <form action="/add/" method="post">
        <input type="text" name="new_show"><br />
        <input type="submit" value="Submit">
    </form>
    </body>
</html>