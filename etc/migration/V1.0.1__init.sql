use banking;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS credentials;

  CREATE TABLE credentials (
  credential_id bigint(20) NOT NULL AUTO_INCREMENT,
  account_password varchar(45) NOT NULL,
  pin_1 varchar(45) NOT NULL,
  pin_2 varchar(45) NOT NULL,
  PRIMARY KEY (credential_id)
);

CREATE TABLE accounts (
  account_id bigint(20) NOT NULL AUTO_INCREMENT,
  credential_id bigint(20) NOT NULL,
  first_name varchar(45) NOT NULL,
  last_name varchar(45) NOT NULL,
  social_security_number varchar(45) NOT NULL,
  account_number varchar(45) NOT NULL,
  account_status varchar(45) NOT NULL,
  balance decimal(15,2) DEFAULT 0.00,
  PRIMARY KEY (account_id),
  CONSTRAINT FK_credential_id FOREIGN KEY (credential_id)
  REFERENCES credentials(credential_id)
  );

CREATE TABLE transactions (
  transaction_id bigint(20) NOT NULL AUTO_INCREMENT,
  account_id bigint(20) NOT NULL ,
  reciver_name varchar(45) NOT NULL,
  reciver_account_number varchar(45) NOT NULL,
  amount decimal(15,2) NOT NULL,
  transaction_date datetime NOT NULL,
  PRIMARY KEY (transaction_id),
  CONSTRAINT FK_account_id FOREIGN KEY (account_id)
  REFERENCES accounts(account_id)
);

