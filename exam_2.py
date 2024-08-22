def all_positive(lst, index=0):
    #if len (lst) == 0:
     #   return False
    
    if not lst:
        return False
        
    
    elif index == len(lst):
        return True
    elif lst[index] <= 0:
        return False
    else:
        return all_positive(lst, index + 1)

# Test case variables
test_case_1 = [1, 2, 3, 4, -5]
test_case_2 = [7, 2, 11, -8, 17]
test_case_3 = [9, 8, 6, 2, 3]
test_case_4 = []
test_case_5 = [-1]
test_case_6 = []

# Test cases
print('Are all elements in', test_case_1, 'positive?', all_positive(test_case_1))
print('Are all elements in', test_case_2, 'positive?', all_positive(test_case_2))
print('Are all elements in', test_case_3, 'positive?', all_positive(test_case_3))
print('Are all elements in', test_case_4, 'positive?', all_positive(test_case_4))
print('Are all elements in', test_case_5, 'positive?', all_positive(test_case_5))
print('Are all elements in', test_case_6, 'positive?', all_positive(test_case_6))