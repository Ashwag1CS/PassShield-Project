# PassShield
#### This is Final CS50 python project 
#### Video Demo:  <[URL HERE](https://youtu.be/JsiPX1lXzBs?si=hJpnALX4HutqSIfV)>
#### Description:
**PassShield** is a system designed to help users create strong and secure passwords. The system guides the user through a series of questions and then provides feedback on the strength of the password they choose. This System can be used in websites when the user enter personal info before the password section. Here's how it works:
1. **Questionnaire**:
   - The system asks the user a series of predefined security questions. These questions are common and might include:
     - What's your name?
     - What's the name of your first pet?
     - When were you born?
     - What's your favorite hobby?
     - What is your favorite movie?
     - What is your favorite food?
   - The user inputs their answers to these questions. 

2. **Password Entry**:
   - After answering the questions, the user is prompted to enter a password.

3. **Password Evaluation**:
   - The system evaluates the password based on several criteria:
     - **Length and Complexity**: The password must be at least 8 characters long and include a mix of uppercase letters, lowercase letters, digits, and special characters.
     - **Personal Information**: The system checks if the password contains any of the answers provided by the user in the security questions, including converted date formats.
     - **Sequential and Repetitive Patterns**: The system checks if the password contains sequential numbers or letters, repetitive characters, or common keyboard patterns.

4. **Feedback**:
   - The system rates the password as "Weak," "Medium," or "Strong" and provides specific feedback:
     - If the password is **Weak**, the user is informed of the reason (e.g., it contains personal information or is too simple) and prompted to enter a new password.
     - If the password is **Medium**, the user is advised that the password is okay but could be improved. The user can choose to try again or accept the medium-strength password.
     - If the password is **Strong**, the user is informed that the password is strong and can be used.

**PassShield** aims to educate users on good password practices and ensure that their passwords are robust and secure against common vulnerabilities. By guiding users through the process and providing detailed feedback, the system helps enhance overall cybersecurity.

# Files:
## 1.project.py
The project file conatins the project code , with 5 different functions 

1. First the ask_questions() function:

    This function prompts the user to answer a series of predefined security questions.

    How its work?
    - Iterates over each question in the questions list.
    - Collects the user's responses and stores them in the answers list.
    - Returns the list of answers.

2. Second the parse_date(date_str):

    This function tries to parse a date string into a standard format

    How its work?
    - Attempts to convert the input date_str using various date formats.
    - If a valid format is found, it returns the date in YYYYMMDD format.

3. Third the is_sequential_or_repetitive(password):

    This function checks if the password contains sequential numbers/letters or repetitive characters.

    How its work?
    - Checks for sequential sequences (both forward and backward) in the password.
    - Checks if all characters in the password are the same.
    - Returns True if the password is sequential or repetitive, False otherwise.

4. Fourth the rate_password(password, answers):

    This function rates the strength of the password based on the user's answers.

    How its work?
    - Uses regular expressions to check for the presence of lowercase, uppercase, digit, and special characters.
    - Ensures the password doesn't contain any answers to the security questions, including parsed dates.
    - Rates the password as "Weak", "Medium", or "Strong" and provides appropriate feedback.

5. Lastly the main() function:

    This is the main function that manages the flow of the program.

    How its work?
    - Displays a welcome message using pyfiglet to render "PassShield" in ASCII art and an introduction to the system.
    - Calls ask_questions() to get the user's answers.
    - Continuously prompts the user to enter a password and rates it using rate_password().
    - Provides feedback based on the password strength:
    - If "Strong", confirms the password can be used and displays a reminder using cowsay.
    - If "Medium", asks if the user wants to try again or accept the password.
    - If "Weak", prompts the user to try a different password until a satisfactory password is entered.

## 2.test_project.py
This file conatin the tests function , that tests the function in the project file.

## 3.requirements.txt
this contain any installistion libraries that the project requires. 
    
