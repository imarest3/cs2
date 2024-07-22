def is_symmetric(lst, start, end):
    # Complete
    if len (lst)
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    elements = []
    for i in range(n):
        elements.append(int(input(f"Element {i+1}: ")))
    print("The list is symmetric:", is_symmetric(elements, 0, len(elements) - 1))
