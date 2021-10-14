from flask_restful import Resource 
from ..models  import db, User, UserSchema
from flask import request
from flask_jwt_extended import jwt_required, create_access_token

user_schema = UserSchema()


class ViewSignUpUser(Resource):

    def post(self):
        if request.json['password1'] != request.json['password2']:
            return "Not acceptable", 406
        else: 
            new_user = User(username=request.json['username'], password=request.json['password1'],
            email=request.json['email'])
            db.session.add(new_user)
            db.session.commit()
            access_token = create_access_token(identity = new_user.id)

            return {"mensaje":"usuario creado exitosamente", "token": access_token}



class ViewLogInUser(Resource):
    def post(self):
        user = User.query.filter(User.username == request.json["username"], User.password == request.json["password"]).first()
        db.session.commit()
        if user is None:
            return "El vendedor no existe", 404
        else:
            access_token = create_access_token(identity = user.id)
            return {"mensaje":"Inicio de sesión exitoso", "token": access_token}


        