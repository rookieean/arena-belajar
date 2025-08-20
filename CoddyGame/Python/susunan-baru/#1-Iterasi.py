
"""
Fungsi ini enumerate()memungkinkan Anda untuk mengulang suatu urutan (seperti daftar, tupel, atau string) sambil tetap melacak posisi indeks setiap item.
"""

# tanpa enumerate
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# dengan enumerate
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")



#------------------ CHALENGE
"""
Tulis program yang menerima daftar angka sebagai input ( diberikan ), dan mencetak daftar indeks angka yang di bawah 50 atau habis dibagi 5. 
"""

lst = list(map(int, input().split(",")))
new_lst = []
for index, num in enumerate(lst):
    if num < 50 or num % 5 == 0:
        new_lst.append(index)
print(new_lst)