from datetime import datetime

import simplejson as json
from decimal import Decimal

from flask import Flask
from flask_restful import Api, Resource

import db_queries

app = Flask(__name__)
api = Api(app)


def convert_to_json(data):
    data = json.dumps(data, use_decimal=True, default=myconverter)
    return json.loads(str(data).replace("'", '"'))


def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()


class Accounts(Resource):

    def get(self):
        return convert_to_json(db_queries.get_accounts())

    def post(self):
        pass

    def update(self):
        pass


class Credentials(Resource):

    def get(self):
        return convert_to_json(db_queries.get_credentials())

    def post(self):
        pass

    def update(self):
        pass


class Transactions(Resource):

    def get(self):
        return convert_to_json(db_queries.get_transactions())

    def post(self):
        pass

    def update(self):
        pass


class TransactionsById(Resource):

    def get(self, trid="newId"):
        return {convert_to_json(db_queries.get_transactionsById(var=trid))}

    def post(self):
        pass

    def update(self):
        pass


class TransactionsByReceiverName(Resource):

    def get(self):
        return convert_to_json(db_queries.get_transactionsByReceiverName())

    def post(self):
        pass

    def update(self):
        pass


class TransactionsByAccNumber(Resource):

    def get(self):
        return convert_to_json(db_queries.get_transactionsByAccNumber())

    def post(self):
        pass

    def update(self):
        pass


api.add_resource(Credentials, "/credentials")
api.add_resource(Transactions, "/transactions")
api.add_resource(TransactionsById, "/transactions/transactionsById/<string:trId>")
api.add_resource(TransactionsByReceiverName, "/transactions/transactionsByReceiverName")
api.add_resource(TransactionsByAccNumber, "/transactions/transactionsByAccNumber")
api.add_resource(Accounts, "/accounts")

if __name__ == "__main__":
    app.run(debug=True)
