import keyword

print("hello python")

# 1. Print several things at once - Python puts a space between them
print("Priya", "is", 24, "years old")

# 2. Change the separator between them
print("2026", "08", "31", sep="-")

# 3.Stop it jumping to a new line  at the end
print("Loading", end="...")
print("done")
"""
Real-life example. sep="-" is how you'd print a date,
sep=", " is how you'd print a shopping list, and
end="" is how a progress bar keeps writing dots
on the same line instead of dribbling down the screen. 
"""
# Variables
city = "Mumbai"
name = "Priya Sharma"
age = 24
salary = 45000.50
is_employed = True

print(name, age, salary, is_employed)

print(keyword.kwlist)  # forbidden keywords

# Rules for naming — the professional habits
# snake_case for variables and functions — lowercase, words joined by _
total_amount = 5000
coustomer_email = "priya@example.com"

# SCREAMING_SNAKE_CASE for values that never change (constants)
GST_RATE = 0.05
MAX_LOGIN_ATTEMPTS = 3

# Names that say what they hold

days_until_delivery = 7

# Names that say nothing

x = 7
temp = 7
data2 = 3


# int - whole numbers

quantity = 12
temperature = -5
population = 1_400_000_000

print(quantity, temperature, population)


# float - decimal numbers

price = 249.99
gst_rate = 0.05
average_score = 78.5

print(price, gst_rate, average_score)
print(price * gst_rate)

print(0.1 + 0.2)

# The professional way to handle money
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))

# str -text

first_name = "Priya"
last_name = "Sharma"
empyt = ""  # a valid string with zero characters
number_as_text = "24"  # this is TEXT, not a number

# Triple quotes keep line breaks exactly as you typed them

address = """12 New Market
Delhi 400020
India"""
print(address)


print("She said 'hello' to me.")
print('She said \t"hello" to me.')
print('She said \n"hello" to me.')
print("Name:\tPriya\nCity:\tMumbai")

# bool - True and False and not true/false

is_logged_in = True
has_paid = True
is_adult = 24 >= 18

print(type(is_adult))

# None - the absence of a value

"""None means "there is deliberately nothing here". It is not zero, and it is not an empty string — it is the concept of not filled in."""

middle_name = None
delivery_date = None

print(type(24))  # → <class 'int'>
print(type(24.0))  # → <class 'float'>
print(type("24"))  # → <class 'str'>
print(type(True))  # → <class 'bool'>
print(type(None))  # → <class 'NoneType'>

# To test a type in a condition, use isinstance() — not type() ==
age = 24
print(isinstance(age, int))  # → True


# Type conversion (casting)
# str -> int
age_text = "24"
age = int(age_text)
print(age + 1)

# Str -> float
price = float("249.99")
print(price * 2)

# int/float -> str
total = 400
print("your total is " + str(total))

# float -> int (truncates!)

print(int(3.5))
print(int(-3.6))
print(round(3.4999999))

# What is falsy?

print(bool(0), bool(0.0), bool(None), bool([]))
print(bool(1), bool(-5), bool("hi"), bool(" "))


# Getting input from a user

# name = input("what is your name?")
print("Hello,", name)

# age = int(input("your age: "))
print(age + 1)


# Formatting output properly - the f-string
name = "priya"
age = 23
salary = 45000.5

# The old , clumsy way
print("Name:", name + ", Age: " + str(age))

# The f-string -read it like a sentence
print(f"Name: {name}, Age: {age}")

# You can put any expression inside th braces
print(f"Next year {name} will be {age +1}.")

# Formatting: 2 decdimal places, and  thousands separators
print(f"Salary: Rs{salary:,.2f}")

# Handy for debugging - the  = sign prints the name AND the value
print(f"{age=}")
