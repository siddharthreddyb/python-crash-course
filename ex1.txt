  # check if a number is positive or negative in python:
# method1:
# Using brute force
a = 15
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("zero")

# method2:
# using nested if-else statement

num = 15
if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")

# method3
# using ternary operator:

num = 15
print("positive" if num>=0 else "negative")

