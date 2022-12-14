import time

from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

import helpers as helpers
import db_queries as queries
import requests

BASE = "http://127.0.0.1:5000/"

## WARNING =====================================================================
## FOR MODULE INSTALLATION PLEASE USE THE FOLLOWING COMMAND IN YOUR TERMINAL
## pip install -r etc/requirements.txt
## =============================================================================

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route("/")
class Accounts(Resource):
    acc_reqparse: reqparse = reqparse.RequestParser()
    acc_reqparse.add_argument("credential_id", type=int, help="ERR: credential_id is a required field", required=True)
    acc_reqparse.add_argument("first_name", type=str, help="ERR: first_name is a required field", required=True)
    acc_reqparse.add_argument("last_name", type=str, help="ERR: last_name is a required field", required=True)
    acc_reqparse.add_argument("social_security_number", type=str,
                              help="ERR: social_security_number is a required field", required=True)
    acc_reqparse.add_argument("account_number", type=str, help="ERR: account_number is a required field", required=True)
    acc_reqparse.add_argument("account_status", type=str, help="ERR: account_status is a required field", required=True)
    acc_reqparse.add_argument("balance", type=float, help="ERR: balance is a required field", required=True)

    @cross_origin()
    def get(self):
        return helpers.convert_to_json(queries.get_accounts())

    @cross_origin()
    def post(self):
        body = self.acc_reqparse.parse_args()
        return queries.add_accounts(helpers.from_json_to_tuple(helpers.convert_to_json(body)))


class Single_account(Resource):
    acc_reqparse: reqparse = reqparse.RequestParser()
    acc_reqparse.add_argument("balance", type=float, help="ERR: balance is a required field", required=True)
    acc_reqparse.add_argument("id", type=str, help="ERR: account_number is a required field", required=True)

    @cross_origin()
    def get(self, acc_id):
        return helpers.convert_to_json(queries.get_account_by_id(acc_id))

    @cross_origin()
    def delete(self, acc_id):
        return helpers.convert_to_json(queries.delete_account(acc_id))


class Patch_account(Resource):
    acc_reqparse: reqparse = reqparse.RequestParser()
    acc_reqparse.add_argument("balance", type=float, help="ERR: balance is a required field", required=True)
    acc_reqparse.add_argument("id", type=str, help="ERR: account_number is a required field", required=True)

    @cross_origin()
    def patch(self):
        body = self.acc_reqparse.parse_args()
        return helpers.convert_to_json(queries.patch_balance(body["id"], body["balance"]))


class Single_account_nr(Resource):
    @cross_origin()
    def get(self, acc_nr):
        return helpers.convert_to_json(queries.get_account_balance_from_acc_nr(acc_nr))


class Credentials(Resource):
    cred_reqparse: reqparse = reqparse.RequestParser()
    cred_reqparse.add_argument("account_password", type=str, help="ERR: account_password is a required field",
                               required=True)

    @cross_origin()
    def get(self):
        return helpers.convert_to_json(queries.get_credentials())

    @cross_origin()
    def post(self):
        body = self.cred_reqparse.parse_args()
        return queries.add_credentials(helpers.from_json_to_tuple(helpers.convert_to_json(body)))


class Single_credential(Resource):

    @cross_origin()
    def get(self, cred_id):
        return helpers.convert_to_json(queries.get_single_credential_by_id(cred_id))

    @cross_origin()
    def delete(self, cred_id):
        return helpers.convert_to_json(queries.delete_credentials(cred_id))


class Transactions(Resource):
    trans_reqparse: reqparse = reqparse.RequestParser()
    trans_reqparse.add_argument("account_id", type=int, help="ERR: account_id is a required field", required=True)
    trans_reqparse.add_argument("receiver_name", type=str, help="ERR: last name is a required field", required=True)
    trans_reqparse.add_argument("receiver_account_number", type=str,
                                help="ERR: receiver_account_number is a required field", required=True)
    trans_reqparse.add_argument("amount", type=float, help="ERR: credential_id is a required field", required=True)
    trans_reqparse.add_argument("details", type=str, help="ERR: credential_id is a required field", required=False)
    trans_reqparse.add_argument("transaction_date", type=str, help="ERR: last name is a required field", required=True)

    @cross_origin()
    def get(self):
        return helpers.convert_to_json(queries.get_transactions())

    @cross_origin()
    def post(self):
        body = self.trans_reqparse.parse_args()
        bal = requests.get(f"{BASE}accounts/{str(body.get('account_id'))}")
        if bal.json()[0].get('balance') < float(body.get("amount")):
            return {"error": f"Sender account does not have enough funds"}
        requests.patch(f"{BASE}accounts",
                       json={
                           'balance': float(bal.json()[0].get('balance')) - float(body.get("amount")),
                           'id': body.get("account_id")
                       })
        bal = requests.get(f"{BASE}accounts_nr/{body.get('receiver_account_number')}")
        requests.patch(f"{BASE}accounts",
                       json={
                           'balance': float(bal.json()[0].get('balance')) + float(body.get("amount")),
                           'id': body.get("receiver_account_number")
                       })
        return queries.add_transactions(helpers.from_json_to_tuple(helpers.convert_to_json(body)))


class TransactionsByID(Resource):

    @cross_origin()
    def get(self, trans_id):
        return helpers.convert_to_json(queries.get_single_transaction_by_id(trans_id))

    @cross_origin()
    def delete(self, trans_id):
        return helpers.convert_to_json(queries.delete_transaction(trans_id))


class TransactionsByAccNumber(Resource):

    @cross_origin()
    def get(self, acc_id):
        return helpers.convert_to_json(queries.get_single_transactions_by_acc_id(acc_id))


class Validation(Resource):
    @cross_origin()
    def get(self, sec_number, password):
        account_data = helpers.convert_to_json(queries.validation())
        if isinstance(account_data, dict) and "err" in account_data.keys():
            return account_data, 404
        acc_data = helpers.check_validation(sec_number, password, account_data)
        if "err" in acc_data.keys():
            return account_data, 404

        return helpers.convert_to_json(queries.get_account_by_id(str(acc_data.get("account_id"))))


api.add_resource(Accounts, "/accounts")
api.add_resource(Patch_account, "/accounts")
api.add_resource(Single_account, "/accounts/<string:acc_id>")
api.add_resource(Single_account_nr, "/accounts_nr/<string:acc_nr>")

api.add_resource(Credentials, "/credentials")
api.add_resource(Single_credential, "/credentials/<string:cred_id>")

api.add_resource(Transactions, "/transactions")
api.add_resource(TransactionsByID, "/transactions/<string:trans_id>")
api.add_resource(TransactionsByAccNumber, "/transactions_acc_id/<string:acc_id>")

api.add_resource(Validation, "/validation/<string:sec_number>/<string:password>")

if __name__ == "__main__":
    pass
