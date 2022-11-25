import unittest

from ingredients import Ingredient
from meals import Meal
from measurements import Measurement

class IngredientTests(unittest.TestCase):
    def test_create_ingredient_values(self):
        # Arrange

        # Act
        ingredient = Ingredient(4, 'Seed Mix', 'Lidl', 'Alesto', 'seeds', 4)

        # Assert
        self.assertEqual(4, ingredient.ingredient_id)
        self.assertEqual('Seed Mix', ingredient.ingredient_name)
        self.assertEqual('Lidl', ingredient.ingredient_shop)
        self.assertEqual('Alesto', ingredient.ingredient_make)
        self.assertEqual('seeds', ingredient._ingredient_desc)
        self.assertEqual(4, ingredient.macro_id)

class MealTests(unittest.TestCase):
    def test_create_meal(self):
        # Act
        meal = Meal(100, 'chicken curry', 'chicken and wholegrain rice')

        # Assert
        self.assertEqual(100, meal.meal_id)
        self.assertEqual('chicken curry', meal.meal_name)
        self.assertEqual('chicken and wholegrain rice', meal.meal_desc)

class MeasurementTests(unittest.TestCase):
    def test_create_measurement(self):
        # Act
        measurement = Measurement(6, 'pieces')

        # Assert
        self.assertEqual(6, measurement.measurement_id)
        self.assertEqual('pieces', measurement.measurement_desc)

if __name__ == '__main__':
    unittest.main()