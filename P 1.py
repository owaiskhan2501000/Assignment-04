class BankAccount:
    def __init__(self, account_number, balance, owner_name, pin):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner_name = owner_name
        self.__pin = pin
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_owner_name(self):
        return self.__owner_name
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance value. Balance must be non-negative.")

    def set_owner_name(self, new_owner_name):
        if isinstance(new_owner_name, str):
            self.__owner_name = new_owner_name
        else:
            print("Invalid owner name. Please provide a valid string.")
    def set_pin(self, current_pin, new_pin):
        if current_pin == self.__pin:
            if isinstance(new_pin, int) and 1000 <= new_pin <= 9999:
                self.__pin = new_pin
                print("PIN successfully updated.")
            else:
                print("Invalid PIN. Please provide a 4-digit integer PIN.")
        else:
            print("Incorrect current PIN. PIN update failed.")
