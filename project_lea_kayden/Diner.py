
class Diner(object): # diner class
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"] # list of statuses
    def __init__(self, dinername):
        self.name = dinername # sets up diner name
        self.order = [] # sets up list for the orders
        self.status = 0 # sets status as 0
    def getName(self):
        return self.name # returns the name
    def getOrder(self): # returns the order list
        return self.order
    def getStatus(self): # returns the status number for index
        return self.status
    def updateStatus(self): # updates status by adding one
        self.status +=1
    def addToOrder(self, menuitem): # adds the menuitem to the order
        self.order.append(menuitem)
    def printOrder(self): # prints the order with the name and what they ordered
        print(self.getName(), "ordered:")
        for item in self.order: # prints every item one after another for the list
            print("- ", item)
    def getMealCost(self):
        cost = 0 # sets cost as 0
        for item in self.order: # for every item, calls the getprice and then adds to total cost
            cost += (item.getPrice())
        return float(cost) # returns as float
    def __str__(self): # returns a string for the status
         return "Diner "+ self.name + " is currently"


