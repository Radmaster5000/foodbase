
class Measurement:
    '''
    A class to create a measurement object that can be added
    to the measurements table
    '''

    def __init__(self, measurement_id, measurement_desc):
        self.measurement_id = measurement_id
        self.measurement_desc = measurement_desc

    def __str__(self):
        '''
        Prints the measurement's name and description for a quick summary
        '''
        return f"measurement {self.measurement_id} | {self.measurement_desc}"

    @property
    def measurement_id(self):
        return self._measurement_id

    @measurement_id.setter
    def measurement_id(self, measurement_id):
        #TODO check the id doesn't already exist in the table and it's an integer
        self._measurement_id = measurement_id

    @property
    def measurement_desc(self):
        return self._measurement_desc

    @measurement_desc.setter
    def measurement_desc(self, measurement_desc):
        #TODO check the name is a string and it's less than 150 characters
        self._measurement_desc = measurement_desc
    
def record_measurement():
    '''
    Takes input from the user and a single measurement object is created
    from the inputted data. 
    '''
    print("Input the measurement information...")

    # this hardcoded number is for testing only. It needs to be replaced with a 
    # function that checks the measurements table and assigns the next increment.
    # Maybe that should be done outside the measurements class?!
    _measurement_id = 100

    _measurement_desc = input("\nPlease enter a brief description of the measurement: ")

    new_measurement = Measurement(measurement_id=_measurement_id,
                                measurement_desc=_measurement_desc)

    return new_measurement