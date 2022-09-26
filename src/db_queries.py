import mysql.connector
import helpers as helpers


def con():
    conf = helpers.create_conf("./etc/conf.yaml", "DATABASE_CON")

    try:
        mydb = mysql.connector.connect(
            host=conf.get("HOST"),
            port=conf.get("PORT"),
            user=conf.get("USER"),
            password=conf.get("PASSWORD"),
            database=conf.get("DATABASE")
        )
    except mysql.connector.Error as err:
        print(f"Connection to database was unsuccessful\nErr: {err}")
    return mydb


# Methods of queries and executions
def get_all_accounts():
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = ("SELECT account_id, credential_id, first_name, last_name, social_security_number, "
                "account_number, account_status, balance FROM accounts")
    try:
        cur.execute(sql_post)
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Accounts table\n", err)

    finally:
        return data


def get_account_by_id(account_id):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = ("SELECT account_id, credential_id, first_name, last_name, social_security_number, "
                "account_number, account_status, balance FROM accounts WHERE account_id = %s")
    try:
        cur.execute(sql_post, tuple(account_id))
        data = cur.fetchall()
        print(len(data))
        if len(data) == 0:
            raise mysql.connector.Error
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        data = {"error": f"Data retrieval was unsuccessful for credential object -> id {account_id}"}

    finally:
        return data


def post_accounts(values):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = ("INSERT INTO accounts (credential_id, first_name, last_name, social_security_number, "
                "account_number, account_status, balance) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    try:
        cur.execute(sql_post, tuple(values))
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't insert data into Accounts table\n", err)
        return {"error": f"Insert was unsuccessful -> values {values}"}

    finally:
        return {"data": "Insert was successful"}


def delete_account(account_id):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "DELETE FROM accounts WHERE account_id = %s"
    try:
        cur.execute(sql_post, tuple(account_id))
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Accounts table\n", err)
        return {"error": f"Deletion was unsuccessful for account object -> id = {account_id}"}

    finally:
        return {"data": f"Deletion was successful for account object -> id = {account_id}"}


def get_credentials():
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT credential_id, account_password FROM credentials"
    try:
        cur.execute(sql_post)
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        return {"error": "Data retrieval was unsuccessful for credential objects"}

    finally:
        return data


def get_single_credential(cred_id):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT credential_id, account_password FROM credentials WHERE credential_id = %s"
    try:
        cur.execute(sql_post, tuple(cred_id))
        data = cur.fetchall()
        print(len(data))
        if len(data) == 0:
            print("yes")
            raise mysql.connector.Error
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        data = {"error": f"Data retrieval was unsuccessful for credential object -> id {cred_id}"}

    finally:
        return data


def add_credentials(values):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = ("INSERT INTO credentials (account_password)"
                "VALUES(%s)")
    try:
        cur.execute(sql_post, tuple(values))
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        return {"error": f"Insert was unsuccessful -> values {values}"}

    finally:
        return {"data": "Insert was successful"}


def delete_credentials(values):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "DELETE FROM credentials WHERE credential_id = %s"
    try:
        cur.execute(sql_post, tuple(values))
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        return {"error": f"Deletion was unsuccessful for credential object -> id = {values}"}

    finally:
        return {"data": f"Deletion was successful for credential object -> id = {values}"}


def get_transactions():
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)

    sql_post = "SELECT account_id, amount, receiver_account_number, receiver_name, details, transaction_date, " \
               "transaction_id " \
               "FROM transactions"
    try:
        cur.execute(sql_post)
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)


    finally:
        return data


def get_transactions_by_id(var):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT account_id, amount, receiver_account_number, receiver_name, transaction_date, transaction_id " \
               "FROM transactions WHERE transaction_id = %s"
    try:
        cur.execute(sql_post, tuple(var))
        data = cur.fetchall()
        cur.close()
        mydb.close()

    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)
        data = {"error": f"data retrieval unsuccessful for passed transaction ID", "passedArg": var}


    finally:
        return data


def get_transactions_by_acc_id(var):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT account_id, amount, receiver_account_number, receiver_name, transaction_date, transaction_id " \
               "FROM transactions WHERE account_id = %s"
    try:
        cur.execute(sql_post, tuple(var))
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)
        data = {"error": f"data retrieval unsuccessful for passed account number", "passedArg": var}

    finally:
        return data


def insert_transaction(values):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "INSERT into Transactions(account_id, amount, " \
               "receiver_account_number, receiver_name, transaction_date, transaction_id " \
               "VALUES %s, %s, %s, %s, %s, %s"

    try:
        cur.execute(sql_post, tuple(values))
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)
        data = {"error": f"transaction not added due to error VALUES = {values}"}

    finally:
        return {"data": "Transaction successfully inserted"}


def validation():
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT credentials.account_password, accounts.social_security_number, accounts.account_id FROM " \
               "accounts RIGHT JOIN " \
               "credentials ON credentials.credential_id=accounts.credential_id"
    try:
        cur.execute(sql_post)
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        pass
    finally:
        return data
