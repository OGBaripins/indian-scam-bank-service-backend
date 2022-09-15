import json

from flask import Flask
from flask_restful import Api, Resource
import db_queries

app = Flask(__name__)
api = Api(app)


class Accounts(Resource):

    def get(self):
        return json.dumps({'data': db_queries.get_accounts()})

    def post(self):
        pass

    def update(self):
        pass


class Credentials(Resource):

    def get(self):
        return json.dumps({'data': db_queries.get_credentials()})

    def post(self):
        pass

    def update(self):
        pass


api.add_resource(Credentials, "/credentials")
api.add_resource(Accounts, "/accounts")
if __name__ == "__main__":
    app.run(debug=True)
