# User-friendly input of Date and Time - using functions
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2
def convert_date_to_tuple(date_str):
    """
    Converts a date string in format yyyy-mm-dd to a tuple of integers (yyyy, mm, dd).
    """
    try:
        year, month, day = map(int, date_str.split('-'))
        return year, month, day
    except ValueError:
        print("Invalid date format. Please use yyyy-mm-dd.")
        return None


def convert_time_to_tuple(time_str):
    """
    Converts a time string in format hh:mm to a tuple of integers (hh, mm).
    """
    try:
        hour, minute = map(int, time_str.split(':'))
        return hour, minute
    except ValueError:
        print("Invalid time format. Please use hh:mm.")
        return None


def main():
    """
    Main function to interact with the user and display the result.
    """
    # Ask for user input
    date_input = input("Please enter the date of the first measurement (format yyyy-mm-dd): ")
    time_input = input("Please enter the time of the first measurement (format hh:mm): ")

    # Convert date and time to tuples
    date_tuple = convert_date_to_tuple(date_input)
    time_tuple = convert_time_to_tuple(time_input)

    if date_tuple and time_tuple:
        # Combine date and time tuples into a single tuple
        result = date_tuple + time_tuple
        print(f"Result of {date_input} {time_input} is {result}")
    else:
        print("Failed to parse date or time. Please try again with correct formats.")


# Run the main program
if __name__ == "__main__":
    main()
