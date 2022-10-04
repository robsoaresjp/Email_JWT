from datetime import datetime
from models import db
from passlib.hash import pbkdf2_sha256 as sha256

class ProviderModel(db.Model):
    __tablename__ = "provider"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), primary_key=False)
    cnpj = db.Column(db.String(14), primary_key=False)
    address = db.Column(db.String(255), primary_key=False)
    city = db.Column(db.String(100), primary_key=False)
    country = db.Column(db.String(50), primary_key=False)
    cep_code = db.Column(db.String(20), primary_key=False)
    add_info = db.Column(db.String(255), primary_key=False)
    responsible_name = db.Column(db.String(255), primary_key=False)
    responsible_email = db.Column(db.String(100), primary_key=False)
    responsible_phone = db.Column(db.String(20), primary_key=False)
    active = db.Column(db.Boolean, primary_key=False, default=True)

    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @staticmethod
    def get(id :int):
        return ProviderModel.query.filter_by(id=id).first()

    @staticmethod
    def get_by_email(responsible_email):
        return ProviderModel.query.filter_by(responsible_email=responsible_email).first()

    @staticmethod
    def get_by_cnpj(cnpj):
        return ProviderModel.query.filter_by(cnpj=cnpj).first()

    @staticmethod
    def list():
        return ProviderModel.query.all()

    @staticmethod
    def authenticate(email, password):
        user = ProviderModel.query.filter_by(email=email).first()
        if user:
            if sha256.verify(password, user.password):
                return user

        return None

    def save(self):
        self.created_at = datetime.now()
        db.session.merge(self)
        db.session.commit()


    def update(self):
        self.updated_at = datetime.now()
        db.session.merge(self)
        db.session.commit()

    @staticmethod
    def delete(id :int):
        ProviderModel.query.filter_by(id=id).delete()
        db.session.commit()
