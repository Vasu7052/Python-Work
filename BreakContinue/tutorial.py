
for x in range(5) :
    if x is 2 :
        print(x  , "is the required number" , "Yeah")
        break
    else:
        print(x)

print("=========================")

for x in range(5) :
    if x is 2 :
        print(x  , "is the required number" , "Yeah")
        continue
        print("This will not show")
    else:
        print(x)