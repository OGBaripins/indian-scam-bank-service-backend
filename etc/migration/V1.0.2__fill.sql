use banking;

insert into credentials (credential_id, account_password, pin_1, pin_2) values (1, 'password1', '1111', '11111');
insert into credentials (credential_id, account_password, pin_1, pin_2) values (2, 'password2', '2222', '22222');
insert into credentials (credential_id, account_password, pin_1, pin_2) values (3, 'password3', '3333', '33333');
insert into credentials (credential_id, account_password, pin_1, pin_2) values (4, 'password4', '4444', '44444');

INSERT INTO accounts (account_id, credential_id, first_name, last_name, social_security_number, account_number, account_status, balance) 
VALUES (1, 1, 'Top', 'G', '010101-11111', 'ISBS1111111111','Active',1000000.00);
INSERT INTO accounts (account_id, credential_id, first_name, last_name, social_security_number, account_number, account_status, balance) 
VALUES (2, 2, 'Bottom', 'G', '020202-22222', 'ISBS2222222222','Active',10.00);
INSERT INTO accounts (account_id, credential_id, first_name, last_name, social_security_number, account_number, account_status, balance) 
VALUES (3, 3, 'Hacker', 'G', '030303-33333', 'ISBS3333333333','Blocked',6969696969.00);
INSERT INTO accounts (account_id, credential_id, first_name, last_name, social_security_number, account_number, account_status, balance) 
VALUES (4, 4, 'Steal', 'Inc.', '040404-44444', 'ISBS4444444444','Active',10000.00);

insert into transactions (transaction_id, account_id, reciver_name, reciver_account_number, amount, transaction_date) 
values (1, 1, 'Steal Inc.', 'ISBS4444444444', 100.00, '2022-09-11');
insert into transactions (transaction_id, account_id, reciver_name, reciver_account_number, amount, transaction_date) 
values (2, 1, 'Steal Inc.', 'ISBS4444444444', 4500.00, '2022-09-11');
insert into transactions (transaction_id, account_id, reciver_name, reciver_account_number, amount, transaction_date) 
values (3, 2, 'Steal Inc.', 'ISBS4444444444', 5.00, '2022-09-11');
