from datetime import datetime
import simplejson as json
from flask import Flask
from flask_restful import Api, Resource
import etc.helpers as helpers
import db_queries

app = Flask(__name__)
api = Api(app)


class Accounts(Resource):

    def get(self):
        return helpers.convert_to_json(db_queries.get_accounts())

    def post(self):
        pass

    def update(self):
        pass


class Credentials(Resource):

    def get(self):
        return helpers.convert_to_json(db_queries.get_credentials())

    def post(self):
        pass

    def update(self):
        pass


class Transactions(Resource):

    def get(self):
        return helpers.convert_to_json(db_queries.get_transactions())

    def post(self):
        pass

    def update(self):
        pass


api.add_resource(Credentials, "/credentials")
api.add_resource(Transactions, "/transactions")
api.add_resource(Accounts, "/accounts")

if __name__ == "__main__":
    app.run(debug=True)
