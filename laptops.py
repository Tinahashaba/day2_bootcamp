import abc


class Laptop(object):
    __metaclass__ = abc.ABCMeta
    initial_sale_price = 0
    battery_life = 0

    def __init__(self, year, HDD, RAM, sold_on):
        self.year = year
        self.HDD = HDD
        self.RAM = RAM
        self.sold_on = sold_on

    def sale_price(self):
        """checks if the laptop has been sold and calcuates the price if hasnt been sold"""
        if self.sold_on is not None:
            return 'Already sold'
        else:
            return 30 * self.battery_life

    def purchase_price(self):
        """checks if laptop was sold and if it was returns the resale price"""
        if self.sold_on is None:
            return 'Not yet sold'
        else:
            return 0.8 * self.initial_sale_price

    @abc.abstractmethod
    def Laptop_type(self):
        """provides type of laptop"""
        pass


class DELL(Laptop):
    """overriding price of the dell laptop"""
    initial_sale_price = 45000
    battery_life = 4

    def Laptop_type(self):
        return 'Dell'


class HP(Laptop):
    """overriding price of the HP laptop"""
    initial_sale_price = 9000
    battery_life = 6

    def Laptop_type(self):
        return 'HP'


class LENOVO(Laptop):
    """overriding price of the lenovo laptop"""
    initial_sale_price = 15000
    battery_life = 5

    def Laptop_type(self):
        return 'Lenovo'
