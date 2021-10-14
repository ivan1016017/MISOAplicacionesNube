from flaskr import create_app
from .models import db, User
from .models import UserSchema
from flask_restful import Api 
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)


jwt = JWTManager(app)

with app.app_context():
    user_schema = UserSchema()


    db.session.commit()