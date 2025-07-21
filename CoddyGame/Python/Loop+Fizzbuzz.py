"""

                                                 FUNCTIONS

"""


# membangun penjumlahan dalam range
def sum_numbers():
    res = 0
    for i in range(1, 10001):
        res += i
    print(res)

n = int(input())
for i in range(n):
    sum_numbers()












# membangun fungsi perkalian
def perkalian(a, b):
    return a * b

result = int(input())
result2 = int(input())

hasil = perkalian(result, result2)

print(hasil)





# membangun fungsi kotak kali kotak
def square_number(n):
    return n ** 2

angka = int(input("angka = "))

hasil2 = square_number(angka)

print(hasil2)




# membangun volume kubus
def cube_number(n):
    return n ** 3

input_num = int(input())
result = cube_number(input_num)
print(result)



# i made vs
def sigma(n):
    for i in range(1, n + 1):
        i += 1
    
# the right answers..
def sigma(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res















# fungsi username dan password

# fungsi yang saya buat
def is_valid(username, password):
    if username == "admin" or "user" and password == "qweasd":
        print(True)
    else:
        print(False)


user_input_username = str(input())
user_input_password = str(input())

result_user = is_valid(user_input_username, user_input_password)


# fungsi yang benar....
def is_valid(username, password):
    if username == 'admin' or (username == 'user' and password == 'qweasd'):
        return True
    else:
        return False
    









# default arguments
def describe_person(name, age=25, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}")

# name = default parameter -> dia belum ada isinya
# age sama city = non-default parameter -> dia udah ada isinya

# urutannya - yg kosong dulu, baru yg ada isinya

describe_person("Alice")
# Uses both defaults

describe_person("Bob", 30)
# Uses default city

describe_person("Charlie", 35, "New York")
# Uses no defaults











# FUZZBUZZ

# yang saya bikin...
print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    if num % 3 == 0:
        print("Fizz")
    elif num % 7 == 0:
        print("Buzz")
    elif num % 7 and 3 == 0:
        print("FizzBuzz")
    else:
        print(num)
        
user_input = int(input("hei.. input ur num ="))

result_user = fizzbuzz(user_input)


# tang benar jawabannya...
print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        result = str(number)
    return result

limit = int(input())
print(fizzbuzz(limit))

# Play FizzBuzz
for i in range(1, limit + 1):
    print(fizzbuzz(i))


# new again..
print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        if "3" in str(number):
            result = "Almost Fizz"
        else:
            result = str(number)
    return result

limit = int(input())

# Play FizzBuzz
for i in range(1, limit + 1):
    print(fizzbuzz(i))










# simulasi brilliant
leaves = 29
daily_hail = [6, 0, 4, 3, 7]

for hail in daily_hail:
  if hail > 0:
    shelter = True
  else:
    shelter = False
  if shelter == False:
    leaves -= hail
  
print ("Leaves:", leaves)










# IF ELSE................

# I MADE
temperature = int(input()) # Don't change this line
weather = "unset"
# Type your code below

if temperature < 0:
    print("Freezing")
elif temperature  <= 15:
    print("Cold")
elif temperature >= 16:
    print("Mild")
else:
    print("Hot")


# Don't change the line below
print(f"weather = {weather}")



# his made
temperature = int(input()) # Don't change this line
weather = "unset"

if temperature < 0:
    weather = "Freezing"
elif temperature >= 0 and temperature <= 15:
    weather = "Cold"
elif temperature >= 16 and temperature <= 25:
    weather = "Mild"
else:
    weather = "Hot"

# Don't change the line below
print(f"weather = {weather}")









# NESTED IF ELSE

# GUA BERHASIL COOYYYY....
level = int(input("input ur level = ")) # Don't change this line
has_training = input() == "True" # Don't change this line
level_message = "None" # Don't change this line

# Write your code below
level_message = ""
if level >= 1 and level <= 5:
    level_message = "Basic weapons only"
elif level >= 6 and level <= 10: 
    if has_training:
        level_message = "Access to advanced weapons granted" 
    else:
        level_message = "Need weapon training first"
elif level >= 11:
    level_message = "Acces to all weapons granted"
else:
    level_message = "Invalid level"


# Don't change below this line
print(level_message)











# yang gua bikin....
# Type your code below

number = input()
if number >= 10 and number <= 50 and number % 2 == 0:
    count_even = number
else:
    count_even = number

# Don't change the line below
print(f"count_even = {count_even}")


# VS JAWABANNYA
# Type your code below
count_even = 0
for i in range(10, 51):
    if i % 2 == 0:
        count_even += 1

# Don't change the line below
print(f"count_even = {count_even}")











"""
                                                LOOP
"""


# BREAK Loop

# yang ana bikin
plus_one = int(input())
plus_two = int(input())


for g in range (plus_one, plus_two):
    if g >= 5:
        print(f"First even number greater than 5: {g}")
    elif g / 7:
        print(f"First number divisible by 7: {g}")
    break


# yang bener 
num1 = int(input())
num2 = int(input())


for num in range(num1, num2):
    if num > 5 and num % 2 == 0:
        print(f"First even number greater than 5: {num}")
        break

for num in range(num1, num2):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break














# NESTED LOOPP



def print_pattern(rows, cols):
    # Outer loop for rows
    for i in range(rows):
        # Inner loop for columns
        row_string = ""
        for j in range(cols):
            row_string += '*'
        # Move to the next line after printing a row
        print(row_string)

# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern(rows, cols)














