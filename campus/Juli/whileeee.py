# membuat sebuah program untuk mencetak angka genap 1 - 5 (2,4)

nama = input("coba input")

while nama % 2 == 0:
    print("angka anda genap ")

#take the input
n = int(input("take your input: "))
#start the loop
i = 1
while i <= n:
   #this condition mean the i is divisable by 2 (is even)
   if i % 2 == 0:
      print(i)
   i = i + 1