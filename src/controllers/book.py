from http import server
from flask import Flask
from flask_restplus import Api, Resource
from server.instance import Server

app, api = server.app, server.api

book_db = [
    {'id':0, 'title':'A Game of Thrones', 'author':'George R.R. Martin', 'year':1996},
    {'id':1, 'title':'A Clash of Kings', 'author':'George R.R. Martin', 'year':1998},
]

@api.route('/Livros')
class Book(Resource):
    def get(self, ):
        return book_db