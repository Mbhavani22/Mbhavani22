def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)  


lst1 = list(map(int, input("Enter first sorted list: ").split()))
lst2 = list(map(int, input("Enter second sorted list: ").split()))

print("Merged sorted list:", merge_sorted_lists(lst1, lst2))
