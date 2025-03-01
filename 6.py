def second_largest(lst):
    first, second = float('-inf'), float('-inf')
    
    for num in lst:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else "No second largest element"

# Example usage
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Second largest number:", second_largest(lst))
