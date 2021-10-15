from flask_restful import Resource 
from ..models  import db, User, UserSchema, Task, TaskSchema, File, FileSchema
from flask import request
from flask_jwt_extended import jwt_required, create_access_token,  get_jwt_identity

user_schema = UserSchema()
task_schema = TaskSchema()
file_schema = FileSchema()


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
            return "El usuario no existe", 404
        else:
            access_token = create_access_token(identity = user.id)
            return {"mensaje":"Inicio de sesión exitoso", "token": access_token}

class ViewTasks(Resource):
    @jwt_required()
    def get(self):
        user = User.query.get_or_404(get_jwt_identity())
        return [task_schema.dump(task) for task in user.tasks]


    @jwt_required()
    def post(self): 
        new_task = Task(file_name = request.json['file_name'],
        new_format = request.json['new_format'])

        user = User.query.get_or_404(get_jwt_identity())
        user.tasks.append(new_task)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task)


class ViewTask(Resource):
    @jwt_required()
    def get(self, id_task):
        user = User.query.get_or_404(get_jwt_identity())
        task = Task.query.get_or_404(id_task)

        if(task.user_id == user.id):
            return task_schema.dump(task)
        else:
            return '', 401

    @jwt_required()
    def put(self, id_task):
        user = User.query.get_or_404(get_jwt_identity())
        task = Task.query.get_or_404(id_task)
        task.file_name = request.json.get("file_name", task.file_name)
        task.new_format = request.json.get("new_format", task.new_format)
        db.session.commit()
        return task_schema.dump(task)

    @jwt_required()
    def delete(self,id_task):
        task = Task.query.get_or_404(id_task)
        db.session.delete(task)
        db.session.commit()
        return '', 204


class ViewFile(Resource):
    @jwt_required()
    def get(self, file_name):
        user = User.query.get_or_404(get_jwt_identity())
        file = File.query.filter(File.file_name == str(file_name))

        # if(file.user_id == user.id):
        return file_schema.dump(file)
        # else:
        #     return '', 401



        