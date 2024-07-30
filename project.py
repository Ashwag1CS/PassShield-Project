import re
from datetime import datetime
from pyfiglet import Figlet
from colorama import Fore, Style
import cowsay

# List of common security questions
questions = [
    "What's your name?",
    "What's the name of your first pet?",
    "When were you born?",
    "What's your favorite hobby?",
    "What is your favorite movie?",
    "What is your favorite food?"
]
#Asks the user a set of common questions and returns their answers.
def ask_questions():
    answers = []
    for question in questions:
        answer = input(question + " ")
        answers.append(answer)
    return answers
#Tries to parse a date string into a standard format.
def parse_date(date_str):
    date_formats = ["%d/%m/%Y", "%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y"]
    for date_format in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, date_format)
            return parsed_date.strftime("%Y%m%d")
        except ValueError:
            continue
    return None
#Checks if the password contains sequential numbers/letters or repetitive characters.
def is_sequential_or_repetitive(password):
    sequences = ["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"[::-1], 
                 "0123456789", "9876543210"]
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password.lower():
                return True

    if len(set(password)) == 1:  # Repetitive characters
        return True

    return False

def rate_password(password, answers):
    """Rates the strength of the password based on the user's answers."""
    lower = re.compile(r'[a-z]')
    upper = re.compile(r'[A-Z]')
    digit = re.compile(r'[0-9]')
    special = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    
    # Check if password contains any answer
    for answer in answers:
        answer_lower = answer.lower()
        parsed_date = parse_date(answer)
        if parsed_date and parsed_date in password:
            return (Fore.RED + "Weak", "Your password contains your birth date from the security questions." + Style.RESET_ALL)
        if re.search(re.escape(answer_lower), password.lower()):
            return (Fore.RED + "Weak", "Your password contains personal information from the security questions." + Style.RESET_ALL)
    
    # Check for sequential or repetitive characters
    if is_sequential_or_repetitive(password):
        return (Fore.RED + "Weak", "Your password contains sequential or repetitive characters." + Style.RESET_ALL)

    # Check for length and variety of characters
    if len(password) < 8:
        return (Fore.RED + "Weak", "Your password is too short. It should be at least 8 characters long." + Style.RESET_ALL)
    elif not lower.search(password) or not upper.search(password) or not digit.search(password) or not special.search(password):
        return (Fore.YELLOW + "Medium", "Your password should contain a mix of uppercase, lowercase, digits, and special characters." + Style.RESET_ALL)
    
    return (Fore.GREEN + 'Strong' + Style.RESET_ALL, "")

#Main function to manage the flow of asking questions, getting a password, and providing feedback.
def main():
    print(Style.RESET_ALL)
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font="larry3d")
    print(figlet.renderText("PassShield"))
    print("-"*77)
    print('Hi this is PassShield system, a system that helps you to create a strong and')
    print('secure password by asking several questions then rating the password you input.')
    print("-"*77)

    answers = ask_questions()
    print(Style.RESET_ALL)
    while True:
        password = input("Please enter a password: " + Style.RESET_ALL)
        strength, feedback = rate_password(password, answers)
        print(f"Your password is rated as: {strength}")
        print(feedback)

        if "Strong" in strength:
            print(Fore.GREEN +"Your password is strong and may be used." + Style.RESET_ALL)
            cowsay.cow('Remember! Avoid reusing passwords and never share them with anyone.')
            break
        elif "Medium" in strength:
            regenerate = input("This password isn't strong enough. Do you wnat to Try a different one?. (yes/no) " + Style.RESET_ALL).lower()
            if regenerate != 'yes':
                cowsay.cow('Remember! Avoid reusing passwords and never share them with anyone.')
                break
        else:
            print("Please try a different password." + Style.RESET_ALL)

          

if __name__ == "__main__":
    main()
