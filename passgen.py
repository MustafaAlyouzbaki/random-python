# Password Generator
# by Mustafa Al-Youzbaki

# Character Sets
char_lower = "abcdefghijklmnopqrstuvwxyz"
char_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_nums = "0123456789"
char_special = ".,;:'][}{)(_~-+=|/!@#$%^&*"

def main():
    print("Password Generator by Mustafa Al-Youzbaki\n\n")
    choice = input("Would you like to generate a password? (Y/N) ")
    if choice.lower() == 'y':
        # Length input
        validLength = False
        while not validLength:
            length = int(input("Enter the length that you want your password to be: "))
            if length > 0 and length < 100:
                validLength = True
            else:
                print("Invalid length. Please enter a number between 1 and 99.")

        # Number of passwords input
        num_passwords = int(input("How many passwords would you like to generate? "))

        # Character preference input
        choice = input("Would you like a standard password with all characters? (Y/N) ")
        if choice.lower() == 'y':
            # All characters included
            for i in range(num_passwords):
                password = generatePassword(length, True, True, True, True)
                print(f"Generated Password {i+1}: {password}")
        else:
            # Custom character preference
            lower = input("Include lowercase letters? (Y/N) ").lower() == 'y'
            upper = input("Include uppercase letters? (Y/N) ").lower() == 'y'
            nums = input("Include numbers? (Y/N) ").lower() == 'y'
            special = input("Include special characters? (Y/N) ").lower() == 'y'
            for i in range(num_passwords):
                password = generatePassword(length, lower, upper, nums, special)
                print(f"Generated Password {i+1}: {password}")
    else:
        print("Exiting the program.")

def generatePassword(length, lower, upper, nums, special):
    """
    Function 'generatePassword' generates a password based
    on the length and character input from the user.
    """
    import random
    characters = ""
    if lower:
        characters += char_lower
    if upper:
        characters += char_upper
    if nums:
        characters += char_nums
    if special:
        characters += char_special
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    main()