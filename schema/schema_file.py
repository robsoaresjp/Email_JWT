from models import db
from sqlalchemy import create_engine
from schema.seed import *

class Schema:
    @staticmethod
    def migration():
        db.configure_mappers()
        db.create_all()

    def prepare_db():
        first_user()
        first_provider()
        first_product()
        first_order()
        return
