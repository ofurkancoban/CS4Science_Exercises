# Print your UniCode Table - but with a for-loop instead of a while loop
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

# Get user inputs for start and end Unicode values and max characters per line
c_start = int(input("Enter the number where your UniCode table shall start: "))
c_end = int(input("Enter the number where your UniCode table shall stop: "))
max_char_in_line = int(input("How many characters shall be in one line: "))

char_counter = 0  # Counter for characters in the current line
table = ""  # String to build the Unicode table

# Use a for-loop to iterate from c_start to c_end (inclusive)
for c_num in range(c_start, c_end + 1):  # Inclusive range
    if char_counter == 0:  # Start a new line if no characters are in the current line
        table += f"\n{c_num}:"
    table += f"\t{chr(c_num)}"  # Append the character for the current Unicode
    char_counter = (char_counter + 1) % max_char_in_line  # Update the character count for line breaks

# Print the resulting Unicode table
print(table)
