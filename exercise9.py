# 8-3

def make_shirt(size, text):
    print(f"shirt size with {text}")


make_shirt('XL', "YO!")

# 8-4

def make_shirt(size = 'L', text = 'I love Python'):
    print(f"shirt size {size.title()} with {text}")


make_shirt('M', 'My brain hurts')
make_shirt()

# 8-5

def describe_city(city, country='USA'):
    print(f"{city.title()} is in {country.title()}")


describe_city('Paris', 'France')
describe_city('Chicago')
describe_city('Tokyo', 'Japan')

# 8-9

messages = ['delete message ', 'call me']
for message in messages:
    print(message)

# 8-10

messages = ['delete message ', 'call me']
sent = []
print("Messages: ", messages)
print("Sent:", sent)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

# 8-11

messages = ['delete message ', 'call me']
sent = []
print("Messages: ", messages)
print("Sent:", sent)


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


send_messages(messages[:], sent)
print("Messages: ", messages)
print("Sent:", sent)

# 9-1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant = Restaurant("Tito's", "Mexican Food")
restaurant.open_restaurant()
print(f"{restaurant.cuisine_type}")
print(f"{restaurant.restaurant_name}")

# 9-2

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant_1 = Restaurant("Tito's", "Mexican Food")
restaurant_2 = Restaurant("Bobs's", "American Food")
restaurant_3 = Restaurant("Tim's", "Asian Food")

restaurant_1.open_restaurant()
print(f"{restaurant.cuisine_type}")
print(f"{restaurant.restaurant_name}")

restaurant_2.open_restaurant()
print(f"{restaurant.cuisine_type}")
print(f"{restaurant.restaurant_name}")

restaurant_3.open_restaurant()
print(f"{restaurant.cuisine_type}")
print(f"{restaurant.restaurant_name}")

# 9-3

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name, self.last_name)
        print()
    def greet_user(self):
        print(f"Hello, {self.first_name}")


new_user = User("Rodriguez", "Chris")
new_user.describe_user()
new_user.greet_user()

# 9-5

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name, self.last_name)
        print()
    def greet_user(self):
        print(f"Hello, {self.first_name}")
    def increment_login_attempts(self):
            self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
            self.login_attempts = 0



new_user = User("Rodriguez", "Christoper")
new_user.reset_login_attempts()
print(f"login attempts value: {new_user.login_attempts}")
