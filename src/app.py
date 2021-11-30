from flask import Flask, app, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html') 

if __name__ == '__main__':
    app.run('0.0.0.0')
