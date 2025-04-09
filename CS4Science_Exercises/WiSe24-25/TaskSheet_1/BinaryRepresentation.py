# Code an unsigned value in binary representation
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2


new_base = 2
n = int(input("Please enter a positive int number: "))
n_original = n
while n < 0 :
    print("Try again! You entered a negative number.")
    n = int(input("Try again: Enter a positive int number: "))

if n == 0:
    result = "0"
else:
    result = ""
    while n > 0:
        digit = n % new_base
        print(f"Next digit: {digit}")
        n = n // new_base
        result = str(digit) + result

print(f"The representation of {n_original} in base {new_base} is: {result}.")