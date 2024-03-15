# method1
# Using Brute Force
# check whether a number is even or odd in python:
num = int(input("enter a number:"))
if num % 2 == 0:
    print("given number is even")
else:
    print("given number is odd")

# Method 2 : Using Ternary Operator
num = 1816
print("even") if num%2 == 0 else print("odd")


# Method 3 : Using Bitwise Operator
def isEven(num):
  return not num&1

if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')

