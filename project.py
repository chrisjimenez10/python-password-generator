#Password Generator: The anti-hacker program
import random

def passwordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    while True:
        password = ""
        while True:
            nr_letters= input("How many letters would you like in your password?\n")
            try:
                nr_letters = int(nr_letters)
                for char in range(1, nr_letters + 1):
                    password += letters[random.randint(0, len(letters) - 1)]
                break
            except ValueError:
                print("Please provide a valid integer number")

        while True:
            nr_numbers = input(f"How many numbers would you like?\n")
            try:
                nr_numbers = int(nr_numbers)
                for char in range(1, nr_numbers + 1):
                    password += numbers[random.randint(0, len(numbers) - 1)]
                break
            except ValueError:
                print("Please provide a valid integer number")
        
        while True:
            nr_symbols = input(f"How many symbols would you like?\n")
            try:
                nr_symbols = int(nr_symbols)
                for char in range(1, nr_symbols + 1):
                    password += symbols[random.randint(0, len(symbols) - 1)]
                break
            except ValueError:
                print("Please provide a valid integer number")

        #Here, we are converting the password string into a list --> So we can use the shuffle() function
        list_version_password = list(password)
        #Here, we use the shuffle() function from the Random Module to rearrange the items in the List randomly
        random.shuffle(list_version_password)
        #Here, we are converting the List BACK into a String with the .join() method --> NOTE: The join() is preceded by the separator we want in between each character inside a set of quotes (If empty, nothing in between characters)
        new_unhackable_password = "".join(list_version_password)
        print(F"Your unhackable password is: {new_unhackable_password}")

        generate_new_password = input("Do you want to generate a new password? Press Y for a new password or anything else to exit:\n").lower()
        if generate_new_password != "y":
            print("Exiting...")
            break

passwordGenerator()