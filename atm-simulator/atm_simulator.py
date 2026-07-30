
MAIN_MENU={
    "w":"Withdraw cash",
    "i":"Balance Inquiry",
    "t":"Transaction history",
    "c":"Cancel",
}

# TRANSACTION_HISTORY DATA
TRANSACTION_HISTORY=[]

class User:
    def __init__(self, user_id: int, username: str, pin: str, fname: str, lname: str):
        self.user_id=user_id
        self.username=username
        self.pin=pin
        self.fname=fname
        self.lname=lname
    def __str__(self):
            return f"User({self.user_id}, {self.username}, {self.fname}, {self.lname})"

    __repr__=__str__
# user class ends

class Account:
    def __init__(self, account_id: int, owner: User, balance: float):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        
    # only withdraw
    def withdraw(self, amount: float) -> None:
        pass
    
    def balance_inquiry(self) -> None:
        pass
    
    def __str__(self):
        return f"Account({self.account_id}, {self.owner}, {self.balance})"

    __repr__=__str__
# account class ends

class Bank:
    bank_name="WORK BANK"
    
    def __init__(self):
        self.users: list[User] = []
        self.accounts: list[Account] = []
        
    def add_user(self, user: User) -> None:
        self.users.append(user)
    
    def add_account(self, account: Account) -> None:
        self.accounts.append(account)
    
    def find_user(self, username: str, pin: str):
        for u in self.users:
            if u.username == username and u.pin == pin:
                return u
        return None
    
    def find_account_for_user(self, user: User):
        for acc in self.accounts:
            if acc.owner.user_id == user.user_id:
                return acc
        return None
# bank class ends

class Auth:
    
    def __init__(self,username,pin):
        self.username=username
        self.pin=pin
    
    def validate_credentials(self):
        if self.username=='' or self.pin=='':
            print("Username and pin are required.")
            return False
        elif len(self.pin)!=4:
            print("Pin should be 4 digits long.")
            return False
        elif not(self.pin.isdigit()):
            print("Pin Should be numbers only.")
            return False
        else:
            return True
    
    def login_user(self,users):
        user=self.get_user(users)
        if user:
            print("Login Successful.")
            return user
        else:
            print('Invalid credentials. Try again.')
            return None

    def get_user(self,users):
        user=None
        for u in users:
            if u.username==self.username and u.pin==self.pin:
                user=u
                break
        return user
# auth class ends

def main()->None:
    bank=Bank()
    # create users and accounts
    user1=User(1,"amir","1122","Amir","Zeb")
    user2=User(2,"ali","4455","ali","khan")
    bank.add_user(user1)
    bank.add_user(user2)
    bank.add_account(Account(1,user1,100))
    bank.add_account(Account(2,user2,50))

    while True:
        print(F"\nWELCOME TO {bank.bank_name}")
        print("__ATM_SIMULATOR__\n")
        # get user credentials
        user_name=input("Username :").strip().lower()
        pin=input("Pin :").strip().lower()
        
        # authenticate user credentials
        user_auth=Auth(user_name,pin)
        
        # validate user
        if user_auth.validate_credentials():
            # login user
            user=user_auth.login_user(bank.users)
            account=bank.find_account_for_user(user)
            print("🚀 ~ main ~ account:", account)
            
            if user:
                while True:
                    # print main menu
                    print("\nMAIN MENU")
                    menu_text = ", ".join(f"{k}: {v}" for k, v in MAIN_MENU.items())
                    print(f"{menu_text}\n")
                    menu_opt=input("Enter menu option :").strip().lower()
                    match menu_opt:
                        case 'w':
                            print("withdraw money will be implemented soon.")
                        case 'i':
                            print("balance inquiry will be implemented soon.")
                        case 't':
                            print("transaction history will be implemented soon.")
                        case 'c':
                            print("Thankyou for using our services.")
                            print("__________*********_________\n")
                            break
                        case _:
                            print("Menu option not available.")

if __name__ == "__main__":
    main()