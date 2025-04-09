# Python- Hash function
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

def myhash(first_name, last_name):
    """
    Make a simple hash code using a person's first and last name.

    Parameters:
        first_name (str): The person's first name
        last_name (str): The person's last name

    Returns:
        str: The hash code as a string
    """
    # Start with a product of 1 for the first name characters
    unicode_product = 1
    # Go through each letter in the first name and multiply its Unicode value
    for char in first_name:
        unicode_product *= ord(char)

    # Start with a sum of 0 for the last name characters
    unicode_sum = 0
    # Go through each letter in the last name and add its Unicode value
    for char in last_name:
        unicode_sum += ord(char)

    # Convert both numbers to strings and put them together
    hash_value = str(unicode_product) + str(unicode_sum)
    return hash_value

def main():
    # Ask the user to enter a first name and a last name
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")

    # Calculate the hash value for the names
    hash_code = myhash(first_name, last_name)

    # Print the result in the requested format
    print(f'The hash code "{hash_code}" corresponds to "{first_name} {last_name}".')

# Run the main function to start the program
if __name__ == "__main__":
    main()

