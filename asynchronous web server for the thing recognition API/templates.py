MainPage = """

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Main page</title>
    </head>
    <body>
        <form enctype="multipart/form-data" method="post" action="http://127.0.0.1:8000/SendFile">
            <p>
                <input type="file" name="file" />
            </p>
            <p>
                <input type="submit" value="Send" />
            </p>
        </form>
    </body>
</html>

"""

def ResponseHTML(string:str):
    return f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Response</title>
    </head>
    <body>

    {string}

        </body>
</html>

"""