from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql import func 
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200))

    def __repr__(self):
        return "{} - {}".format(self.username, self.password)

class UserSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = User
        include_relationships = True 
        load_instance = True 

