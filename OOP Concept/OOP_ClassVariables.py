class student:
    num_student = 0
    raise_amount = 1.04 #class variable

    def __init__(self, first, last, fee):
        self.first = first
        self.last = last
        self.fee = fee
        self.email = first + '.'+last +'@gmail.com'

        student.num_student +=1

    def full_name(self):
        return (f'{self.first} {self.last}')

    def apply_raise(self):
        self.fee = int(self.fee * self.raise_amount)



s1 = student('Ravi', 'Kumar', 2000)
s2 = student('Suman', 'patel', 5000)

#print(s1.first)
#print(s1.full_name())
#print(s1.email)
#student.raise_amount = 1.05 #class variable
#s1.raise_amount = 1.05 # instance
#print(s1.raise_amount)
#print(s2.raise_amount)

print(student.num_student)
