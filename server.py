"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULT = ["ugly", "angry", "silly"]


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.<a href = "/hello">hello</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    # loop over list
    compliment_html = []
    for compliment in AWESOMENESS:
        compliment_html.append(f"<option value={compliment}>{compliment}</option>")
    phrase = ",".join(compliment_html)


    insult_html = []
    for disses in INSULT:
        insult_html.append(f"""<input type = "radio" name = "diss" value = {disses}>{disses} """)
    phrase_insult = " ".join(insult_html)
    # print(compliment_html)
    # append f"<option {dlafjsdkf}>{dlkjfalksdjf}"
    # phrase = ", ".join(["<b>cool</b>", "<i>smart</i>", "happy", "weird"])

    # print(phrase)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <br>
          Choose your compliment <select name="compliment">
            {phrase}            
          </select> 
          <input type="submit" value="Submit compliment">
        </form>
        <form action="/diss">
          <br>
          What's your name? <input type="text" name="person">
          <br>
          <br>
          Choose your insult
            {phrase_insult}

          <input type="submit" value="Submit diss">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def insult_person():
    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
