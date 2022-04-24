from http import server
from flask import Flask
from flask_restplus import Api, Resource
from src.server.instance import server

app, api = server.app, server.api

game_db = [
    {'id': 1, 'name': 'Super Mario Bros.', 'year': 1985},
    {'id': 2, 'name': 'Super Mario Bros. 2', 'year': 1988},
    {'id': 3, 'name': 'Super Mario Bros. 3', 'year': 1990},
    {'id': 4, 'name': 'Super Mario World', 'year': 1994},
    {'id': 5, 'name': 'Super Mario World 2: Yoshi\'s Island', 'year': 1996},
    {'id': 6, 'name': 'Super Mario World 3: Wario\'s Woods', 'year': 1999},
    {'id': 7, 'name': 'Super Mario World 4: Super Mario Bros. 3', 'year': 2003},
    {'id': 8, 'name': 'Super Mario World 5: Super Mario World', 'year': 2007},
    {'id': 9, 'name': 'Sonic', 'year': 1991},
    {'id': 10, 'name': 'Sonic 2', 'year': 1992},
    {'id': 11, 'name': 'Sonic 3', 'year': 1993}
]

@api.route('/Jogos')
class gameList(Resource):
    def get(self, ):
        return game_db
        
    def post(self, ):
        response = api.payload
        game_db.append(response)
        return response, 200