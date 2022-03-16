# These were created in two different files, but for the sake of turning this in on one sheet..they are combined here. Terminal was a success!
# printing_functions.py:

def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# printing_models.py:

        import printing_functions as pf

        unprinted_designs = ['boots', 'dogs', 'cats']
        completed_models = []

        pf.print_models(unprinted_designs, completed_models)
        pf.show_completed_models(completed_models)


# 9-10
# taken from restaurant.py

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} serves delicious {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} is open. Welcome!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

# from file my_restaurant.py

from restaurant import Restaurant

channel_club = Restaurant('YUMMY', 'Mexi-Q')
channel_club.describe_restaurant()
channel_club.open_restaurant()

# 9-11

# from file user.py

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"\nWelcome back, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = Privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

# from file my_user.py

from user import Admin

self = Admin('tony', 'hernandez')
self.describe_user()

self_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can block accounts',
    ]
self.privileges.privileges = self_privileges

print(f"\nThe admin {self.first_name} has these privileges: ")
self.privileges.show_privileges()

# 9-12

# from file user.py:

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"\nWelcome back, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# from file admin.py:

from user import User


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = Privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

# from my_admin.py

from admin import Admin

self = Admin('tony', 'hernandez')
self.describe_user()

self_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
self.privileges.privileges = self_privileges

print(f"\nThe admin {self.first_name} has these privileges: ")
self.privileges.show_privileges()

# 9-16

# I visited pymotw.com and went through the random module as suggested. Example code I ran from the standard library:
# random_random.py

import random

for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()
