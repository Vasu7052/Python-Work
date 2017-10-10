class Parent:
    def print_last_name(self):
        print('Roberts')


class Child(Parent):
    def print_first_name(self):
        print('Bucky')

    def print_last_name(self):
        print('Snitzleberg')


vasu = Child()
vasu.print_first_name()
vasu.print_last_name()