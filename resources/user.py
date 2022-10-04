from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.user import UserModel
from resources import require_roles
import re

class UserResource(Resource):
    @require_roles('admin')
    def get(self):
        if 'id' in request.args:
            item = UserModel.get(request.args['id'])
            item = serialize_model(item)
            return item
        elif 'email' in request.args:
            item = UserModel.get_by_email(request.args['email'])
            item = serialize_model(item)
            return item
        elif 'cpf' in request.args:
            item = UserModel.get_by_cpf(request.args['cpf'])
            item = serialize_model(item)
            return item
        list = UserModel.list()
        return serialize_model_list(list)

    @require_roles('admin')
    def post(self):
        try:
            data = request.get_json()
            item = UserModel()

            if check_cpf(data['cpf']) is False:
                return 'CPF incorreto', 401

            if check_email(data['email']) is False:
                return 'Email incorreto', 401

            if data['role'] not in ['admin', 'common']:
                return 'Perfil incorreto, selecione entre: "admin" ou "common"', 401

            if UserModel.get_by_cpf(data['cpf']) != None:
                return 'CPF já registrado', 401

            if UserModel.get_by_email(data['email']) != None:
                return 'Email já registrado', 401

            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.role = Roles().name_to_enum(data['role'])
            item.save()
            return "successo", 201
        except:
            return "error", 401

    @require_roles('admin')
    def put(self):
        try:
            data = request.get_json()
            item = UserModel.get(data['id'])

            if check_cpf(data['cpf']) is False:
                return 'CPF incorreto', 401

            if check_email(data['email']) is False:
                return 'Email incorreto', 401

            if data['role'] not in ['admin', 'common']:
                return 'Perfil incorreto, selecione entre: "admin" ou "common"'

            if data['cpf'] != item.cpf:
                if UserModel.get_by_cpf(data['cpf']) != None:
                    return 'CPF já registrado para outro usuário'

            if data['email'] != item.email:
                if UserModel.get_by_email(data['email']) != None:
                    return 'Email já registrado para outro usuário'

            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.role = Roles().name_to_enum(data['role'])
            item.update()
            return "successo", 201
        except:
            return "error", 401

    @require_roles('admin')
    def delete(self):
        try:
            if 'id' in request.args:
                item = UserModel.delete(request.args['id'])
                return "successo", 201
            return "No ID", 401
        except:
            return "error", 401
