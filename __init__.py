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
@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)
@app.route('/pairimpair/<n1>/<n2>')
def impair_pair(val_user):
  n1 = input(val_user)
  n2 = input(val_user)
  somme = n1 + n2
  if somme %2 = 0 :
    print("pair")
  else: 
    print("impair")
if __name__ == "__main__":
  app.run(debug=True)
