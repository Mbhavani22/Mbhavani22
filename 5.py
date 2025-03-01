def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(lst)  # Sum of given list
    return expected_sum - actual_sum  # The missing number

# Example usage
n = int(input("Enter the value of n: "))
lst = list(map(int, input("Enter the numbers separated by space: ").split()))

missing_number = find_missing_number(lst, n)
print("The missing number is:", missing_number)
