from flask_restful import Resource 
from ..models  import db, User, UserSchema
from flask import request
from flask_jwt_extended import jwt_required, create_access_token

user_schema = UserSchema()


class SignInUser(Resource):

    def post(self):
        new_user = User(username=request.json['username'], password=request.json['password1'],
        email=request.json['email'])
        db.session.add(new_user)
        db.session.commit()

        