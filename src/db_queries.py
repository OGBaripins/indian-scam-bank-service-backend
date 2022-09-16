import mysql.connector


def con():
    try:
        mydb = mysql.connector.connect(
            host="sql11.freesqldatabase.com",
            port="3306",
            user="sql11520035",
            password="WjRaAgGLiL",
            database="sql11520035"
        )
    except:
        print("Connection to database was unsuccessful")
    return mydb


# Methods of queries and executions
def get_accounts():
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
        print("Couldn't retrieve information for Transactions table\n", err)

    finally:
        return data


def get_transactionsById(var):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT account_id, amount, reciver_account_number, reciver_name, transaction_date, transaction_id " \
               "FROM transactions WHERE transaction_id like %s"
    try:
        cur.execute(sql_post, tuple(var))
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)

    finally:
        return data


def get_transactionsByReceiverName(var):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT account_id, amount, reciver_account_number, reciver_name, transaction_date, transaction_id " \
               "FROM transactions WHERE reciver_name like %s"
    try:
        cur.execute(sql_post, tuple(var))
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)

    finally:
        return data


def get_transactionsByAccNumber(var):
    mydb = con()
    cur = mydb.cursor(buffered=True, dictionary=True)
    sql_post = "SELECT account_id, amount, reciver_account_number, reciver_name, transaction_date, transaction_id " \
               "FROM transactions WHERE reciver_account_number like %s"
    try:
        cur.execute(sql_post, tuple(var))
        data = cur.fetchall()
        cur.close()
        mydb.close()
    except mysql.connector.Error as err:
        print("Couldn't retrieve information for Transactions table\n", err)

    finally:
        return data
