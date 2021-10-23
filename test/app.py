from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Squid Game"
    picture_url = "ddakji.jpg"
    text = """You're waiting for your train and suddenly a man in a  suit walks up to you. He asks to play ddakji with him for money"""

    choices = [
        ('the_game',"Hell yes!"),
        ('not_happening',"Ignore the stranger")
    ]
   
    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)



@app.route("/the_game")
def the_game():
    title = "You start the game"
    
    text = """At first you loose but then you start to undestand the game and end up making some cash. The man invites you to play games with higher stakes and gives you a business card."""

    choices = [
        ('call',"Call right away"),
        ('not_happening',"Throw the card away")
    ]

    return render_template('card.html', title=title, text=text, choices=choices)

@app.route("/the_contract")
def call():
    title = "You called."
    
    text = """ You were taken to a strange place where you're asked to sign a simple contract. After signing you can't leave."""

    choices = [
        ('sign',"Sign it duh"),
        ('not_happening',"Not happening")
    ]

    return render_template('contract.html', title=title, text=text, choices=choices)

@app.route("/escape")
def not_happening():
    title = "You're saved"
    
    text = """...but broke."""

    choices = []

    return render_template('end.html', title=title, text=text, choices=choices)



@app.route("/the_real_game")
def sign():
    title = "The game started."
    
    text = """You don't speak Korean, so you didn't understand the rules and were killed."""

    choices = []

    return render_template('over.html', title=title, text=text, choices=choices)


@app.route("/pic")
def pic():
   picture_url="https://assets-prd.ignimgs.com/2021/10/01/gong-yoo-squid-game-1633128635449.jpg?fit=bounds&width=640&height=480"

