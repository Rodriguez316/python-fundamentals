# 11-1

# code from city_functions.py

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# code from test_cities.py

import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        tokyo_japan = city_country('tokyo', 'japan')
        self.assertEqual(tokyo_japan, 'Tokyo, Japan')

if __name__ == '__main__':
    unittest.main()

# Result- OK

# 11-2

# Modified city_functions.py with required third parameter

def city_country(city, country, population):
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" -population {population}"
    return output_string

# Output from running test_cities.py:
# TypeError: city_country() missing 1 required positional argument: 'population'
# FAILED

# Modified city_functions.py with optional population parameter

def city_country(city, country, population=0):
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string

# Output of running test_cities.py
# OK

# Modified test_cities.py

import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        tokyo_japan = city_country('tokyo', 'japan')
        self.assertEqual(tokyo_japan, 'Tokyo, Japan')

    def test_city_country_population(self):
        tokyo_japan = city_country('tokyo', 'japan', population=5_000_000)
        self.assertEqual(tokyo_japan, 'Tokyo, Japan - population 5000000')

if __name__ == '__main__':
    unittest.main()

# Output Ran 2 Tests OK

# 11-3
# Code from employee.py

class Employee():

    def __init__(self, f_name, l_name, salary):
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount

# Code from test_employee.py

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.tony = Employee('tony', 'hernandez', 65_000)

    def test_give_default_raise(self):
        self.tony.give_raise()
        self.assertEqual(self.tony.salary, 70000)

    def test_give_custom_raise(self):
        self.tony.give_raise(10000)
        self.assertEqual(self.tony.salary, 75000)

if __name__ == '__main__':
    unittest.main()

# Output - Ran 2 tests OK