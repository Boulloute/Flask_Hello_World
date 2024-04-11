from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
@app.route('/contact/')
def MaPremiereAPI():
    return render_template('contact.html')                                                                                                                                  
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/somme/<int:val_user>/<int:val_user2>')
def somme(n1 + n2):
  n1 = input(val_user)
  n2 = input(val_user2)
  somme = n1 + n2
  if somme % 2 == 0 :
    return "pair"
  else: 
    return "impair"
if __name__ == "__main__":
  app.run(debug=True)
