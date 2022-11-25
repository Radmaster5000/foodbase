from database import connect
from ingredients import Ingredient, record_ingredient
from meals import Meal, record_meal
from measurements import Measurement, record_measurement

cursor = connect()

# cursor.execute("SELECT * FROM ingredients")

# for row in cursor:
#     print(f"row = {row}")

#def main_menu():

# test_ingredient = record_ingredient()

# print(test_ingredient.__str__())

# test_meal = record_meal()

# print(test_meal.__str__())

test_measurement = record_measurement()
print(test_measurement.__str__())