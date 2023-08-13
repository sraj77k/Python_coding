# 1. Write a code to reverse a number

num = int(input("Enter the number: "))
temp = num
reverse = 0
while num > 0:
    reminder = num % 10
    reminder = (reminder * 10) + reminder
    num = num // 10
print(f"The given reminder is {temp} and reversed is {reverse}")
