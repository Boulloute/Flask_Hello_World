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
@app.route('/somme')
def somme():
    # Obtenez les valeurs de la requête GET sous forme de liste
    valeurs = request.args.getlist('valeur')
    
    # Convertissez les valeurs de chaînes en entiers et calculez la somme
    somme_resultat = sum(int(v) for v in valeurs)
    
    return f"<h2>La somme des valeurs saisies est : {somme_resultat}</h2>"
@app.route('/impair/<int:val_user>/<int:val_user2>')
def somme(val_user,val_user2):

  somme = val_user + val_user2
  if somme % 2 == 0 :
    return "pair"
  else: 
    return "impair"
if __name__ == "__main__":
  app.run(debug=True)
