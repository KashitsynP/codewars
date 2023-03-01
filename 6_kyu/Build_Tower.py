# DESCRIPTION:
# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]
####################################################################################################################

# My solution:

def tower_builder(n_floors):
    s = []
    for i in range(1, n_floors + 1):
        s.append(f"{' ' * (n_floors - i) + '*' * (i + i - 1) + ' ' * (n_floors - i)}")
    return s