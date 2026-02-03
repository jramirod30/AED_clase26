from bank_account import BankAccount

bank: BankAccount = BankAccount(1000)

bank.deposit(40)
print(f"Balance: {bank.bank_balance}")
print(bank)

bank1: BankAccount = BankAccount(2000, True)

print(bank1)

BankAccount.set_opening_expenditure(20)

print(bank)
print(bank1)
print(f"List of components: {dir(BankAccount)}")
print(f"bank instance list of attributes: {bank.__dict__}")
print(f"bank1 instance list of attributes: {bank1.__dict__}")
# bank instance didn’t hide class attribute __interest_rate
print(f"Interest rate bank {bank.get_interest_rate2()}")
# bank1 instance has hidden class attribute __interest_rate
print(f"Interest rate bank1 {bank1.get_interest_rate2()}")
