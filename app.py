from flask import  Flask,render_template,request
import requests
import pokeapi

port = process.env.PORT or 4000
app = Flask(__name__)

@app.route("/",methods = ["GET", "POST"])
def hello_world():
    return render_template('index.html')

@app.route("/result",methods=["GET", "POST"])
def result():
    pokemon_name = request.form['pokemon']

    response = pokeapi.fetchResult(pokemon_name)
    if len(response) == 0:
        response = {'name' : "Pokemon Doesn't exist",
                    'picture' : "https://cdn.dribbble.com/users/2917698/screenshots/17312745/media/62253fac4f0b0f2e43fb010fb65dd707.jpg"}
       

    return render_template('result.html',response = response)

# if __name__ == '__main__':
#     app.run(port = port,debug=True)

    
