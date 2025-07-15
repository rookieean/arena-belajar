"""
Buat sebuah fungsi bernama compare_spices yang menerima spice1, spice2, dan merchant_preference sebagai parameternya.

Di pasar yang ramai di Damaskus kuno, para pedagang rempah-rempah dikenal dengan selera mereka yang tinggi. Tugas Anda adalah membuat sebuah fungsi yang membandingkan dua rempah-rempah berdasarkan preferensi pedagang.

Fungsi tersebut harus menentukan rempah mana yang berkualitas lebih tinggi menurut aturan berikut:

Jika preferensi pedagang cocok dengan salah satu rempah, maka rempah tersebut dianggap berkualitas lebih tinggi.
Jika preferensi pedagang tidak cocok dengan salah satu rempah, bandingkan nama rempah menurut abjad untuk menentukan rempah yang lebih berkualitas.
Parameter

rempah1 (str): Nama bumbu pertama.
spice2 (str): Nama bumbu kedua.
merchant_preference (str): Bumbu pilihan pedagang.
Fungsi ini mengembalikan sebuah string yang menunjukkan bumbu mana yang memiliki kualitas lebih tinggi. String yang dikembalikan harus dalam format: "[Nama Bumbu] memiliki kualitas yang lebih tinggi."
"""

# yang gua bikin
def compare_spices(spice1, spice2, merchant_preference):
    merchant_preference = {}
    if spice1 or spice2 == True:
        print(f"{merchant_preference} are high")
    elif spice1 or spice2 == False:
        print()
    else:
        return merchant_preference
    

# vs yag bener...
def compare_spices(spice1, spice2, merchant_preference):
    if spice1 == merchant_preference:
        return f"{spice1} is of higher quality."
    elif spice2 == merchant_preference:
        return f"{spice2} is of higher quality."
    else:
        if spice1 < spice2:
            return f"{spice1} is of higher quality."
        else:
            return f"{spice2} is of higher quality."
        
user_input = str(input("input ur spice = "))
user_input2 = str(input("input ur spice = "))
user_input3 = str(input("siapa yang kamu suka = "))

compare_spices(user_input, user_input2, user_input3)
    
        