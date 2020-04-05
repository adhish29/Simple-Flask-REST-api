from flask_restful import reqparse, Resource
from models.user import UserModel
import sqlite3


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="this field can't be blank!!!"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="this field can't be blank!!!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message' : 'Username already taken!!!'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message" : "user registered successfully"}, 201
