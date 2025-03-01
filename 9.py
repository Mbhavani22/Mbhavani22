def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))   


lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))

print("Common elements:", list_intersection(lst1, lst2))
