from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from helpers.enum import Status
from models.order import OrderModel
from models.product import ProductModel
from resources import require_roles
from os import environ
import jwt

class OrderResource(Resource):
    @require_roles('admin', 'common')
    def get(self):
        current_user = jwt.decode(request.headers['Authorization'], environ.get('JWT_SECRET_KEY'), options={'verify_exp': False})

        if Roles().enum_to_name(current_user['sub']['role']) == 'admin':
            if 'id' in request.args:
                item = OrderModel.get(request.args['id'])
                item = serialize_model(item)
                item['status'] = Status().enum_to_name(item['status'])
                return item
            elif 'id_user' in request.args:
                itens = OrderModel.list_by_user(request.args['id_user'])
                itens = serialize_model_list(itens)
                for item in itens:
                    item['status'] = Status().enum_to_name(item['status'])
                return itens
            list = OrderModel.list()
            itens = serialize_model_list(list)
            for item in itens:
                item['status'] = Status().enum_to_name(item['status'])
            return itens
        else:
            if 'id' in request.args:
                item = OrderModel.get(request.args['id'])
                if item.id_user == current_user['sub']['id']:
                    item = serialize_model(item)
                    item['status'] = Status().enum_to_name(item['status'])
                    return item
                else:
                    return "Você não tem acesso", 401
            else:
                itens = OrderModel.list_by_user(current_user['sub']['id'])
                itens = serialize_model_list(itens)
                for item in itens:
                    item['status'] = Status().enum_to_name(item['status'])
                return itens

    @require_roles('admin', 'common')
    def post(self):
        current_user = jwt.decode(request.headers['Authorization'], environ.get('JWT_SECRET_KEY'), options={'verify_exp': False})

        if Roles().enum_to_name(current_user['sub']['role']) == 'admin':
            data = request.get_json()
            item = OrderModel()
            error = ''

            for product in data['products']:
                prod = ProductModel.get(product['id'])

                if prod == None:
                    error = "Produto não encontrado. ID: " + product['id']

                if float(prod.quantity) - float(product['quantity']) < 0:
                    error = "Produto insuficiente"

                if prod.available is False:
                    error = "Produto indisponível"

                if float(prod.quantity) - float(product['quantity']) == 0:
                    prod.available = False

                prod.update()


            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.products = str(data['products'])
            item.status = 0 if error == '' else 4
            item.save()

            return "successo", 201
        else:
            error = ''
            data = request.get_json()
            item = OrderModel()

            for product in data['products']:
                prod = ProductModel.get(product['id'])

                if prod == None:
                    error = "Produto não encontrado. ID: " + product['id']

                if float(prod.quantity) - float(product['quantity']) < 0:
                    error = "Produto insuficiente"

                if prod.available is False:
                    error = "Produto indisponível"

                if float(prod.quantity) - float(product['quantity']) == 0:
                    prod.available = False

                prod.update()

            item.id_user = current_user['sub']['id']
            item.products = str(data['products'])
            item.status = 0 if error == '' else 4
            item.save()

            return "successo", 201
            
    @require_roles('admin')
    def put(self):
        try:
            data = request.get_json()
            item = OrderModel.get(data['id'])
            status = Status().name_to_enum(data['status'])
            item.update()

            return "successo", 201
        except:
            return "error", 401
