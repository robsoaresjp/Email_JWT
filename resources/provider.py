from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.provider import ProviderModel
from resources import require_roles
import re

class ProviderResource(Resource):
    @require_roles('admin')
    def get(self):
        if 'id' in request.args:
            item = ProviderModel.get(request.args['id'])
            item = serialize_model(item)
            return item
        elif 'email' in request.args:
            item = ProviderModel.get_by_email(request.args['email'])
            item = serialize_model(item)
            return item
        elif 'cnpj' in request.args:
            item = ProviderModel.get_by_cnpj(request.args['cnpj'])
            item = serialize_model(item)
            return item
        list = ProviderModel.list()
        return serialize_model_list(list)

    @require_roles('admin')
    def post(self):
        try:
            data = request.get_json()
            item = ProviderModel()

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
            item = ProviderModel.get(data['id'])

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
                item = ProviderModel.delete(request.args['id'])
                return "successo", 201
            return "No ID", 401
        except:
            return "error", 401
