# Python Program: Paint a Triangle using a While Statement
# Coban, Omer Furkan
# SoSe 24/25
# CS4Science - Team B2

initial = 0
height = int(input("Enter height of triangle: "))

while initial < height:
    stars = 2 * initial + 1
    spaces = height - initial - 1
    print(" " * spaces + "*" * stars)
    initial = initial + 1
