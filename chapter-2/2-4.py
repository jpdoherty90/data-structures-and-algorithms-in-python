class Flower:

    def __init__(self, name, petals, price):

        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, new_name):

        self._name = new_name

    def set_name(self, new_petals):
    
        self._petals = new_petals

    def set_name(self, new_price):
    
        self._price = new_price

    def get_name(self):

        return self._name

    def get_petals(self):

        return self._petals

    def get_price(self):

        return self._price





#  TESTING

rose = Flower("rose", 30, 2.00)

print rose.get_name()
print rose.get_petals()
print rose.get_price()


