fruits = ["apple", "banana", "cherry"]
for x in fruits:
    rec=[x[i] for i in range(len(x))]
    print(tuple(rec))

