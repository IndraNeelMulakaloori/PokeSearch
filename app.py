from flask import  Flask,render_template,request
import requests
import pokeapi


app = Flask(__name__)

@app.route("/",methods = ["GET", "POST"])
def hello_world():
    return render_template('index.html')

@app.route("/result",methods=["GET", "POST"])
def result():
    pokemon_name = request.form['pokemon']

    response = pokeapi.fetchResult(pokemon_name)
    print(response['picture'])
    return render_template('result.html',response = response)

if __name__ == '__main__':
    app.run(port = 8000,debug=True)

    
