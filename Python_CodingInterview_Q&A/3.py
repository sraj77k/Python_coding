# 3. Write code of Greatest Common Divisor

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


def gcdFunction(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1

    for i in range(1, small + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = 1
        print(f"GCD of two number is {gcd}")
    gcdFunction(num1, num2)
