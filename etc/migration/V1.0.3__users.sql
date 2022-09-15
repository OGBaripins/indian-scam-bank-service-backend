use banking;

DROP USER IF EXISTS 'admin'@'localhost';
DROP USER IF EXISTS 'user'@'localhost';

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

GRANT ALL PRIVILEGES ON banking.accounts TO 'admin'@'localhost';
GRANT ALL PRIVILEGES ON banking.credentials TO 'admin'@'localhost';
GRANT ALL PRIVILEGES ON banking.transactions TO 'admin'@'localhost';

CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';

GRANT UPDATE, SELECT ON banking.accounts TO 'user'@'localhost';
GRANT UPDATE ON banking.credentials TO 'user'@'localhost';
GRANT CREATE, SELECT ON banking.transactions TO 'user'@'localhost';