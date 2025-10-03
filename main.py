from withdraw_module.auth import verify_pin
from withdraw_module.withdraw import withdraw

if __name__ == "__main__":
    card_no = input("Card number: ")
    pin = input("PIN: ")
    if verify_pin(card_no, pin):
        amount = float(input("Amount to withdraw: "))
        withdraw(card_no, amount)
    else:
        print("Invalid PIN!")
