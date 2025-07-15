"""
    Write a function named alphabet_soup that accepts a string and returns it with letters in alphabetical order.

    Examples:

    alphabet_soup("hello") returns "ehllo"
    alphabet_soup("coddy") returns "cddoy"
    alphabet_soup("hacker") returns "acehkr"

"""


def alphabet_soup(s):
    return ''.join(sorted(s))

ast = str(input("masukan input = "))
print(alphabet_soup(ast))



"""
                                PENJELASAN

                                
A.SORTED()

Fungsi sorted() adalah fungsi bawaan (built-in) Python yang sangat berguna.
Ketika Anda meneruskan sebuah string ke sorted(), fungsi ini akan mengembalikan sebuah daftar (list) dari karakter-karakter dalam string tersebut, yang telah diurutkan secara alfabetis (berdasarkan nilai ASCII/Unicode) secara ascending (dari A ke Z, atau angka dari 0 ke 9, dll.).
Contoh:
Jika s adalah "hello", maka sorted(s) akan menghasilkan ['e', 'h', 'l', 'l', 'o'].
Jika s adalah "python", maka sorted(s) akan menghasilkan ['h', 'n', 'o', 'p', 't', 'y'].
Perhatikan bahwa huruf kapital diurutkan sebelum huruf kecil dalam urutan ASCII/Unicode. Misalnya, sorted("Za") akan menghasilkan ['Z', 'a'].



B.JOIN()

Ini adalah metode string yang digunakan untuk menggabungkan elemen-elemen dari sebuah iterable (dalam kasus ini, daftar karakter yang dihasilkan oleh sorted(s)) menjadi satu string tunggal.
Bagian '' sebelum .join adalah "delimiter" atau pemisah. Dalam kasus ini, kita menggunakan string kosong (''), yang berarti tidak ada pemisah yang akan disisipkan di antara elemen-elemen yang digabungkan. Jika Anda menggunakan '-'.join(...), maka akan ada tanda hubung di antara setiap elemen.
Contoh lanjutan dari sebelumnya:
Jika sorted(s) menghasilkan ['e', 'h', 'l', 'l', 'o'], maka ''.join(['e', 'h', 'l', 'l', 'o']) akan menghasilkan string "ehllo".
Jika sorted(s) menghasilkan ['h', 'n', 'o', 'p', 't', 'y'], maka ''.join(['h', 'n', 'o', 'p', 't', 'y']) akan menghasilkan string "hnopty".

"""
