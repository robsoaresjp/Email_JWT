from datetime import datetime
from models import db
from models.user import UserModel
from passlib.hash import pbkdf2_sha256 as sha256

class OrderModel(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)

    id_user = db.Column(db.ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    products = db.Column(db.String(255), primary_key=False)
    status = db.Column(db.Integer, primary_key=False)

    user = db.relationship(UserModel)

    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    @staticmethod
    def get(id :int):
        return OrderModel.query.filter_by(id=id).first()

    @staticmethod
    def list_by_user(id_user :int):
        return OrderModel.query.filter_by(id_user=id_user).all()

    @staticmethod
    def list_by_status(status :int):
        return OrderModel.query.filter_by(status=status).all()

    @staticmethod
    def list():
        return OrderModel.query.all()

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
        OrderModel.query.filter_by(id=id).delete()
        db.session.commit()
