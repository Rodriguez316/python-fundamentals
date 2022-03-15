# All about numbers
# Numeric types are broken down into 3 distinct categories: int,float, & complex

# int in detail
val_intl1 = 42
val_intl2 = 8164888888
val_intl3 = -4456889
val_intl4 = 123456789987654321

# print values
print(val_intl1)
print(val_intl2)
print(val_intl3)
print(val_intl4)

# get the type of one of our values above
print(type(val_intl4))

# float in detail
val_float1 = 3.14
val_float2 = 2.13456
val_float3 =-234.45

#print values of float
print(val_float1)
print(val_float2)
print(val_float3)
# scientific notation
val_float4 = 25E4
val_float5 = 42e9
val_float6 = -98.6E2

print(val_float4)
print(val_float5)
print(val_float6)

# get the type of a float value
print(type(val_float2))


# complex in partial detail
val_complex = 3j
val_complex2 = -5j
print(val_complex)
print(val_complex2)


# The method below will cover an integer to different numeric system values
print(bin(22))
print(oct(22))
print(hex(22))

value = 0b10110
print(value)

# Taking values that are strings and converting, while also converting
# numbers to string
value1 = float(34)
value2 = int(34.5)
value3 = str(89.3)
value4 = str(48)
value5 = int('45')
value6 = float('23.5')

# print values used in converting
print(value1)
print(value2)
print(value3)
print(value4)
print(value5)
print(value6)

# input allows for users to provide information for us to use
name = input('What is your name?')
movie = input('What is your favorite movie?')

message = 'My name is {0} and my favorite movie is {1}'
print(message.format(name, movie))
