#class and Instance vaiable
class student:
    def __init__(self, first, last, roll):
        self.first = first
        self.last = last
        self.roll = roll
        self.email = first + '.'+last +'@gmail.com'

    def full_name(self):
        return (f'{self.first} {self.last}')



s1 = student('Ravi', 'Kumar', 2)
s2 = student('Suman', 'patel', 5)

print(s1.first)
print(s1.full_name())
print(s1.email)

