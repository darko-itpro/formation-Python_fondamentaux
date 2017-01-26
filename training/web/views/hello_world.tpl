<html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
    <h1>Bottle works!</h1>
    <p>You can <a href="/">go back</a></p>
    <br />
    Say Hello to…
    <ul>
        % for name in names:
        <li><a href="/hello/{{name}}">{{name}}</a> </li>
        % end
    </ul>
    Or add another
    <form action="/add/" method="post">
        <input type="text" name="new_hero"><br />
        <input type="submit" value="Submit">
    </form>
    </body>
</html>