# Script which manages the allergies of my friends


def lst2str(mylist):
    # just a helper function which converts a given list in a csv-String
    mystring = [item + ", " for item in mylist]
    return mystring[:-2]

def read_dict_from_file(filename): 
    print("This function hasn't been implemented yet")
    return {} # empty dictionary

def read_friends_names():
    # read the friends' names from file or manually:
    answer = input("Enter the name of a csv-file with allergy information to be loaded or enter x for manual input): ")
    if answer in "xX": # manual input
        print("Enter the names of your friends manually: ")
        name ="No one"  # invalid name , just to get the variable initialised
        allgy_dict = {}
        while name != "X":
            name = input("Please enter another friend's name (or x to abort):")
            name = name.capitalize()
            if name != "X":
                allgy_dict[name] = [] # so far no allergy of this friend is known
        return allgy_dict
    else: # read the friends' names from file 
        return read_dict_from_file(answer)

    
def print_friends(fdict):
    for name in fdict:
        print(f"{name} has the allergies: {fdict[name]}.")
    
def choose_friend(fdict):
    namestext = ""
    for item in fdict.keys():
        namestext += item + ", "
    print(f"Your (other) known friends are {namestext[:-2]}. ")  
    chosenname = "some invalid name"
    while chosenname not in fdict:
        chosenname = input("Name of the friend: ")
        chosenname = chosenname.capitalize()
    return chosenname

def alter_allergies(name, allergies):
    answer =input(f"Do you want to add (A) or delete (D) an allergy of {name} or abort (x): ")
    answer = answer.lower()
    while answer not in "Xx":
        if answer in "aA":
            algy = input(f"Enter {name}'s next allergy: ").lower()
            allergies.append(algy)
        elif answer in "dD":
            print(f"{name} is allergic against {allergies}.")
            algy = input(f"{name} has recovered from which allergy: ")
            allergies.remove(algy.lower())
        answer =input(f"Do you want to add (A) or delete (D) an allergy of {name} or abort (x): ")
    
def write_file(filename, a_dict):
    with open(filename,"w") as file:
        for name in a_dict: #build a String of this friend's information, starting with name + ":"
            line = str(name)+":" 
            for algy in a_dict[name]:
                line += str(algy) + ","
            line = line[:-1] +"\n" # everything, but the last ",", but add a newline
            file.write(line)

    
## main program ###

# Read all friends'names and initialize the allergy dictionary 
allgy_dict = read_friends_names()

# loop which let you choose friends and modify their allergies
answer = input("Do you want to alter a friends allergies? (y/n)")
while answer not in "nN":
    friend_name = choose_friend(allgy_dict)
    alter_allergies(friend_name, allgy_dict[friend_name])
    answer = input("Do you want to alter another friends allergies? (y/n)")

print_friends(allgy_dict)

# write the current dictionary to file...

# list of invite friends...

# list of allergies to be taken into account...