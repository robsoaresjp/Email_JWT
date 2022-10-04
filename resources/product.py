from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.product import ProductModel
from resources import require_roles
import re

class ProductResource(Resource):
    @require_roles('admin', 'common')
    def get(self):
        if 'id' in request.args:
            item = ProductModel.get(request.args['id'])
            item = serialize_model(item)
            return item
        elif 'id_provider' in request.args:
            itens = ProductModel.list_by_provider(request.args['id_provider'])
            itens = serialize_model_list(itens)
            return itens
        list = ProductModel.list()
        return serialize_model_list(list)

    @require_roles('admin')
    def post(self):
        try:
            data = request.get_json()
            item = ProductModel()

            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.save()

            return "successo", 201
        except:
            return "error", 401

    @require_roles('admin')
    def put(self):
        try:
            data = request.get_json()
            item = ProductModel.get(data['id'])

            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.update()

            return "successo", 201
        except:
            return "error", 401

    @require_roles('admin')
    def delete(self):
        try:
            if 'id' in request.args:
                item = ProductModel.delete(request.args['id'])
                return "successo", 201
            return "No ID", 401
        except:
            return "error", 401
