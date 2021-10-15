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
    tasks = db.relationship('Task', cascade='all, delete, delete-orphan')
    files = db.relationship('File', cascade='all, delete, delete-orphan')
    

    def __repr__(self):
        return "{} - {}".format(self.username, self.password)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(200))
    new_format = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(200))
    format_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class UserSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = User
        include_relationships = True 
        load_instance = True 


class TaskSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = Task
        include_relationships = True 
        load_instance = True 

class FileSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = File
        include_relationships = True 
        load_instance = True 

