"""
If it's cold (temp<12):
Stay inside
Play  chess
else:
If it's windy (velo>10):
Play soccer
Else:
Play badminton
print: It's warm outside.
"""

temp = int(input("Enter the temperature "))
velo = int(input("Enter the velocity "))

if temp < 12 :
    print("Stay inside")
    print("Play  chess")
else:
    if velo >10:
        print("Play soccer")
    else:
        print("Play badminton")
    print("It's warm outside")