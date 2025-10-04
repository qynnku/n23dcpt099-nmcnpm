class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, input_pin):
        return self.pin == input_pin

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Số tiền rút phải lớn hơn 0"
        if amount > self.balance:
            return False, "Không đủ tiền trong tài khoản"
        self.balance -= amount
        return True, "Rút tiền thành công"