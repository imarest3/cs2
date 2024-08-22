def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()  # Keep only alphanumeric characters and convert them to lower case
    def helper(s, left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        
        return helper(s, left +1, right -1)
    
    return helper(s, 0, len(s)-1)

# List of test cases
test_cases = [
    ("Noon", True),
    ("Madam", True),
    ("Radar", True),
    ("Racecar", True),
    ("No lemon, no melon", True),
    ("Never odd or even", True),
    ("A man, a plan, a canal, Panama", True),
    ("Hello", False),
    ("Starman", False),
    ("Blitzkrieg Bop", False)
]

# Running test cases
for text, expected in test_cases:
    result = is_palindrome(text)
    print(f'Is "{text}" a palindrome? {result} (Expected: {expected})')