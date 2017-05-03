<html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
    <h1>Ma médiathèque</h1>
    <p>You can <a href="/">go back</a></p>
    <br />
    Mes series
    <ul>
        % for name in series:
        <li><a href="/hello/{{name}}">{{name}}</a> </li>
        % end
    </ul>
    Vous pouvez en ajouter une
    <form action="/add/" method="post">
        <input type="text" name="new_hero"><br />
        <input type="submit" value="Submit">
    </form>
    </body>
</html>