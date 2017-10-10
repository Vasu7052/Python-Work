class Fruits :

    num = 0

    def __init__(self, x):
        print("Init called")
        self.num = x

fruits = Fruits(8)
print(fruits.num)