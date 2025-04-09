# Noisy Animals
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

# Ask user to enter an animal
animal = input("What kind of animal do you have? ")

# Using if-elif-else to determine the animal noise
if animal == "dog":
    print("A dog makes 'wuff'.")
elif animal == "cat":
    print("A cat says 'meow'.")
elif animal == "bird":
    print("A bird sings 'piep'.")
elif animal == "sheep":
    print("A sheep says 'baa'.")
elif animal == "cow":
    print("A cow says 'moo'.")
# If the animal is not known, print an unknown message
else:
    print(f"I do not know what kind of noise a {animal} makes.")