# atm-simulator/test_atm_simulator.py
import pytest
from atm_simulator import Auth, User, Account, Bank, Transaction, InsufficientFundsError

# Auth test cases start
def test_validate_credentials_if_credentials_empty(capsys: pytest.CaptureFixture[str]):
    
    user_auth=Auth("","") 
    invalid=user_auth.validate_credentials()
    
    captured = capsys.readouterr()
    assert "Username and pin are required." in captured.out
    assert invalid is False

def test_validate_credentials_if_only_username_empty(capsys: pytest.CaptureFixture[str]):
    
    user_auth=Auth("","1234") 
    invalid=user_auth.validate_credentials()
    
    captured = capsys.readouterr()
    assert "Username and pin are required." in captured.out
    assert invalid is False

def test_validate_credentials_if_only_pin_empty(capsys: pytest.CaptureFixture[str]):
    
    user_auth=Auth("amir","") 
    invalid=user_auth.validate_credentials()
    
    captured = capsys.readouterr()
    assert "Username and pin are required." in captured.out
    assert invalid is False

def test_validate_credentials_if_pin_len_5(capsys: pytest.CaptureFixture[str]):
    
    user_auth=Auth("amir","13245") 
    invalid=user_auth.validate_credentials()
    
    captured = capsys.readouterr()
    assert "Pin should be 4 digits long." in captured.out
    assert invalid is False

def test_validate_credentials_if_pin_len_3(capsys: pytest.CaptureFixture[str]):
    
    user_auth=Auth("amir","132") 
    invalid=user_auth.validate_credentials()
    
    captured = capsys.readouterr()
    assert "Pin should be 4 digits long." in captured.out
    assert invalid is False
    
def test_validate_credentials_if_pin_not_int_only(capsys: pytest.CaptureFixture[str]):
    
    user_auth=Auth("amir","132a") 
    invalid=user_auth.validate_credentials()
    
    captured = capsys.readouterr()
    assert "Pin Should be numbers only." in captured.out
    assert invalid is False

def test_validate_credentials_if_credentials_valid():
    
    user_auth1=Auth("amir","1324") 
    valid=user_auth1.validate_credentials()

    assert valid is True

def test_get_user():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)
    
    user_auth=Auth("amir","1122") 
    user=user_auth.get_user(bank.users)
    
    assert user is not None
    assert user.user_id == 1
    assert user.username == 'amir'
    assert user.pin == '1122'
    assert user.fname == 'Amir'
    assert user.lname == 'Zeb'

def test_get_user_return_none():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)
    
    user_auth=Auth("amir","1123") 
    user=user_auth.get_user(bank.users)
    
    assert user is None
    
def test_successful_login_user(capsys: pytest.CaptureFixture[str]):
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)
    
    user_auth=Auth("amir","1122") 
    user=user_auth.login_user(bank.users)
    
    assert user is not None
    assert user.user_id == 1
    assert user.username == 'amir'
    assert user.pin == '1122'
    assert user.fname == 'Amir'
    assert user.lname == 'Zeb'
    
    captured = capsys.readouterr()
    assert "Login Successful." in captured.out

def test_fail_login_user(capsys: pytest.CaptureFixture[str]):
    bank = Bank()
    user1 = User(1, "amir", "1123", "Amir", "Zeb")
    bank.add_user(user1)
    
    user_auth=Auth("amir","1122") 
    user=user_auth.login_user(bank.users)
    assert user is None
    
    captured = capsys.readouterr()
    assert "Invalid credentials. Try again." in captured.out
# Auth test cases ends

# Bank test cases start
def test_add_user():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)

    assert bank.users[0].user_id==1
    assert bank.users[0].username=='amir'
    assert bank.users[0].pin=='1122'
    assert bank.users[0].fname=='Amir'
    assert bank.users[0].lname=="Zeb"

def test_add_account():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)
    account1 = Account(1, user1, 100)
    bank.add_account(account1)

    assert bank.accounts[0].account_id==1
    assert bank.accounts[0].balance==100
    assert bank.accounts[0].owner.user_id==1
    
def test_find_user_for_correct_username_and_pin():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)

    user = bank.find_user('amir','1122')
    assert user.user_id==1
    assert user.username=='amir'
    assert user.pin=='1122'
    assert user.fname=='Amir'
    assert user.lname=="Zeb"

def test_find_user_for_wrong_username_and_pin():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)

    user = bank.find_user('amir','1123')
    assert user is None
    
def test_find_account_for_user_returns_correct_account():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    user2 = User(2, "ali", "4455", "ali", "khan")
    bank.add_user(user1)
    bank.add_user(user2)
    account1 = Account(1, user1, 100)
    account2 = Account(2, user2, 50)
    bank.add_account(account1)
    bank.add_account(account2)

    result = bank.find_account_for_user(user2)
    assert result is account2

def test_find_account_for_user_returns_none():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    bank.add_user(user1)

    result = bank.find_account_for_user(user1)
    assert result is None

def test_record_transaction():
    bank = Bank()
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    account1 = Account(1, user1, 100)
    bank.add_user(user1)
    bank.add_account(account1)

    tx = account1.withdraw(10)
    bank.record_transaction(tx)
    
    assert bank.transaction[0].account.account_id==account1.account_id 
    assert bank.transaction[0].tx_type=='withdraw'
    assert bank.transaction[0].amount== 10
    assert bank.transaction[0].balance_after==90.0 
# Bank test cases end

# Account test cases start
def test_withdraw_reduces_balance_and_returns_transaction():
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    account1 = Account(1, user1, 100)

    tx = account1.withdraw(10)

    assert account1.balance == 90
    assert tx.amount == 10
    assert tx.tx_type == "withdraw"
    
def test_withdraw_raises_insufficient_funds_when_over_balance():
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    account1 = Account(1, user1, 100)

    with pytest.raises(InsufficientFundsError):
        account1.withdraw(150)


def test_withdraw_raises_value_error_on_negative_amount():
    user1 = User(1, "amir", "1122", "Amir", "Zeb")
    account1 = Account(1, user1, 100)

    with pytest.raises(ValueError):
        account1.withdraw(-10)
    
def test_balance_inquiry_prints_correct_amount(capsys: pytest.CaptureFixture[str]):
    user = User(1, "amir", "1122", "Amir", "Zeb")
    account = Account(1, user, 100)
    
    account.balance_inquiry("RS")
    
    captured = capsys.readouterr()
    assert "RS100" in captured.out
# Account test cases end
    