from MenuItem import MenuItem
class Menu(object): # menu class
    CATEGORIES = ["Drink", "Appetizer", "Entree", "Dessert"]  # sets up list of categories
    def __init__(self, menufile):
        self.menufile = menufile # menufile from the variable
        self.fileIn = open(self.menufile, "r") # opens file
        self.items = {} # sets up empty dict
        for line in self.fileIn:  # goes through the line
            line = line.strip()  # strips the line
            data_list = line.split(",")  # splits the lines
            cat = data_list[1]  # category will be the first column
            price = data_list[2] # price is second column
            name = data_list[0] # name is the 0 column
            desc = data_list[3] # desc is third column
            menuentry = MenuItem(name, cat, price, desc) # menuentry combines the entries from the columns
            if cat in self.items: # if the category is already in the dictionary adds another entry from the menu to the key
                self.items[cat].append(menuentry)
            else: # if it is not already a key will add a new key and entry
                self.items[cat] = [menuentry]
        self.fileIn.close() # clsoes file
    def getMenuItem(self, string, index): # returns the single menu item from dictionary
        return self.items[string][index]

    def printMenuItems(self,category):
        count = 0 # sets up count
        print("--------", category, "----------") # prints out category first
        if category in Menu.CATEGORIES: # if the variable is in the category list
            for menuItem in self.items[category]: # for every item in that category it will print out with the count
                print(count, ")", menuItem)
                count += 1 # adds one more to the count for the next menu item

    def getNumMenuItems(self,category): # gets the number of menuitems
        self.category = category # sets up category variable
        count = 0 # sets count
        if self.category in Menu.CATEGORIES:
            count = len(self.items[self.category]) # counts the amount of items that are in the key
        return count




