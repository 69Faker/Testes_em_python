from peewee import *

db = SqliteDatabase('hortifruti.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    cep = CharField()

    class Meta():
        database = db


        