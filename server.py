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



@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Say hello!</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    inputs = """"""

    for compliment_name in AWESOMENESS:
      
        compliment = f"""<input type="radio" name='compliment' value='{compliment_name}' id="{compliment_name}">
        <label for="{compliment_name}">{compliment_name.title()}</label>"""

        inputs += compliment

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <p>Pick a compliment or a diss.</p>
        <form action="/greet">
          What's your name? <input type="text" name="person">

          <fieldset>
            <legend>Which compliment would you like?</legend>
              {inputs}
          </fieldset>
          
          <input type="submit" value="Submit">

        </form>

        <form action="/diss">
          What's your name? <input type="text" name="person">
          <fieldset>
            <legend>Which diss would you like?</legend>
          
              <input type="radio" name='diss' value='bad'>Bad
              <input type="radio" name='diss' value='cruel'>Cruel
              <input type="radio" name='diss' value='terrible'>Terrible
              <input type="radio" name='diss' value='rude'>Rude
              <input type="radio" name='diss' value='a mistake'>A Mistake
          </fieldset>

          
          <input type="submit" value="Submit">
        </form>
        
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def diss_someone():
  """Diss a user"""
  
  player = request.args.get("person")
  diss = request.args.get("diss")
  
  return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """






if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
