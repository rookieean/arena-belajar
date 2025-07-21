"""
Buat sebuah fungsi bernama swap_characters yang menerima input_string sebagai parameternya.

Fungsi ini bertujuan untuk membuat string baru dengan menukar karakter pertama dan terakhir dari input_string yang diberikan.

Untuk melakukannya, ikuti langkah-langkah berikut:

Periksa apakah panjang input_string kurang dari 2. Jika ya, kembalikan input_string apa adanya karena penukaran tidak mungkin dilakukan.
Simpan karakter pertama dari input_string dalam sebuah variabel.
Ganti karakter pertama dari input_string dengan karakter terakhir.
Mengganti karakter terakhir dari input_string dengan karakter pertama yang disimpan.
Kembalikan input_string yang telah dimodifikasi.
Parameter

input_string (str): String masukan yang perlu ditukar karakter pertama dan terakhirnya.
Fungsi ini akan mengembalikan sebuah string dengan karakter pertama dan terakhir dari input_string yang ditukar.

"""


def swap_characters(input_string):
    if len(input_string) < 2:
        return input_string
    else:
        first_char = input_string[0]
        modified_string = input_string[-1] + input_string[1:-1] + first_char
        return modified_string