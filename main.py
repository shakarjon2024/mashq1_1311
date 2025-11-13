class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so'm depozit qilindi. Yangi balans: {self.__balance} so'm")
        else:
            print("Depozit miqdori musbat bo‘lishi kerak!")


    def withdraw(self, amount):
        if amount <= 0:
            print("Pul miqdori musbat bo‘lishi kerak!")
        elif amount > self.__balance:
            print("Xatolik! Balansda yetarli mablag‘ mavjud emas.")
        else:
            self.__balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.__balance} so'm")


    def get_balance(self):
        return self.__balance

    def account_info(self):
        print(f"Mijoz: {self.__customer_name}, Hisob raqami: {self.__account_number}, Balans: {self.__balance} so'm")

class PremiumAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0, discount_rate=0.02):
        super().__init__(account_number, customer_name, balance)
        self.__discount_rate = discount_rate


    def add_interest(self):
        bonus = self.get_balance() * self.__discount_rate
        self.deposit(bonus)
        print(f"Premium bonus ({self.__discount_rate * 100}%): {bonus} so'm qo'shildi.")


account1 = BankAccount("UZ123456", "Ali", 100000)
account1.deposit(50000)
account1.withdraw(30000)
print("Balans:", account1.get_balance())
account1.account_info()

print("\n--- PREMIUM ACCOUNT ---")


premium = PremiumAccount("UZ987654", "Vali", 200000)
premium.deposit(100000)
premium.add_interest()
premium.withdraw(150000)
premium.account_info()
