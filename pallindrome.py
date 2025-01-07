# this code is for word to check palindrome or not
user_input = input("Enter the word to check it is palindrome or not palindrome. ")

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

if is_palindrome(user_input):
    print(f"The word '{user_input}' is a palindrome.")
else:
    print(f"The word '{user_input}' is not a palindrome.")    

# this code for the number to check palindrome or not
user_input = (input("Enter the number that you want to check it is palindrome or not a palindrome. "))

def is_palindrome(number):

    return str(number) == str(number[::-1])

if is_palindrome(user_input):
    print(f"The number '{user_input}' is a palindrome.")
else:
    print(f"The number '{user_input}' is not a palindrome.")

