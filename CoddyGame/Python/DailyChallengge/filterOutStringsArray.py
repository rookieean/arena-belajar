'''

Create a function named filter_list that takes a list of non-negative integers and strings and returns a new list without the strings.

The function should maintain the original order of the integers in the list.

Examples:

filter_list([1, 2, "a", "b"]) returns [1, 2]
filter_list([1, "a", "b", 0, 15]) returns [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) returns [1, 2, 123]


membuat fungsi dengan nama filter_list, yang isinya bisa menm-filter array campuran, outputnya jadi array angka saja

'''

# def filter_list(a):
#   return[if a == int print]


def filter_list(a):
    res = []
    for i in a:
        if type(i) == int:
            res.append(i)
    return res

