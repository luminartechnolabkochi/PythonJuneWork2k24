
# create a function is_palindrome(word) return True if word is a palindromic string
# else return False


def is_palindrome(word):

    reversed_str=word[::-1]#reversed_str="madam"

    return word==reversed_str#return "madam"=="madam"

print(is_palindrome("madam"))


# create a function reverse(word) return revesed_string


def reverse(word):

    revesed_str=word[::-1]

    return revesed_str

print(reverse("hello"))






