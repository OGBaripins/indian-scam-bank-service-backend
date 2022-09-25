import mysql.connector
import etc.helpers as helpers

def con():
    conf = helpers.create_conf("../etc/conf.yaml", "DATABASE_CON")

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


def get_account(account_id):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = ("SELECT account_id, credential_id, first_name, last_name, social_security_number, "
                "account_number, account_status, balance FROM accounts WHERE account_id = %s")
    try:
        cur.execute(sql_post, tuple(account_id))
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Accounts table\n", err)

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
    sql_post = "DELETE FROM credentials WHERE account_id = %s"
    try:
        cur.execute(sql_post, tuple(account_id))
        mydb.commit()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)
        return {"error": f"Deletion was unsuccessful for credential object -> id = {account_id}"}

    finally:
        return {"data": f"Deletion was successful for credential object -> id = {account_id}"}


def get_credentials():
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT credential_id, account_password, pin_1, pin_2 FROM credentials"
    try:
        cur.execute(sql_post)
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)

    finally:
        return data


def get_transactions():
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT account_id, amount, reciver_account_number, reciver_name, transaction_date, transaction_id " \
               "FROM transactions"
    try:
        cur.execute(sql_post)
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Credentials table\n", err)

    finally:
        return data
