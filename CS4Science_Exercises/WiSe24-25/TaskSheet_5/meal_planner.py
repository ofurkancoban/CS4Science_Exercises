# Meal Planner for Allergic Friends
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

def lst2str(mylist):
    """
    Converts a list to a CSV-style string.
    Parameters:
        mylist (list): The list to convert.
    Returns:
        str: The list elements as a comma-separated string.
    """
    mystring = ", ".join(mylist)
    return mystring

def read_dict_from_file(filename):
    """
    Reads a dictionary of friends and their allergies from a CSV file.
    Parameters:
        filename (str): Path to the CSV file.
    Returns:
        dict: Dictionary with friends' names as keys and allergy lists as values.
    """
    allgy_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            name, allergies = line.strip().split(":")
            allgy_dict[name.capitalize()] = [allergy.strip() for allergy in allergies.split(",") if allergy]
    return allgy_dict

def read_friends_names():
    """
    Reads friends' names and initializes their allergy lists, either manually or from a file.
    Returns:
        dict: Dictionary of friends' names and their allergies.
    """
    answer = input("Enter the name of a CSV file with allergy information to be loaded or enter x for manual input: ").strip()
    if answer.lower() == "x":  # manual input
        print("Enter the names of your friends manually: ")
        allgy_dict = {}
        while True:
            name = input("Please enter another friend's name (or x to abort): ").capitalize()
            if name.lower() == "x":
                break
            allgy_dict[name] = []  # initialize with no known allergies
        return allgy_dict
    elif answer:  # check if the input is not empty
        try:
            return read_dict_from_file(answer)
        except FileNotFoundError:
            print(f"Error: File '{answer}' not found. Please try again.")
            return read_friends_names()  # recursively ask for input again
    else:
        print("No input provided. Please try again.")
        return read_friends_names()  # recursively ask for input again


def print_friends(fdict):
    """
    Prints each friend and their allergies in a readable format.
    Parameters:
        fdict (dict): Dictionary of friends and their allergies.
    """
    for name, allergies in fdict.items():
        print(f"{name} has the allergies: {lst2str(allergies)}.")

def choose_friend(fdict):
    """
    Prompts the user to choose a friend from the dictionary.
    Parameters:
        fdict (dict): Dictionary of friends and their allergies.
    Returns:
        str: The name of the chosen friend.
    """
    namestext = ", ".join(fdict.keys())
    print(f"Your (other) known friends are {namestext}.")
    while True:
        chosenname = input("Name of the friend: ").capitalize()
        if chosenname in fdict:
            return chosenname

def alter_allergies(name, allergies):
    """
    Allows the user to modify a friend's allergy list by adding or removing allergies.
    Parameters:
        name (str): The friend's name.
        allergies (list): List of the friend's allergies.
    """
    while True:
        action = input(f"Do you want to add (A) or delete (D) an allergy of {name} or abort (x): ").lower()
        if action == "x":
            break
        elif action == "a":
            algy = input(f"Enter {name}'s next allergy: ").lower()
            if algy not in allergies:
                allergies.append(algy)
        elif action == "d":
            print(f"{name} is allergic to {lst2str(allergies)}.")
            algy = input(f"{name} has recovered from which allergy: ").lower()
            if algy in allergies:
                allergies.remove(algy)

def write_file(filename, a_dict):
    """
    Writes the dictionary of friends and their allergies to a file.
    Parameters:
        filename (str): The file to write to.
        a_dict (dict): Dictionary of friends and their allergies.
    """
    with open(filename, "w") as file:
        for name, allergies in a_dict.items():
            line = f"{name}:{','.join(allergies)}\n"
            file.write(line)

def invite_friends(fdict):
    """
    Allows the user to select friends to invite from the dictionary.
    Parameters:
        fdict (dict): Dictionary of friends and their allergies.
    Returns:
        list: List of invited friends' names.
    """
    invited = []
    remaining_friends = set(fdict.keys())
    while remaining_friends:
        print(f"Your (other) known friends are {', '.join(remaining_friends)}.")
        name = input("Name of the friend: ").capitalize()
        if name in remaining_friends:
            invited.append(name)
            remaining_friends.remove(name)
        else:
            print("Invalid name.")
        if not remaining_friends or input("Do you want to invite another friend? (y/n): ").lower() == "n":
            break
    return invited

def calculate_allergies_union(fdict, invited):
    """
    Calculates the union of allergies of the invited friends.
    Parameters:
        fdict (dict): Dictionary of friends and their allergies.
        invited (list): List of invited friends' names.
    Returns:
        set: Union of allergies of the invited friends.
    """
    all_allergies = set()
    for name in invited:
        all_allergies.update(fdict[name])
    return all_allergies

# Main program
allgy_dict = read_friends_names()

while input("Do you want to alter a friend's allergies? (y/n): ").lower() == "y":
    friend_name = choose_friend(allgy_dict)
    alter_allergies(friend_name, allgy_dict[friend_name])

print_friends(allgy_dict)

if input("Do you want to save the data to a file? (y/n): ").lower() == "y":
    filename = input("Enter the filename to save: ")
    write_file(filename, allgy_dict)

invited_friends = invite_friends(allgy_dict)
menu_allergies = calculate_allergies_union(allgy_dict, invited_friends)
print(f"In the menu for your friends avoid: {lst2str(list(menu_allergies))}.")
