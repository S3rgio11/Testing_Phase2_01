from flask import Flask, request, jsonify
from flask_cors import CORS
from handler.championship import ChampionshipsHandler


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello there!"


@app.route('/championships', methods=['POST', 'GET'])
def handleChampionship():
    if request.method == 'GET':
        return ChampionshipsHandler().getAllChampionship()
    elif request.method == 'POST':
        return ChampionshipsHandler().createChampionship(request.json)
    else:
        return jsonify("Unsupported Method"), 405
    
@app.route('/championships/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleChampionshipById(id):
    if request.method == 'DELETE':
        return ChampionshipsHandler().deleteChampionshipById(id)
    elif request.method == 'PUT':
        return ChampionshipsHandler().updateChampionshipById(request.json, id)
    elif request.method == 'GET':
        return ChampionshipsHandler().getChampionshipById(id)
    else:
        return jsonify("Unsupported Method"), 405


if __name__ == '__main__':
    app.run(debug=True)
    
    