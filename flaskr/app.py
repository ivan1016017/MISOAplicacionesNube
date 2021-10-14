from flaskr import create_app
from .models import db, User, Task
from .models import UserSchema, TaskSchema
from flask_restful import Api 
from flask_cors import CORS, cross_origin
from .views import ViewSignUpUser, ViewLogInUser, ViewTasks
from flask_jwt_extended import JWTManager


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)


api = Api(app)
api.add_resource(ViewSignUpUser, '/signup')
api.add_resource(ViewLogInUser, '/login')
api.add_resource(ViewTasks, '/tasks')




jwt = JWTManager(app)

with app.app_context():
    user_schema = UserSchema()
    user_one = User(username="user1",password = "password_user1", email='email_user1')
    user_two = User(username="user2",password = "password_user1", email='email_user2')
    task_one = Task(file_name= "fileNameOne", new_format = 'xml')
    user_two.tasks.append(task_one)

    db.session.add(user_one)
    db.session.add(user_two)



    db.session.commit()