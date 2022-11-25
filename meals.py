
class Meal:
    '''
    A class to create a meal object that can be added
    to the meals table
    '''

    def __init__(self, meal_id, meal_name,  meal_desc):
        self.meal_id = meal_id
        self.meal_name = meal_name
        self.meal_desc = meal_desc

    def __str__(self):
        '''
        Prints the meal's name and description for a quick summary
        '''
        return f"meal {self.meal_id} | {self.meal_name} | {self.meal_desc}"

    @property
    def meal_id(self):
        return self._meal_id

    @meal_id.setter
    def meal_id(self, meal_id):
        #TODO check the id doesn't already exist in the table and it's an integer
        self._meal_id = meal_id

    @property
    def meal_name(self):
        return self._meal_name

    @meal_name.setter
    def meal_name(self, meal_name):
        #TODO check the name is a string and it's less than 150 characters
        self._meal_name = meal_name

    @property
    def meal_desc(self):
        return self._meal_desc

    @meal_desc.setter
    def meal_desc(self, meal_desc):
        #TODO check the name is a string and it's less than 150 characters
        self._meal_desc = meal_desc
    
def record_meal():
    '''
    Takes input from the user and a single meal object is created
    from the inputted data. 
    '''
    print("Input the meal information...")

    # this hardcoded number is for testing only. It needs to be replaced with a 
    # function that checks the meals table and assigns the next increment.
    # Maybe that should be done outside the meals class?!
    _meal_id = 100

    _meal_name = input("\nPlease enter the name of the product: ")

    _meal_desc = input("\nPlease enter a brief description of the meal: ")

    new_meal = Meal(meal_id=_meal_id, meal_name=_meal_name,
                                meal_desc=_meal_desc)

    return new_meal