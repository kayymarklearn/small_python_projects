from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)
def add_css(func):
    def style(*args, **kwargs):
        number = kwargs.get('number')
        if number == random_number:
            return f"<div style='color: green'>{func(number)}" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/> </div>"
        elif number < random_number:
            return f"<div style='color: red'>{func(number)}" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/> </div>"
        else:
            return f"<div style='color: purple'>{func(number)}" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' /> </div>"

    return style

@app.route('/')
def index():
    return f"<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/> "

@app.route("/<int:number>")
@add_css
def guessed_number(number):
    if number == random_number:
        return f"<h1>You found me!</h1>"
    elif number < random_number:
        return f"<h1>Too low, try again!</h1>"
    else:
        return f"<h1>Too high, try again!</h1>"

print(random_number)
if __name__ == "__main__":
    app.run(debug=True)
