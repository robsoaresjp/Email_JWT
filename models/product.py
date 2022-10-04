from datetime import datetime
from models import db
from models.provider import ProviderModel
from passlib.hash import pbkdf2_sha256 as sha256

class ProductModel(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable=True)
    id_provider = db.Column(db.ForeignKey("provider.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    available = db.Column(db.Boolean, nullable=False, default=True)

    provider = db.relationship(ProviderModel)

    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @staticmethod
    def get(id :int):
        return ProductModel.query.filter_by(id=id).first()

    @staticmethod
    def list_by_provider(id_provider :int):
        return ProductModel.query.filter_by(id_provider=id_provider).all()

    @staticmethod
    def list():
        return ProductModel.query.all()

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
        ProductModel.query.filter_by(id=id).delete()
        db.session.commit()
