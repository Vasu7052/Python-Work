class Man:
    gender = 'male'

    def __init__(self, name):
        self.name = name


r = Man('Robert')
s = Man('Sam')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)