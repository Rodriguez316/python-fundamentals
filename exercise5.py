ball = 'golfball'
print("Is the ball == 'golfball'? I predict True.")
print(ball == 'golfball')

print("\nIs ball == 'baseball?' I predict false.")
print(ball =='baseball')

food = 'hotdog'
print("Is the food == 'hotdog'? I think yes.")
print(food == 'hotdog')

print("\nIs the food == pizza'? I think false.")
print(food == 'pizza')

pi = 3.14
print("3.14 equals pi")
print(pi == 3.14)
print("10 == pi?")
print(pi == 10)

value = 'taco'
print("does value == taco?")
print(value == "taco")
print("does value == carrot?")
print(value == "carrot")

Gun = 'Riffle'
print("is the gun == a Riffle?")
print(Gun == "Riffle")
print("is the Gun == a watergun?")
print(Gun == 'watergun')


string_test = "random string test"
print(string_test == "true and false statements")
print()

test = "This IS just A TEST"
print(test.lower() == "this is just a test")
print(test.lower() == "THIS IS JUST A TEST")

my_savings = 1000000
print("The total of my savings is more than 100000: ", my_savings >= 1000000)
print("The total of my savings is less than 10000: ", my_savings <= 100000)


age = 20
print("Age is: ", age)
print("Is your age greater than 10 and more than 15")
print(age > 10 and age > 15)
print("Age is more than thirty and more than nineteen")
print(age > 30 and age > 19)

grocery_list = ("milk", "eggs", "bread")
print("'cheese', is in my grocery list: ", 'cheese' in grocery_list)
print("'bread', is in my grocery list: ", 'bread' in grocery_list)


value1 = 5
value2 = 6

def basic_assign(value1,value2):
    value1 += value2
    print(value1)
    value1 -= value2
    print(value1)
    value2 *= value1
    print(value2)
    value2 /= value1
    print(value2)