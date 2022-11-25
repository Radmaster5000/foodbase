

class Ingredient:
    '''
    A class to create an ingredient object that can be added
    to the ingredients table
    '''

    def __init__(self, ingredient_id, ingredient_name, ingredient_shop,
                 ingredient_make, ingredient_desc, macro_id):
        self.ingredient_id = ingredient_id
        self.ingredient_name = ingredient_name
        self.ingredient_shop = ingredient_shop
        self.ingredient_make = ingredient_make
        self.ingredient_desc = ingredient_desc
        self.macro_id = macro_id

    def __str__(self):
        '''
        Prints the ingredients name and description for a quick summary
        '''
        return f"Ingredient {self.ingredient_id} | {self.ingredient_name} | {self.ingredient_desc}"

    @property
    def ingredient_id(self):
        return self._ingredient_id

    @ingredient_id.setter
    def ingredient_id(self, ingredient_id):
        #TODO check the id doesn't already exist in the table and it's an integer
        self._ingredient_id = ingredient_id

    @property
    def ingredient_name(self):
        return self._ingredient_name

    @ingredient_name.setter
    def ingredient_name(self, ingredient_name):
        #TODO check the name is a string and it's less than 150 characters
        self._ingredient_name = ingredient_name

    @property
    def ingredient_shop(self):
        return self._ingredient_shop

    @ingredient_shop.setter
    def ingredient_shop(self, ingredient_shop):
        #TODO check the shop is a string and it's less than 150 characters
        self._ingredient_shop = ingredient_shop
    
    @property
    def ingredient_make(self):
        return self._ingredient_make

    @ingredient_make.setter
    def ingredient_make(self, ingredient_make):
        #TODO check the make is a string and it's less than 150 characters
        self._ingredient_make = ingredient_make

    @property
    def ingredient_desc(self):
        return self._ingredient_desc

    @ingredient_desc.setter
    def ingredient_desc(self, ingredient_desc):
        #TODO check the desc is a string and is less than 150 characters
        self._ingredient_desc = ingredient_desc

    @property
    def macro_id(self):
        return self._macro_id

    @macro_id.setter
    def macro_id(self, macro_id):
        #TODO check the macro id is an integer and matches the ingredient name in the macro table?
        self._macro_id = macro_id

def record_ingredient():
    '''
    Takes input from the user and a single ingredient object is created
    from the inputted data. 
    '''
    print("Input the ingredient information...")

    # this hardcoded number is for testing only. It needs to be replaced with a 
    # function that checks the ingredients table and assigns the next increment.
    # Maybe that should be done outside the ingredients class?!
    _ingredient_id = 100

    _ingredient_name = input("\nPlease enter the name of the product: ")

    _ingredient_shop = input("\nPlease enter the name of the shop: ")

    _ingredient_make = input("\nPlease enter the make of the ingredient: ")

    _ingredient_desc = input("\nPlease enter a brief description of the ingredient: ")

    # as with ingredient_id, this needs to be dynamically generated
    _macro_id = 99

    new_ingredient = Ingredient(ingredient_id=_ingredient_id, ingredient_name=_ingredient_name,
                                ingredient_shop=_ingredient_shop, ingredient_make=_ingredient_make,
                                ingredient_desc=_ingredient_desc, macro_id=_macro_id)

    return new_ingredient