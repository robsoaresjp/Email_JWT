class Roles():
    def __init__(self):
        self.switcher_by_name = {
            'admin': 1,
            'common': 2
        }

        self.switcher_by_number = {
            1: 'admin',
            2: 'common'
        }

    def enum_to_name(self, enum):
        return self.switcher_by_number.get(enum, 'Número Inválido')

    def name_to_enum(self, name):
        return self.switcher_by_name.get(name, 'Nome Inválido')

class Active():
    def __init__(self):
        self.switcher_by_name = {
            True: 1,
            False: 0
        }

        self.switcher_by_number = {
            1: True,
            0: False
        }

    def enum_to_name(self, enum):
        return self.switcher_by_number.get(enum, 'Número Inválido')

    def name_to_enum(self, name):
        return self.switcher_by_name.get(name, 'Nome Inválido')

class Status():
    def __init__(self):
        self.switcher_by_name = {
            'Aguardando aprovação': 0,
            'Pagamento aprovado': 1,
            'Ao entregar': 2,
            'Entregue': 3,
            'Cancelado': 4,
        }

        self.switcher_by_number = {
            0 : 'Aguardando aprovação',
            1 : 'Pagamento aprovado',
            2 : 'Ao entregar',
            3 : 'Entregue',
            4 : 'Cancelado',
        }

    def enum_to_name(self, enum):
        return self.switcher_by_number.get(enum, 'Número Inválido')

    def name_to_enum(self, name):
        return self.switcher_by_name.get(name, 'Número Inválido')
