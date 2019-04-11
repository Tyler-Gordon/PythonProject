from arena              import Arena
from abstract_character import AbstractCharacter
from knight_character   import KnightCharacter
from mage_character     import MageCharacter
from flask              import Flask, request
import json

app = Flask(__name__)

CHARACTERS_DB = 'characters.sqlite'

arena = Arena(CHARACTERS_DB)

@app.route('/arena/characters',methods=['POST'])
def add_character():

    content = request.get_json()

    try:
        
        if content['type'] == 'knight':
            character = KnightCharacter(content['username'], content['health'], content['attack'], content['defence'],
            content['attack_speed'], content['type'], content['sword_crit_chance'], content['sword_crit_modifier'], content['shield_defence_modifier'])
        elif content['type'] == 'mage':
            character = MageCharacter(content['username'], content['health'], content['attack'], content['defence'],
            content['attack_speed'], content['type'], content['spell_power'], content['spell_chance'])

        char_id = arena.add_character(character)
        response = app.response_class(
            response="OK - " + str(char_id),
            status=200
        )    

    except ValueError:
        response = app.response_class(
            response="INVALID DATA",
            status=400
        ) 

    return response

@app.route('/arena/characters/<char_id>', methods=['PUT'])

def update_character(char_id):
    content = request.get_json()

    try:
        if content['type'] == 'knight':
            character = KnightCharacter(content['username'], content['health'], content['attack'], content['defence'],
            content['attack_speed'], content['type'], content['sword_crit_chance'], content['sword_crit_modifier'], content['shield_defence_modifier'])
        elif content['type'] == 'mage':
            character = MageCharacter(content['username'], content['health'], content['attack'], content['defence'],
            content['attack_speed'], content['type'], content['spell_power'], content['spell_chance'])
        
        character.id = char_id
        arena.update_character(character)
        response = app.response_class(
            response="OK",
            status=200
        )

    except ValueError:
        response = app.response_class(
            response="INVALID DATA",
            status=400
        )

    return response

@app.route('/arena/characters/<char_id>',methods=['DELETE'])
def delete_character(char_id):

    if int(char_id) > 0:
        response = app.response_class(
            response="BAD ID",
            status=400
        )

        try:
            arena.delete_character(char_id)
            response = app.response_class(
                response="OK",
                status=200
            )

        except:
            response = app.response_class(
                response="CHAR NOT FOUND",
                status=404
            )
        
    return response

@app.route('/arena/characters/<char_id>',methods=['GET'])
def get_character(char_id):

    if int(char_id) > 0:
        response = app.response_class(
            response="BAD ID",
            status=400
        )

        try:
            character = arena.get_character(char_id)

            response = app.response_class(
                response=json.dumps(character.to_dict()),
                mimetype='application/json',
                status=200
            )

        except:
            response = app.response_class(
                response="CHAR NOT FOUND",
                status=404
            )

    return response

@app.route('/arena/characters/all',methods=['GET'])
def get_all_characters():

    characters = [character.to_dict() for character in arena.get_all()]

    response = app.response_class(
        response=json.dumps(characters),
        mimetype='application/json',
        status=200
    )

    return response


@app.route('/arena/characters/all/<char_type>',methods=['GET'])
def get_all_characters_type(char_type):

    if char_type.lower() in ['knight','mage']:
        characters = [character.to_dict() for character in arena.get_all_by_type(char_type)]

        response = app.response_class(
            response=json.dumps(characters),
            mimetype='application/json',
            status=200
        )

    else:
        response = app.response_class(
            response="INVALID TYPE",
            status=400
        )

    return response

if __name__ == "__main__":
    app.run()