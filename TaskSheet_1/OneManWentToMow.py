# Lyrics "One man went to mow"
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

# We assigned variables
current_men_count = 1
countdown_line = ""
num_texts = ("One", "Two", "Three",
             "Four", "Five", "Six", "Seven",
             "Eight", "Nine", "Ten")

# We are getting a positive number of men from the user
while True:
    max_men = int(input("Enter the maximum number of men:"))
    if max_men > 0:
        break
    else:
        print("Please enter a number greater than 0!")

# We are generating and printing lyrics based on the number of men
while current_men_count <= max_men:
    for n in range(current_men_count, 0, -1):
        if n <= len(num_texts):
            men_text = num_texts[n - 1]
        else:
            men_text = str(n)

        if n > 1:
            countdown_line += (f"{men_text} men, ")
        else:
            countdown_line += "one man and his dog, Spot"

    # We are determining the text for the current number of men
    if current_men_count <= len(num_texts):
        current_men_text = num_texts[current_men_count - 1]
    else:
        current_men_text = current_men_count

    if current_men_count == 1:
        print(f"""{current_men_text} man went to mow 
Went to mow a meadow;
{countdown_line}
Went to mow a meadow \n \n """)
    else:
        print(f"""{current_men_text} men went to mow 
Went to mow a meadow;
{countdown_line}
Went to mow a meadow \n \n """)

    # We are resetting countdown line and move to the next number of men
    countdown_line = ""
    current_men_count += 1
