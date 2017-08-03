class store(object):
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        self.products.remove(product)
        return self

    def inventory(self):
        print "Products:", ", ".join(self.products)
        print "Location:", self.location
        print "Owner:", self.owner
        return self

store1 = store("Seattle", "Me").add_product("apple").add_product("banana").add_product("grape").add_product("apple").remove_product("apple").inventory()
store2 = store("Portland", "Stranger").add_product("apple").add_product("banana").add_product("grape").add_product("apple").inventory()