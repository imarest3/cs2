def count_char(s, char):
    # Complete
    count = 0
    if not s:
        return 0
    

    count = 1 if s[0] == char else 0

    rest_count = count_char (s[1:], char)


    return count + rest_count
    

if __name__ == "__main__":
    input_string = input("Enter the string: ")
    input_char = input("Enter the character to count: ")
    print(f"'{input_char}' appears", count_char(input_string, input_char), "times.")
