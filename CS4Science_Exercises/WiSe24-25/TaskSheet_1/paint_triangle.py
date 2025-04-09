# Python Program: Paint a Triangle using a While Statement
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2
# Height input from user
height = int(input("Please enter the height of triangle: "))

# Initialize the row number
row = 0

while row < height:
    stars = 2 * row + 1  # Calculation the number of stars
    spaces = height - row - 1  # Calculate the number of spaces
    print(' ' * spaces + '*' * stars)  # Print the spaces followed by the stars for the current row
    row += 1  # Increment to the next row
