class Computer:
    
    def __init__(self):
        self.__maxprice = 900
        
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
        
    def setMaxPrice(self, price):
        self.__maxprice = price
            
c = Computer()
c.sell()

# change the price directly 
c.__maxprice = 1000
c.sell()   # still shows 900

# using setter function 
c.setMaxPrice(1000)
c.sell()  