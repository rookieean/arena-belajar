"""

    Calculate the Sum of Digits in a Number


    Write a function sum_of_digits(num) that takes a non-negative integer as input and returns the sum of its digits.


"""

# what ve made..............
def sum_of_digits(num):
    take = int(input())
    take2 = sum(take)
    print(take2)



# the answer
def sum_of_digits(num):
    res = 0
    for c in str(num):
        res = res + int(c)
    return res

num = int(input())
print(sum_of_digits(num))