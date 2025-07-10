def divide(a,b):
    return a/b
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
try:
    answer=divide(a,b)
    print(answer)
except ZeroDivisionError:
    print("You can't divide by zero")