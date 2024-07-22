def generate_subsets(lst):
    # Complete

if __name__ == "__main__":
    count = int(input("How many elements? "))
    elements = []
    for i in range(count):
        elements.append(int(input(f"Element {i+1}: ")))
    print("Subsets:", generate_subsets(elements))
