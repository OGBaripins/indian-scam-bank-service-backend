import mysql.connector
import helpers as helpers


def con():
    try:
        conf = helpers.create_conf("../etc/conf.yaml", "DATABASE_CON")
    except FileNotFoundError:
        conf = helpers.create_conf("./etc/conf.yaml", "DATABASE_CON")

    try:
        mydb = mysql.connector.connect(
            host=conf.get("HOST"),
            port=conf.get("PORT"),
            user=conf.get("USER"),
            password=conf.get("PASSWORD"),
            database=conf.get("DATABASE")
        )
    except Exception as err:
        print(f"Connection to database was unsuccessful\nErr: {err}")
        return {"err": "Cant connect to the database"}
    return mydb


con()


# Methods of queries and executions
def get_accounts():
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message

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
        data = {"error": "Data retrieval was unsuccessful for account objects"}

    return data


def get_account_by_id(account_id):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = ("SELECT account_id, credential_id, first_name, last_name, social_security_number, "
                "account_number, account_status, balance FROM accounts WHERE account_id = %s")
    try:
        cur.execute(sql_post, tuple(account_id))
        data = cur.fetchall()
        if len(data) == 0:
            raise mysql.connector.Error
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        data = {"error": f"Data retrieval was unsuccessful for account object -> id {account_id}"}

    return data


def add_accounts(values):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
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
        return {"error": f"Insert was unsuccessful for account object -> values {values}"}

    finally:
        return {"data": "Insert was successful"}


def delete_account(account_id):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message

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
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT credential_id, account_password FROM credentials"
    try:
        cur.execute(sql_post)
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        data = {"error": "Data retrieval was unsuccessful for credential objects"}

    finally:
        return data


def get_single_credential_by_id(cred_id):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT credential_id, account_password FROM credentials WHERE credential_id = %s"
    try:
        cur.execute(sql_post, tuple(cred_id))
        data = cur.fetchall()
        if len(data) == 0:
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
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
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
        return {"error": "Insert was unsuccessful for credential object"}

    finally:
        return {"data": "Insert was successful"}


def delete_credentials(values):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
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
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
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
        data = {"error": "Data retrieval was unsuccessful for transaction objects"}
    finally:
        return data


def get_single_transaction_by_id(var):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
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
        data = {"error": f"Data retrieval unsuccessful for transaction object, values -> {var}"}

    finally:
        return data


def get_single_transactions_by_acc_id(var):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
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
        data = {"error": f"Data retrieval unsuccessful for transaction object, values -> {var}"}

    finally:
        return data


def get_account_balance_from_acc_nr(arg):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
    cur = mydb.cursor(buffered=True, dictionary=True)
    try:
        cur.execute(f"SELECT balance FROM accounts WHERE account_number = '{arg}'")
        data = cur.fetchall()
        if len(data) == 0:
            raise mysql.connector.Error
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for accounts table\n", err)
        data = {"error": f"Data retrieval was unsuccessful for accounts object, account_id -> {arg}"}

    finally:
        return data


def delete_transaction(values):
    data = {"data": f"Deletion successful for -> id = {values}"}
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message

    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "DELETE FROM transactions WHERE transaction_id = %s"
    try:
        cur.execute(sql_post, tuple(values))
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)
        data = {"error": f"Deletion was unsuccessful for transactions object -> id = {values}"}
        return data

    finally:
        return data


def add_transactions(values):
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "INSERT INTO transactions (account_id, amount, details, receiver_name, receiver_account_number,  " \
               "transaction_date)" \
               "VALUES (%s, %s, %s, %s, %s, %s)"
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


def patch_balance(identifier, value):
    is_account_number = False
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
    cur = mydb.cursor(buffered=True, dictionary=True)
    if identifier.lower().startswith('isbs'):
        is_account_number = True
        identifier = f"'{identifier}'"
    sql_post = f"UPDATE accounts SET balance = {'%.2f' % value} " \
               f"WHERE {'account_number' if is_account_number else 'account_id'}={identifier}"
    try:
        cur.execute(sql_post)
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Balance Update was unsuccessful\n", err)
        return {"error": f"Balance Update was unsuccessful for account with identifier -> {identifier}"}

    finally:
        return {"data": "Insert was successful"}


def validation():
    mydb = con()
    if isinstance(mydb, dict):
        return mydb  # <- In here is an error message
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
        print("Validation was unsuccessful\n", err)
        data = {"error": f"Credentials checking was unsuccessful"}
    finally:
        return data


if __name__ == "__main__":
    pass
