import random

def key_signature():

    dct = {"C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,
           "F": 1, "B♭": 2, "E♭": 3, "A♭": 4, "D♭": 5, "G♭": 6, "C♭": 7,
           "a": 0, "e": 1, "b": 2, "f#": 3, "c#": 4, "g#": 5, "d#": 6, "a#": 7,
           "d": 1, "g": 2, "c": 3, "f": 4, "b♭": 5, "e♭": 6, "a♭": 7}

    print("Guess how many accidentals a key has. To exit, type 'exit'.")
    choice = random.choice(list(dct.keys()))
    user = input("Key: " + choice)
    while user.lower() != "exit":
        while not user.isdigit() or int(user) < 0 or int(user) > 7:
            print("Please choose a number between 0 and 7.")
            user = input("Key: " + choice + ": ")      
        if user == str(dct[choice]):
            if dct[choice] == 1:
                print("That's right! " + choice + " has " + user + " accidental.")
            else:
                print("That's right! " + choice + " has " + user + " accidentals.")
        else:
            if dct[choice] == 1:
                print("Incorrect. " + choice + " has " + str(dct[choice]) + " accidental.")
            else:
                print("Incorrect. " + choice + " has " + str(dct[choice]) + " accidentals.")
        choice = random.choice(list(dct.keys()))
        user = input(choice + ": ")

key_signature()
