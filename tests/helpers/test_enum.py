from helpers.enum import *

class TestEnums:
    def test_roles(self):
        assert Roles().enum_to_name(1) == 'admin'
        assert Roles().enum_to_name(2) == 'common'

        assert Roles().name_to_enum('admin') == 1
        assert Roles().name_to_enum('common') == 2

    def test_active(self):
        assert Active().enum_to_name(0) == False
        assert Active().enum_to_name(1) == True

        assert Active().name_to_enum(True) == 1
        assert Active().name_to_enum(False) == 0

    def test_status(self):
        assert Status().enum_to_name(0) == 'Aguardando aprovação'
        assert Status().enum_to_name(1) == 'Pagamento aprovado'
        assert Status().enum_to_name(2) == 'Ao entregar'
        assert Status().enum_to_name(3) == 'Entregue'
        assert Status().enum_to_name(4) == 'Cancelado'

        assert Status().name_to_enum('Aguardando aprovação') == 0
        assert Status().name_to_enum('Pagamento aprovado') == 1
        assert Status().name_to_enum('entregar') == 2
        assert Status().name_to_enum('Entregue') == 3
        assert Status().name_to_enum('Cancelado') == 4
