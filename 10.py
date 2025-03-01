from collections import Counter

def first_non_repeating_char(s):
    count = Counter(s)  
    for char in s:
        if count[char] == 1:
            return char  
    return "No non-repeating character found"


string = input("Enter a string: ")
print("First non-repeating character:", first_non_repeating_char(string))
