def find_min(lst):
    # Complete
    if len(lst) == 1:
        return lst[0]
    
    rest_min = find_min(lst[1:])
    if lst[0] < rest_min:
        return lst[0]
    else:
        return rest_min
if __name__ == "__main__":
    count = int(input("Enter the number of elements: "))
    elements = []
    for i in range(count):
        elements.append(int(input(f"Element {i+1}: ")))
    print("The minimum is:", find_min(elements))
