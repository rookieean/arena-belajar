print("\nNormalPyramid")
for i in range(5):
    x='*'
    x=x*i
    print(f'{x:^10}')

print("\nInvertedPyramid")
for i in range(5):
    x='@'
    x=x*(5-i)
    print(f'{x:^10}')

print("\nHollowPyramid")
for i in range(5):
    x='*'
    x=x*(2*i+1)
    print(f'{x:^10}')   

print("\nHollowInvertedPyramid")
for i in range(5):
    x='@'
    x=x*(2*(5-i)-1)
    print(f'{x:^10}')

print("\nHollowPyramidWithSpace")
for i in range(5):
    x='*'
    x=x*(2*i+1)
    print(f'{x:^10}')

print("\nleftsidedpyramid")
for i in range(5):
    x='*'
    x=x*i
    print(f'{x:<10}')

print("\nRightsidedpyramid")
for i in range(5):
    x='*'
    x=x*i
    print(f'{x:>5}')

print("\nPatternNumber")
n = 5
for i in range(n):
    p = 1
    for j in range(i+1):
        print(p, end=' ')
        p += 1
    print()

print("\nPatternAlphabet")
n = 5
p = 1
for i in range(n-1):
    for j in range(i, n):
        print(' ', end = ' ')
    for j in range(i):
        print(p, end = ' ')
    for j in range (i+1):
        print(p, end = ' ')
    p += 1
    print()
for i in range (n):
    for j in range (i+1):
        print(' ', end = ' ')
    for j in range(i, n-1):
        print(p, end = ' ')
    for j in range (i, n):
        print(p, end = ' ')
    p -= 1
    print()

print("\nPatternNumber")
n = 5
for i in range(n):
    p = 1
    for j in range(i+1):
        print(p, end=' ')
        p += 1
    print(f'{p:>5}')
