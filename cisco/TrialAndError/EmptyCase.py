AnekaMolen = ["coklat", "pisang", "nanas", "ketan"]
Minum = ["kopi", "teh", "susu", "jus"]
Gabung = []
Gabung.append(AnekaMolen + Minum)
print(Gabung)

for i in Minum:
    AnekaMolen.append(i)
print(AnekaMolen)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print({f"thisset = {tropical}"})

number = (1, 2, 3, 4, 5, 6, 7,  8, 9, 10)
i = 3
while i < len(number):
    print(number[i])
    i += 2

apollo = {
    "name": "Apollo",
    "age": 21
}
apollo.pop("age")
print(apollo)


myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for subject, valueDict in myfamily.items():
    print(subject)

    for y in valueDict:
        print(y, ":", valueDict[y])
