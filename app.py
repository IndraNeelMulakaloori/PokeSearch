from flask import  Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/",methods = ["GET", "POST"])
def hello_world():
    return render_template('index.html')

@app.route("/result",methods=["GET", "POST"])
def result():
    pokemon = requests.form['name']
    
    return render_template('result.html',pokemon = pokemon)

if __name__ == '__main__':
    app.run(port = 8000,debug=True)

    
