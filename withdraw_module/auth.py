# Xác thực PIN
import hashlib
from .db import get_connection

def verify_pin(card_no, pin):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    return row and row[0] == hashlib.sha256(pin.encode()).hexdigest()
