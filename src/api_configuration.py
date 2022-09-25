from datetime import datetime
import simplejson as json
from decimal import Decimal

from flask import Flask
from flask_restful import Api, Resource, reqparse

import etc.helpers as helpers
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
    trans_reqparse: reqparse = reqparse.RequestParser()
    trans_reqparse.add_argument("acc_id", type=int, help="ERR: account_id is a required field", required=True)
    trans_reqparse.add_argument("cred_id", type=int, help="ERR: credential_id is a required field", required=True)
    trans_reqparse.add_argument("first_name", type=str, help="ERR: first name is a required field", required=True)
    trans_reqparse.add_argument("last_name", type=str, help="ERR: last name is a required field", required=True)
    trans_reqparse.add_argument("ssn", type=int, help="ERR: security number is a required field", required=True)
    trans_reqparse.add_argument("acc_nr", type=int, help="ERR: account number is a required field", required=True)

    def get(self):
        return convert_to_json(queries.get_transactions())

    def post(self):
        body = self.trans_reqparse.parse_args()
        return queries.insert_transactions(helpers.from_json_to_tuple(helpers.convert_to_json(body)))

    def update(self):
        pass


class TransactionsByID(Resource):

    def get(self, trans_id):
        return convert_to_json(db_queries.get_transactions_by_id(trans_id))

    def post(self):
        body = self.cred_reqparse.parse_args()
        return queries.add_credentials(helpers.from_json_to_tuple(helpers.convert_to_json(body)))

    def update(self):
        pass


class TransactionsByAccNumber(Resource):

    def get(self, acc_id):
        return convert_to_json(db_queries.get_transactions_by_acc_id(acc_id))

    def post(self):
        pass

    def update(self):
        pass


api.add_resource(Credentials, "/credentials")
api.add_resource(Transactions, "/transactions")
api.add_resource(TransactionsByID, "/transactions/TransactionsByID/<string:trans_id>")
api.add_resource(TransactionsByAccNumber, "/transactions/TransactionsByAccID/<string:acc_id>")
api.add_resource(Accounts, "/accounts")

if __name__ == "__main__":
    app.run(debug=True)
