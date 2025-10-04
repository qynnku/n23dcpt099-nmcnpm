import pytest
from atm import ATM

def test_verify_pin_correct():
    atm = ATM('1234', 1000)
    assert atm.verify_pin('1234') is True

def test_verify_pin_wrong():
    atm = ATM('1234', 1000)
    assert atm.verify_pin('0000') is False

def test_withdraw_enough_balance():
    atm = ATM('1234', 1000)
    success, msg = atm.withdraw(500)
    assert success is True
    assert atm.balance == 500
    assert msg == "Rút tiền thành công"

def test_withdraw_not_enough_balance():
    atm = ATM('1234', 1000)
    success, msg = atm.withdraw(1500)
    assert success is False
    assert atm.balance == 1000
    assert msg == "Không đủ tiền trong tài khoản"

def test_withdraw_invalid_amount():
    atm = ATM('1234', 1000)
    success, msg = atm.withdraw(-100)
    assert success is False
    assert msg == "Số tiền rút phải lớn hơn 0"
