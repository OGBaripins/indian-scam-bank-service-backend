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


class TransactionsByID(Resource):

    def get(self, trans_id):
        return convert_to_json(db_queries.get_transactions_by_id(trans_id))

    def post(self):
        pass

    def update(self):
        pass


class TransactionsByAccNumber(Resource):

    def get(self, acc_id):
        return convert_to_json(db_queries.get_transactions_by_acc_id(acc_id))

    def post(self):
        pass

    def update(self):
        pass

class InsertTransaction(Resource):

    def get(self):
        pass

    def post(self, acc_id, cred_id, first_name, last_name):
        return db_queries.insert_transaction()

    def update(self):
        pass


api.add_resource(Credentials, "/credentials")
api.add_resource(Transactions, "/transactions")
api.add_resource(TransactionsByID, "/transactions/TransactionsByID/<string:trans_id>")
api.add_resource(TransactionsByAccNumber, "/transactions/TransactionsByAccID/<string:acc_id>")
api.add_resource(TransactionsByAccNumber, "/transactions/InsertTransaction/<string:acc_id>/<string:cred_id>/<string:first_name/<string:last_name/<string:ssn>/<string:acc_nr>")
api.add_resource(Accounts, "/accounts")

if __name__ == "__main__":
    app.run(debug=True)
