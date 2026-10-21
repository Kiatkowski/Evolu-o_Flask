#CONTEM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
#BOOK REPRESENTA A ENTIDADE BOOK
from uuid import uuid4

from sqlalchemy import String,Text
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Book(db.Model):
#indicar que o book é um modelo gerenciado pelo SQLalchemy
    __tabelname__ = "book"
    id = db . Column(
        UUID(as_uuid=True),#vou usar o UUID
        primary_key = True,#chave primaria
        default = uuid4#quando criar um novo livro, um UUID será criado
    )
    title = db.Column(
        String(255),#recebe string
        nullable = False#não aceita nulo
    )
    author = db.Column(
        String(255),
        nullable = False
    )
    description = db.Column(
        Text,
        nullable = False
    )
    is_favorite = db.Column(
        db.Boolean,#Campo que vai armazenar o BOOL
        nullable = False,
        default = False#Tudo começa com 0
    )
    is_reading = db.Column(
        db.Boolean,
        mullable = False,
        default = False
    )
    is_finished = db.Column(
            db.Boolean,
            mullable = False,
            default = False
    )

#Transformando o modelo em dicionario
"""
POR ISSO SERÁ CRIADO UM MÉTODO RESPONSÁVEL POR TRANSFORMAR
O BOJETO BOOK EM UM DICIONÁRIO PYTHON

QUANDO OCORRER UMA CONSULTA AO NOSSO SISTEMA ELE RETORNA UM OBJETO BOOK,
ELE NÃO É SIMPLESMENTE UM DICT PYTHON.
O MÉTODO AS_DICT() FUNCIONA COMO UMA CAMADA DE CONVERSÃO, SLECIONANDO
APENAS O NECESSÁRIO PARA SER EXPOSTO PELA API E TRANSFORMANDO EM UM DICT,
ESTRUTURA PODE SER FACILMENTE SERIALIZADA PARA JSON NA RESPOSTA HTTP.
"""
def as_dict(self):
    return{
        "id":str(self.id),
        "title":self.title,
        "author":self.author,
        "description":self.description,
        "is_favorite":self.is_favorite,
        "is_reading":self.is_reading,
        "is_finished":self.is_finished
    }