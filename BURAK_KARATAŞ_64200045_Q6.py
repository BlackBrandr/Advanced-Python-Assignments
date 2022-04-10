class CompanyStock:
    # Constructor
    def __init__(self, name="", price=1,total_shares=0):
        self.name = name
        self.price = price
        self.total_shares = total_shares

    # increases the stock price by p%
    def update_price(self,p):
        return self.price + (p / 100)

    def get_total_shares(self):
        return self.total_shares

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    # sells TL share of total value and updates the remainder of the share number
    def sell(self,m):
        number_of_shares = m/self.price
        # check if there are shares available
        if self.total_shares >= number_of_shares:
            # updates the remaining amount of shares
            self.total_shares -= number_of_shares

    # Buy m TL's total share value and change the total share number
    def buy(self, m):
        number_of_shares = m/self.price
        # updates the remaining amount of shares
        self.total_shares += number_of_shares

# child class
class LimitedStock(CompanyStock):
    # constructor
    def __init__(self, name="", price=1,total_shares=0,ltd_shares=0):
        # call super class constructor
        super(LimitedStock, self).__init__(name, price,total_shares)
        self._ltd_shares = ltd_shares

    # Sells mTL shares and updates the rest of the share amounts
    def sell(self,m):
        number_of_shares = m/self.price
        if number_of_shares <= self._ltd_shares:
            CompanyStock.buy(m)

# Create LimitedStock Object
ltdStock = LimitedStock("VAKFN", 12.60, 1000, 200)
# Sell shares worth of 5000 TL
ltdStock.sell(5000)
# update stock price by +5%
ltdStock.update_price(5)
# buy shares worth of 1000 TL
ltdStock.buy(1000)
print("Company Name: {0}\nStock Price: {1}\nTotal Shares: {2}".format(ltdStock.get_name(), ltdStock.get_price(), ltdStock.get_total_shares()) )