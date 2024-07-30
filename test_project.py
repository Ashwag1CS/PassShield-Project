from project import parse_date, is_sequential_or_repetitive, rate_password
from colorama import Fore, Style
answers = ["John", "Fluffy", "01/01/1990", "Reading", "Inception", "Pizza"]

# Test cases for parse_date function
def test_parse_date():
    assert parse_date("27/07/2024") == "20240727"
    assert parse_date("07/27/2024") == "20240727"
    assert parse_date("2024-07-27") == "20240727"
    assert parse_date("27-07-2024") == "20240727"

# Test cases for is_sequential_or_repetitive function
def test_is_sequential_or_repetitive():
    assert is_sequential_or_repetitive("123456") is True
    assert is_sequential_or_repetitive("abcdef") is True
    assert is_sequential_or_repetitive("aaaaaaa") is True
    assert is_sequential_or_repetitive("a1b2c3") is False
    assert is_sequential_or_repetitive("Ab1!@#") is False
 
# Test cases for test_rate_password function
def test_rate_password():
    password = "Str0ngP@ssw0rd!"
    actual_strength, actual_feedback = rate_password(password, answers)
    expected_strength = Fore.GREEN + "Strong" + Style.RESET_ALL
    expected_feedback = ""
    assert actual_strength == expected_strength
    assert actual_feedback == expected_feedback

    password = "AshwagB@#751"
    actual_strength, actual_feedback = rate_password(password, answers)
    expected_strength = Fore.GREEN + "Strong" + Style.RESET_ALL
    expected_feedback = ""
    assert actual_strength == expected_strength
    assert actual_feedback == expected_feedback

    password = "Fluffy"
    actual_strength, actual_feedback = rate_password(password, answers)
    expected_strength = Fore.RED + "Weak"
    expected_feedback = "Your password contains personal information from the security questions."+ Style.RESET_ALL
    assert actual_strength == expected_strength
    assert actual_feedback == expected_feedback

    password = "Ab"
    actual_strength, actual_feedback = rate_password(password, answers)
    expected_strength = Fore.RED + "Weak"
    expected_feedback = "Your password is too short. It should be at least 8 characters long."+ Style.RESET_ALL
    assert actual_strength == expected_strength
    assert actual_feedback == expected_feedback

    password = "123456"
    actual_strength, actual_feedback = rate_password(password, answers)
    expected_strength = Fore.RED + "Weak"
    expected_feedback = "Your password contains sequential or repetitive characters."+ Style.RESET_ALL
    assert actual_strength == expected_strength
    assert actual_feedback == expected_feedback

    password = "Jh28935A"
    actual_strength, actual_feedback = rate_password(password, answers)
    expected_strength = Fore.YELLOW + "Medium"
    expected_feedback = "Your password should contain a mix of uppercase, lowercase, digits, and special characters."+ Style.RESET_ALL
    assert actual_strength == expected_strength
    assert actual_feedback == expected_feedback