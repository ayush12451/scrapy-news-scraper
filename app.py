from flask import render_template,Flask
from test import payload_create,create_index
from random import shuffle

app = Flask(__name__)

@app.route("/")
def index():
    li = create_index()
    shuffle(li)
    return render_template('base.html', x='News', l=li)

@app.route("/tech")
def tech():
    li = payload_create('tech')
    return render_template('base.html',x = 'Tech News',l = li)

@app.route("/auto")
def auto():
    li = payload_create('auto')
    return render_template('base.html',x = 'Auto News',l = li)

@app.route("/general")
def general():
    li = payload_create('general')
    return render_template('base.html',x = 'General News',l = li

if __name__ == '__main__':
    app.debug = True
    app.run()