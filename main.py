import random
import string
import time
import colorama
from colorama import init, Fore, Back, Style

init(autoreset=True)

error = f"{colorama.Fore.RED}"                  # Error
notif = f"{colorama.Fore.BLUE}"                 # Notification
warn = f"{colorama.Fore.YELLOW}"                # Warning
scess = f"{colorama.Fore.GREEN}"                # Success
end = f"{colorama.Style.RESET_ALL}"             # Reset all styles

print(f"Random Password Generator v.1.0 ∙ {notif}If program stucks press Ctrl+C (without selected text) to exit")

def generate_random_password(length=12):

        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def execute():

        try:

            password_length = int(input("\nEnter the desired password length: "))
            
            if password_length > 1:

                password = generate_random_password(password_length)
                print(f"{scess}Generated Password: {password}")

            else:

                print(f"{warn}Length of password must be more than 1 symbol")

        except ValueError:

            print(f"{warn}Please, enter the length in numbers")

if __name__ == "__main__":
    
    ask_to_continue = "Y"

    while True:

        if ask_to_continue.lower() == "y":
            
            try:
                
                execute()
                ask_to_continue = input("Make another one? (Y/N): ")

            except ValueError:

                print(f"{warn}Type Y for yes or N for no")

        elif ask_to_continue.lower() == "n":

            print(f"{notif}\nProgram will exit in few seconds")
            time.sleep(2)
            break

        else: 
            
            print(f"{warn}Type Y for yes or N for no")
            ask_to_continue = input("Make another one? (Y/N): ")
