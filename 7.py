def count_vowels(s):
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    return sum(1 for char in s if char in vowels)

# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
