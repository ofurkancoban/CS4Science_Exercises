# Coding unsigned integers with an arbitrary base
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2
# Height input from user

new_base = int(input("Enter a positive int number as new base (>=2): "))
while new_base < 2:
    print("Numbers cannot be represented by a base <=1: ")
    new_base = int(input("Try again: Enter a positive int number >=2: "))

n = int(input("Enter a positive int number: "))
while n < 0:
    print("I cannot convert negative numbers")
    n = int(input("Try again: Enter a positive int number: "))

if n == 0:
    result = "0"
else:
    result = ""  # initialize String for new representation
    while n > 0:
        digit = n % new_base  # new digit
        if digit < 10:  # convert into feasible digits of new_base
            digitChar = str(digit)  # 0..9: change in String '0',..,'9'
        else:
            digitChar = chr(ord('A') + digit - 10)  # chr(Unicode number of the correct letter)

        print(f"Next digit: {digitChar}")  # printing digit by digit
        n = n // new_base  # Continue with n // new_base in the next iteration

        result = result + digitChar # printing the final t result in one String.

print(f"Result: {result}")
