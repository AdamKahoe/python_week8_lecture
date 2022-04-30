from flask import Flask, request, session, redirect, render_template
import random
app = Flask(__name__)

app.secret_key = "W0rdn0w!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['post'])
def process():
    print(request.form['selected'])
    print(session['computer_choice'])
    choices = ("foot", "nuke", "cockroach")
    computer_choice = random.randint(0,2)
    session['computer_choice'] = choices[computer_choice]
    session['you_chose'] = request.form['selected']
    if session['computer_choice'] == "nuke" and request.form['selected'] == "nuke":
        session['results'] = "Draw"
    if session['computer_choice'] == "nuke" and request.form['selected'] == "cockroach":
        session['results'] = "You win!"
    if session['computer_choice'] == "nuke" and request.form['selected'] == "foot":
        session['results'] = "You lose!"
    if session['computer_choice'] == "foot" and request.form['selected'] == "nuke":
        session['results'] = "You lose!"
    if session['computer_choice'] == "foot" and request.form['selected'] == "cockroach":
        session['results'] = "You win!"
    if session['computer_choice'] == "foot" and request.form['selected'] == "foot":
        session['results'] = "Draw"
    if session['computer_choice'] == "cockroach" and request.form['selected'] == "nuke":
        session['results'] = "You win!"
    if session['computer_choice'] == "cockroach" and request.form['selected'] == "cockroach":
        session['results'] = "Draw"
    if session['computer_choice'] == "cockroach" and request.form['selected'] == "foot":
        session['results'] = "You lose!"
    return redirect('/')

@app.route('/reset')
def resest():
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)