import requests

URI = "https://pokeapi.co/api/v2/"
endpoint = {
    'pokemon' : 'pokemon'
}



def fetchResult(pokemon_name):
    pokemon_name = pokemon_name.lower()
    URL = URI + endpoint['pokemon'] +'/' + pokemon_name

    response = requests.get(URL)

    if response.status_code == 404:
        return "Not Found"
    
    data = stripData(response.json())
    return data

def stripData(data):

    result = {}
    result['name'] = data["name"].capitalize()
    result['weight'] = data["weight"]
    result['height'] = data['height']
    result['base_experience'] = data['base_experience']

    abilities = []

    for record in data['abilities']:
        abilities.append(record['ability']['name'])
    result['abilities'] = abilities

    types = []

    for record in data['types']:
        types.append(record['type']['name'])
    result['types'] = types 

    moves = []

    for record in data['moves']:
        moves.append(record['move']['name'])
    result['moves'] = moves

    result['cries'] = data['cries']['latest']
    result['picture'] = data['sprites']['other']['official-artwork']['front_default']

    return result



