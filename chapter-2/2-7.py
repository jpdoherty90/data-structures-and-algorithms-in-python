class CreditCard:
    
    def __init__(self, customer, bank, acnt, limit, bal=0):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = bal

    def get_customer(self):

        return self._customer

    def get_bank(self):

        return self._bank

    def get_account(self):

        return self._account

    def get_limit(self):

        return self._limit

    def get_balance(self):

        return self._balance

    def charge(self, price):
        
        if isinstance(price, (int, float)):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        raise TypeError("Price must be a number")
    
    def make_payment(self, amount):
        
        if isinstance(amount, (int, float)):
            if amount >= 0: 
                self._balance -= amount
            else:
                raise ValueError("Payment amount cannot be negative")
        else:
            raise TypeError("Payment amount must be numeric")

    