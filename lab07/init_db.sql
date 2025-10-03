-- Tạo database và các bảng cho mô phỏng ATM Withdraw
CREATE DATABASE IF NOT EXISTS atm_demo;
USE atm_demo;

-- Bảng accounts
CREATE TABLE IF NOT EXISTS accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0
);

-- Bảng cards
CREATE TABLE IF NOT EXISTS cards (
    card_no VARCHAR(32) PRIMARY KEY,
    account_id INT,
    pin_hash CHAR(64) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Bảng transactions
CREATE TABLE IF NOT EXISTS transactions (
    tx_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    card_no VARCHAR(32),
    atm_id INT,
    tx_type VARCHAR(16),
    amount DECIMAL(15,2),
    balance_after DECIMAL(15,2),
    tx_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id),
    FOREIGN KEY (card_no) REFERENCES cards(card_no)
);

-- Dữ liệu mẫu
INSERT INTO accounts(balance) VALUES (1000000);
SET @acc_id = LAST_INSERT_ID();
INSERT INTO cards(card_no, account_id, pin_hash) VALUES ('1234567890', @acc_id, SHA2('1234',256));
