

var = {12, 17, 10, 515, 25, 11, 8, 3, 16, 19}
n = int(input())
jum = 0
i = 0

while i <= 10:
    if var[i] == n:
        jum += 1
    i += 1

if jum > 0:
    print("ADA")
else:
    print("TIDAK ADA")



var = [12, 17, 10, 515, 25, 11, 8, 3, 16, 19] # Changed to a list
n = int(input("Masukkan angka yang ingin dicari: ")) # Added a prompt
jum = 0
i = 0

# Loop through each element in the list
while i < len(var):
    if var[i] == n:
        jum += 1 # Increment jum if the number is found
    i += 1

if jum > 0:
    print("ADA")
else:
    print("TIDAK ADA")




