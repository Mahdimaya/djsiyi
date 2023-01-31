from . import db
from  flask_Login import UserMixin
from sqlalchemy.sql import func


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)

class Utilisateurs(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    adresse = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)

class Panier(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'), nullable=False)
    livre_id = db.Column(db.Integer, db.ForeignKey('livres.id'), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
def create_tables():
    db.create_all()