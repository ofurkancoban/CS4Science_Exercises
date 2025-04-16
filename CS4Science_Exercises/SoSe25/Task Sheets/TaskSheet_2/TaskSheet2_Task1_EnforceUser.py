# Enforce the user to enter certain values
# Coban, Omer Furkan
# SoSe 24/25
# CS4Science - Team B2

while True:
    UserInput = int(input("Please enter a value in the range of 0..10: "))

    if 0 <= UserInput <= 10:
         print(f"You have entered {UserInput} which is in the range of 0..10 - Thank you!")
         break
    else:
         print(f"{UserInput} is out of range - Please try again!")