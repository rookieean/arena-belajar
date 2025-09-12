"""
    'why i made this code?'

    the story is, when sensei share his past story to code his reverse name in code program. he need to put into Array first, and then use 'for in' with initial, condition and the end initial point. so i was thinking in my head, 

    '..using python is more easiest way, but i forgot the function to reverse something, filter? no! what it is..? ' 

    even though, i just wanna be silly and came up here 

"""



#--------------------------------------- Part I

# pembalik nama logika sederhana
nama = ['K', 'I', 'N', 'G', 'G', 'N', 'U']

print(nama[6])
print(nama[5])
print(nama[4])
print(nama[3])
print(nama[2])
print(nama[1])
print(nama[0])




#--------------------------------------- Part II

# program output pembalik nama, dgn fungsi bawaan python, simple
wadah = ['T', 'S', 'U', 'N', 'E', 'T', 'A']

for b in reversed(wadah):
    print(b)




#--------------------------------------- Part III

# nyoba pakai fungsi
def jujutsu(gojo):
    for b in reversed(gojo):
        print(b)

jujutsu(wadah)




#--------------------------------------- Part VI

# fungsi yang lebih normal lah
iblis_kutukan = ['Mahito', 'Sukuna', 'Kamo', 'Geto', 'Dagon'] 

def pembalik_kutukan(gojo_satoru):
    for setiap_iblis_kutukan in reversed(gojo_satoru):
        print(setiap_iblis_kutukan)

pembalik_kutukan(iblis_kutukan)