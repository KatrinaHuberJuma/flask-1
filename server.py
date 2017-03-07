from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>
      Hi! This is the home page.
      <p><a href="/hello">Get greeted!</a></p>
    <html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <p>Choose your compliment</p>
          <select name="compliment">
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
            <option value="{}">{}</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(AWESOMENESS[0], AWESOMENESS[0], AWESOMENESS[1], AWESOMENESS[1],
               AWESOMENESS[2], AWESOMENESS[2], AWESOMENESS[3], AWESOMENESS[3],
               AWESOMENESS[4], AWESOMENESS[4], AWESOMENESS[5], AWESOMENESS[5],
               AWESOMENESS[6], AWESOMENESS[6], AWESOMENESS[7], AWESOMENESS[7],
               AWESOMENESS[8], AWESOMENESS[8], AWESOMENESS[9], AWESOMENESS[9],
               AWESOMENESS[10], AWESOMENESS[10], AWESOMENESS[11], AWESOMENESS[11],
               AWESOMENESS[12], AWESOMENESS[12], AWESOMENESS[13], AWESOMENESS[13])


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, %s! I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
