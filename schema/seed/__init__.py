from models.user import UserModel
from models.provider import ProviderModel
from models.product import ProductModel
from models.order import OrderModel

def first_user():
    if UserModel.get_by_cpf("43268926843") != None:
        return
    new_user = UserModel()
    new_user.name = "Daniel Silva Menegasso"
    new_user.cpf = "43268926843"
    new_user.email = "ds.menegasso+user@hotmail.com"
    new_user.password = "Dani@1234"
    new_user.address = "Endereço 01"
    new_user.city = "Cidade 01"
    new_user.country = "País 01"
    new_user.cep_code = "000000-000"
    new_user.role = 1
    new_user.save()
    return

def first_provider():
    if ProviderModel.get_by_cnpj("67413740000120") != None:
        return
    new_provider = ProviderModel()
    new_provider.name = "Fornecedor 01"
    new_provider.cnpj = "67413740000120"
    new_provider.address = "Endereço 01"
    new_provider.city = "Cidade 01"
    new_provider.country = "País 01"
    new_provider.cep_code = "000000-000"
    new_provider.responsible_name = "Daniel Silva Menegasso"
    new_provider.responsible_email = "ds.menegasso+user@hotmail.com"
    new_provider.responsible_phone = "+55(11)96602-1723"
    new_provider.active = True
    new_provider.save()
    return

def first_product():
    if ProviderModel.get_by_cnpj("67413740000120") == None:
        first_provider()
        return
    new_product = ProductModel()
    new_product.name = "Produto 01"
    new_product.provider = ProviderModel.get_by_cnpj("67413740000120")
    new_product.quantity = 100
    new_product.price = 10.0
    new_product.available = True
    new_product.save()
    return

def first_order():
    if UserModel.get_by_cpf("43268926843") == None:
        first_user()
        return
    if len(ProductModel.list()) == 0:
        first_product()
        return
    new_order = OrderModel()
    new_order.user = UserModel.get_by_cpf("43268926843")
    new_order.products = str({"id": 1, "quantity": 10})
    new_order.save()
    return
