class product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    # changes status to "sold"
    def sell(self):
        self.status = "sold"
        return self

    # takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def addtax(self, tax):
        if 0 < tax < 1:
            print "Price:", self.price * tax
        else:
            print "Tax needs to be decimal value."
        return self

    def return_product(self, reason):
        if reason == "d":
            self.status = "defective"
            self.price = 0
        if reason == "b":
            self.status = "for sale"
        if reason == "o":
            self.status = "used"
            self.price = self.price * 20
        return self

    # show all product details
    def display_info(self):
        print "Price:", self.price
        print "Name", self.name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self


product1 = product(20, "shirt", 12, "Gap")
product1.addtax(2)
product1.addtax(.3)
product1.sell().display_info()
product1.return_product("d").display_info()

product2 = product(10, "pants", 10, "Levi")
product2.sell().return_product("o").display_info()