def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Example usage
lst = [1, 3, 2, 3, 4, 5, 2, 6, 4, 7, 8, 5]
print("List after removing duplicates:", remove_duplicates(lst))
