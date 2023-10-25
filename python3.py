def generate_binary_series(start, end):
    if start < 0 or end < start:
        print("The range specified is invalid.")
        return

    current = start
    while current <= end:
        print(current)
        current += 2

# Ask user to put a range
start = int(input("enter the start of the range : "))
end = int(input("Enter the end of the range : "))

generate_binary_series(start, end)

