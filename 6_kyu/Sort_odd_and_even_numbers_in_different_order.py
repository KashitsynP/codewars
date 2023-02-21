# DESCRIPTION:
# You are given an array of integers. Your task is to sort odd numbers within the array in ascending order, and even numbers in descending order.

# Note that zero is an even number. If you have an empty array, you need to return it.

# For example:

# [5, 3, 2, 8, 1, 4]  -->  [1, 3, 8, 4, 5, 2]

# odd numbers ascending:   [1, 3,       5   ]
# even numbers descending: [      8, 4,    2]
####################################################################################################################

# My solution:

def sort_array(a):
    odds = [x for x in a if x % 2 != 0]
    odds.sort()
    evens = [x for x in a if x % 2 == 0]
    evens.sort(reverse=True)
    result = []
    i, j = 0, 0
    for x in a:
        if x % 2 != 0:
            result.append(odds[i])
            i += 1
        else:
            result.append(evens[j])
            j += 1
    return result
    