# Logic rút tiền
from .db import get_connection
import decimal

def withdraw(card_no, amount):
    conn = get_connection()
    cur = conn.cursor()
    try:
        conn.start_transaction()
        cur.execute("SELECT account_id, balance FROM accounts JOIN cards USING(account_id) WHERE card_no=%s FOR UPDATE", (card_no,))
        result = cur.fetchone()
        if not result:
            raise Exception("Card not found")
        account_id, balance = result
        amount_decimal = decimal.Decimal(str(amount))
        if balance < amount_decimal:
            raise Exception("Insufficient funds")
        cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s", (amount_decimal, account_id))
        cur.execute("INSERT INTO transactions(account_id,card_no,atm_id,tx_type,amount,balance_after) VALUES(%s,%s,1,'WITHDRAW',%s,%s)", (account_id, card_no, amount_decimal, balance-amount_decimal))
        conn.commit()
        print("Withdraw success")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        conn.close()
