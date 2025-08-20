"""
    Create a function named even_odd_divider that takes a list of positive integers as strings.

    The function should split this list into two lists: one with even numbers and one with odd numbers. Return these two lists wrapped in a main list. If there are no even or odd numbers, return an empty list.

    pembagi angka genap dan ganjil
"""

def even_odd_divider(lst):
    even = []
    odd = []
    for i in lst:
        num = int(i)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(odd) == 0 and len(even) == 0:
        return []
    else:
        return [even, odd]