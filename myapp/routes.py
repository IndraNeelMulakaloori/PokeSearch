from flask import  Blueprint,render_template,request,url_for
import requests
from .pokeapi import fetchResult


main = Blueprint('main',__name__)

@main.route("/",methods = ["GET", "POST"])
def index():
    return render_template("index.html")

@main.route("/result",methods=["GET", "POST"])
def result():
    pokemon_name = request.form['pokemon']

    response = fetchResult(pokemon_name)
    if len(response) == 0:
        response = {'name' : "Pokemon Doesn't exist",
                    'picture' : "https://cdn.dribbble.com/users/2917698/screenshots/17312745/media/62253fac4f0b0f2e43fb010fb65dd707.jpg"}
       

    return render_template('result.html',response = response)