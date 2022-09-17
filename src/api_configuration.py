from flask import Flask
from flask_restful import Api, Resource, reqparse
import etc.helpers as helpers
import db_queries as queries

app = Flask(__name__)
api = Api(app)


class Accounts(Resource):

    def get(self):
        return helpers.convert_to_json(queries.get_accounts())

    def post(self):
        pass

    def update(self):
        pass


class Credentials(Resource):
    cred_reqparse: reqparse = reqparse.RequestParser()
    cred_reqparse.add_argument("credential_id", type=int, help="ERR: credential_id is a required field", required=True)
    cred_reqparse.add_argument("account_password", type=str, help="ERR: account_password is a required field",
                               required=True)
    cred_reqparse.add_argument("pin_1", type=str, help="ERR: pin_1 is a required field", required=True)
    cred_reqparse.add_argument("pin_2", type=str, help="ERR: pin_2 is a required field", required=True)

    def get(self):
        return helpers.convert_to_json(queries.get_all_credentials())

    def post(self):
        body = self.cred_reqparse.parse_args()
        return queries.add_credentials(helpers.from_json_to_tuple(helpers.convert_to_json(body)))


class Single_credential(Resource):

    def get(self, cred_id):
        print(helpers.convert_to_json(queries.get_single_credential(cred_id)))
        return helpers.convert_to_json(queries.get_single_credential(cred_id))

    def delete(self, cred_id):
        return helpers.convert_to_json(queries.delete_credentials(cred_id))


class Transactions(Resource):

    def get(self):
        return helpers.convert_to_json(queries.get_transactions())

    def post(self):
        pass

    def update(self):
        pass


api.add_resource(Credentials, "/credentials")
api.add_resource(Transactions, "/transactions")
api.add_resource(Single_credential, "/credentials/<string:cred_id>")
api.add_resource(Accounts, "/accounts")

if __name__ == "__main__":
    app.run(debug=True)
