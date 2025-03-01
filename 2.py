from collections import Counter

def most_frequent_element(lst):
    count = Counter(lst)  # Count occurrences of each element
    return count.most_common(1)[0][0]  # Return the most common element

# Example usage
lst = [1, 3, 2, 3, 4, 3, 5, 3, 6, 2, 2, 2, 2]
print("Most frequent element:", most_frequent_element(lst))
