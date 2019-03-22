from arena              import Arena
from abstract_character import AbstractCharacter
from knight_character   import KnightCharacter
from mage_character     import MageCharacter
from flask              import Flask, request
import json

app = Flask(__name__)
arena = Arena('arena.json')

def create_character_from_json(data, cls):
    character = cls(data['username'], data['health'], data['attack'],
                    data['defence'], data['attack_speed'])
            
    return character

@app.route('/arena/characters',methods=['POST'])
def post_new_character():

    content = request.get_json()

    try:
        if content['type'].lower() == 'knight':
            character = create_character_from_json(content, KnightCharacter)

        elif content['type'].lower() == 'mage':
            character = create_character_from_json(content, MageCharacter)

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

@app.route('/arena/characters/<char_id>',methods=['PUT'])

def put_character(char_id):

    if char_id.isdigit():
        char_id = int(char_id)
        current_character = arena.get_character(char_id)

        if current_character:
            content = request.get_json()

            try:
                if content['type'].lower() == 'knight':
                    character = create_character_from_json(content, KnightCharacter)

                elif  content['type'].lower() == 'mage':
                    character = create_character_from_json(content, MageCharacter)
                
                character.set_id(char_id)
                arena.update(character)
                response = app.response_class(
                    response="OK",
                    status=200
                )

            except ValueError:
                response = app.response_class(
                    response="INVALID DATA",
                    status=400
                ) 
            
        else:
            response = app.response_class(
                response="CHAR NOT FOUND",
                status=404
            )
            
    else:
        response = app.response_class(
            response="INVALID ID",
            status=400
        )

    return response

@app.route('/arena/characters/<char_id>',methods=['DELETE'])
def del_character(char_id):

    if char_id.isdigit():
        char_id = int(char_id)
        character = arena.get_character(char_id)

        if character:
            arena.delete(char_id)
            response = app.response_class(
                response="OK",
                status=200
            )

        else:
            response = app.response_class(
                response="CHAR NOT FOUND",
                status=404
            )

    else:
        response = app.response_class(
            response="BAD ID",
            status=400
        )
        
    return response

@app.route('/arena/characters/<char_id>',methods=['GET'])
def get_character(char_id):

    if char_id.isdigit():
        char_id = int(char_id)
        character = arena.get_character(char_id)

        if character:
            response = app.response_class(
                response=json.dumps(character.to_dict()),
                mimetype='application/json',
                status=200
            )

        else:
            response = app.response_class(
                response="CHAR NOT FOUND",
                status=404
            )

    else:
        response = app.response_class(
            response="BAD ID",
            status=400
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