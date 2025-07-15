"""
Write a Python function named filter_even_numbers that takes a list of numbers as input and returns a new list containing only the even numbers from the original list, using list comprehension.


Fungsi ini dirancang untuk mengambil daftar angka dan menyaringnya, hanya menyisakan angka-angka genap.

List comprehension adalah cara yang sangat ringkas dan efisien di Python untuk membuat list baru berdasarkan list yang sudah ada.

"""


def filter_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]


"""
    []  -> untuk membuat list baru, berdasarkan list yg udah ada
    x   -> apa yang akan dimasukan dalam list baru
    for x in numbers -> x akan mengulang setiap yang ada di numbers


    "Buatlah sebuah list baru. Untuk setiap x dalam list numbers yang diberikan, masukkan x ke dalam list baru hanya jika x adalah angka genap (yaitu, sisa pembagian x dengan 2 adalah 0)."

    

"""