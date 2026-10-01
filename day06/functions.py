def greet(name):
    print("hello", name)


greet("vijay")
greet("navya")

# name: parameter, vijay: argument

# Function that return a value


def add(a, b):
    return a + b


result = add(10, 20)

print(result)


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


marks = [70, 80, 90]

average = calculate_average(marks)
print(average)

# Python can return multiple values:


def calculate1(a, b):
    return a + b, a - b


addition, subtraction = calculate1(10, 3)

print(addition, subtraction)

# A lambda is a small anonymous function.

square = lambda x: x * x
print(square(5))


def calculate_tax(price):
    return price * 0.18


print("tax", calculate_tax(200))


# Day 06 practice:
def calculate_avg(numbers):
    return sum(numbers) / len(numbers)


print("average", calculate_avg(marks))
