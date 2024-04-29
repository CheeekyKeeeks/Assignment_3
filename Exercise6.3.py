def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]



def is_palindrome(word):
    # Base case: If the word is empty or has one letter, it is a palindrome
    if len(word) <= 1:
        return True
    
    # Check if the first and last letters are the same
    if first(word) != last(word):
        return False
    
    # Recursively check the middle of the word
    return is_palindrome(middle(word))


