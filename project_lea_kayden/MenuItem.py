class MenuItem(object): # create menuitem class
    def __init__(self,name, category, price, description):
        self.name = name # sets up name variable
        self.category = category # sets up category variable
        self.price = float(price) # sets up price variable
        self.description = description # sets up description variable
    def getName(self): #returns the name
        return self.name
    def getCategory(self): # returns the category
        return self.category
    def getPrice(self): # returns the price
        return self.price
    def getDescription(self): # returns the description
        return self.description
    def __str__(self): #returns a string of the menuitem object based on inputs
        return str(self.name+"("+self.category+"): "+"$"+ "{:.2f}".format(self.price) +"\n"+self.description)

