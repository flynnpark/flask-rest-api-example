from flask import Flask
from flask_restful import Resource, Api
from database import init_db


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'success': True, 'message': 'Hello World!'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True, port=80)
