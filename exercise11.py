# 9-6


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'cherry']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand = IceCreamStand('Ice Cream Stand', 'Ice Cream')
ice_cream_stand.display_flavors()


# 9-7

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"\nHello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        print("/nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

self = Admin('tony', 'hernandez')
self.describe_user()

self.privileges = [
    'can reset passwords'
    'can moderate discussions'
    'kick people out'
]

self.show_privileges()

# 9-8

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
            print("- Access denied")


tito = Admin('Tito', 'Rodriguez')
tito.describe_user()

tito.privileges.show_privileges()

print("\nAdding privileges...")
tito_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can kick people out',
    ]
tito.privileges.privileges = tito_privileges
tito.privileges.show_privileges()
