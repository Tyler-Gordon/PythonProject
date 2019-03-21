from arena              import Arena
from abstract_character import AbstractCharacter
from knight_character   import KnightCharacter
from mage_character     import MageCharacter
from ranger_character   import RangerCharacter
from thief_character    import ThiefCharacter
from flask              import Flask, request
from json               import dumps

app = Flask(__name__)
arena = Arena('arena.json')

@app.route('/arena/characters',mothods=['POST'])
def post_new_character():
    content = request.json
    if content == None or content == '':
        response = app.response_class(response="404 - DATA NOT FOUND",status=404)
    else:
        if content['type'] == 'Knight':
            character = KnightCharacter()
        elif  content['type'] == 'Mage':
            character = MageCharacter()
        elif  content['type'] == 'Ranger':
            character = RangerCharacter()
        elif  content['type'] == 'Thief':
            character = ThiefCharacter()
        else:
            response = app.response_class(response="404 - TYPE NOT FOUND",status=404)
            return response
        arena.add_character(character)
        response = app.response_class(response="OK",status=200)        

    return response

@app.route('/arena/characters/<id>',mothods=['PUT'])
def put_character(id):
    if id == int:
        if arena.character_exists(id):
            content = request.json

            if content['type'] == 'Knight':
                character = KnightCharacter()
            elif  content['type'] == 'Mage':
                character = MageCharacter()
            elif  content['type'] == 'Ranger':
                character = RangerCharacter()
            elif  content['type'] == 'Thief':
                character = ThiefCharacter()

            arena.update(character)
            response = app.response_class(response="OK",status=200)
        else:
            response = app.response_class(response="404 - CHAR NOT FOUND",status=404)
    else:
        response = app.response_class(response="400 - BAD ID",status=400)
    return response

@app.route('/arena/characters/<id>',mothods=['DELETE'])
def del_character(id):
    if id == int:
        if arena.character_exists(id):
            arena.delete(id)
            response = app.response_class(response="OK",status=200)
        else:
            response = app.response_class(response="404 - CHAR NOT FOUND",status=404)
    else:
        response = app.response_class(response="400 - BAD ID",status=400)
    return response

@app.route('/arena/characters/<id>',mothods=['GET'])
def get_character(id):
    if id == int:
        if arena.character_exists(id):
            arena.get_character(id)
            response = app.response_class(response="OK",status=200)
        else:
            response = app.response_class(response="404 - CHAR NOT FOUND",status=404)
    else:
        response = app.response_class(response="400 - BAD ID",status=400)
    return response

@app.route('/arena/characters/all',mothods=['GET'])
def get_all_characters():
    if arena.get_all() == None or arena.get_all() == '':
        response = app.response_class(response="404 - CHARACTERS NOT FOUND",status=404)
    else:
        arena.get_all()
        response = app.response_class(response="OK",status=200)
    return response


@app.route('/arena/characters/all/<type>',mothods=['GET'])
def get_all_characters_type(type):
    if type == str:
        if type in ['Knight','Mage','Ranger','Thief']:
            arena.get_all_by_type(type)
            response = app.response_class(response="OK",status=200)
        else:
            response = app.response_class(response="404 - TYPE NOT FOUND",status=404)
    else:
        response = app.response_class(response="400 - BAD TYPE STRING",status=400)
    return response

if __name__ == "__main__":
    app.run()