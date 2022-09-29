## Required Python packages and their use in the back-end of this project:
- Flask - Web application framework
- Flask _restful - Creates restful API connectivity 
- Flask_cors - Used to make the website available on all browsers 
- Requests  - Sending HTTP requests
- Mysql-connector-python - Access MySQL databases
- PyYaml - Config file creation 
- Simplejson - Json encoding and decoding 

## Transactions endpoints

For every possible transaction within our API we provide a detailed overview.
- For transaction with **POST** methods we provide a structure of the request body as a **json** object template and extra information on the right side.
- For transaction with **GET** methods we provide a small description of return value. For some methods a value is required to be passed as a link attribute.
- For transaction with **PATCH** methods we provide a structure of the request body as a **json** object template.
- For transaction with **DELETE** methods we provide a structure of the request body as a **json** object template.\

**GET** /transactions - returns full transactions table from database.

**POST** /transactions - endpoint used to insert values into database.
>JSON BODY
```
{
    "account_id": 1,                             |  type=int, required=True
    "amount": 10,00,                             |  type=float, required=True
    "details": "test_details",                   |  type=str, required=False
    "receiver_account_number": "isbs3333333333", |  type=str, required=True
    "receiver_name": "Steal Inc.",               |  type=str, required=True
    "transaction_date": "2022-09-11 00:00:00"    |  type=str, required=True
}
```
\
**GET** /transactions_by_acc_id/ - returns single transaction from database.
>ENDPOINT EXAMPLE: 
```
GET localhost/transactions_by_acc_id/1
```
\
**DELETE** /transactions_acc_id/ - deletes single transaction from database.
>ENDPOINT EXAMPLE: 
```
DELETE localhost/transactions_by_acc_id/1
```

### Accounts endpoints

**GET** /accounts - returns full accounts table from database.

**POST** /accounts/ - endpoint used to insert values into database.
>JSON BODY
```
}
    credential_id: 1,                             |  type=int, required=True
    first_name: "Top",                            |  type=str, required=True 
    last_name: "G",                               |  type=str, required=True 
    social_security_number: ,                     |  type=str, required=True 
    account_number: 1,                            |  type=str, required=True 
    account_status": "active",                    |  type=str, required=True 
    balance: 100,00                               |  type=float required=True
}
```
**GET** /accounts/ - returns single transaction from database.
>ENDPOINT EXAMPLE: 
```
GET localhost/accounts/1
```

**DELETE** /accounts/ - deletes single transaction from database.
>ENDPOINT EXAMPLE: 
```
DELETE localhost/accounts/1
```

**GET** /accounts_nr/ - returns balance of single account, arguments:
>ENDPOINT EXAMPLE: 
```
GET localhost/accounts/1
```

### Administrative Accounts endpoints:

**PATCH** /accounts/ - called during insertion in the transactions table, to update balances of accounts.
>JSON BODY
```
{
balance: 100,00, type=float, required=True
id: "1" , type=str, required=True
}
```
### Credentials endpoints
\
**GET** /credentials - returns full credentials table from database.

**GET** /credentials/ - returns single credentials row from database.
>ENDPOINT EXAMPLE: 
```
GET localhost/credentials/1
```
### Validations endpoints

**GET** /validation/ - Validates login with password and social security number (1.ssc, 2.password).
>ENDPOINT EXAMPLE: 
```
GET localhost/credentials/010101-11111/password1
```








