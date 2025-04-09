# Using the debugging mode
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

# Determining the largest value in a list

# Define a tuple of 11 values
valueList = (12, 21, 23, 2.71, 42, 37, 0, -12, '10', 24, 3.14)

# Initialize index to 0
index = 0

# Convert all elements to float for consistent comparison
valueList = tuple(float(x) for x in valueList)

# Initialize maxi with the first element of the tuple
maxi = valueList[index]

# Iterate through the tuple
while index < len(valueList):
    # Check if the current element is greater than maxi
    if valueList[index] > maxi:
        # Update maxi
        maxi = valueList[index]
    # Increment index
    index += 1

# Print the largest element in the sequence
print(f"The largest element in the sequence is {maxi}.")
