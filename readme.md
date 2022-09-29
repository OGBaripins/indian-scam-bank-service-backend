Required Python packages and their use in the back-end of this project:
- Flask - Web application framework
- Flask _restful - Creates restful API connectivity 
- Flask_cors - Used to make the website available on all browsers 
- Requests  - Sending HTTP requests
- Mysql-connector-python - Access MySQL databases
- PyYaml - Config file creation 
- Simplejson - Json encoding and decoding 

**Transactions endpoints:**

**GET** /transactions - returns full transactions table from database

**POST** /transactions/ - endpoint used to insert values into database, arguments:
1. account_id, type=int, required=True
2. receiver_name, type=str, required=True 
3. receiver_account_number, type=str, required=True 
4. amount, type=float, required=True 
5. details, type=str, required=False 
6. transaction_date, type=str, required=True


**GET** /transactions_by_acc_id/ - returns single transaction from database, arguments : 
1. account_id, type=int, required=True

**DELETE** /transactions_acc_id/ - deletes single transaction from database, arguments :
1. transaction_id, type=int, required=True

**Accounts endpoints:**

**GET** /accounts - returns full accounts table from database

**POST** /accounts/ - endpoint used to insert values into database, arguments:
1. credential_id, type=int, required=True
2. first_name, type=str, required=True 
3. last_name, type=str, required=True 
4. social_security_number, type=str, required=True 
5. account_number, type=str, required=True 
6. account_status", type=str, required=True 
7. balance, required=True

**POST** /accounts/ - returns single transaction from database, arguments :
1. account_id, type=int, required=True

**DELETE** /accounts/ - deletes single transaction from database, arguments :
1. account_id, type=int, required=True

**GET** /accounts_nr/ - returns balance of single account, arguments:
1. account_number, type=int, required=True

***Administrative /accounts/ endpoints***

**PATCH** /accounts/ - called during insertion in the transactions table, to update balances of accounts, arguments:
1. balance, type=float, required=True
2. id, type=int, required=True



**Credentials endpoints:**

**GET** /credentials - returns full credentials table from database

**GET** /credentials/ - returns single credentials row from database, arguments:
1. credentials_id, type=int, required=True

**Validation endpoints:**

**GET** /validation/ - returns single account from accounts database, validating login








