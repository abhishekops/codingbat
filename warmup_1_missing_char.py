# Given a non-empty string and an int n, return a new string where the char at
# index n has been removed. The value of n will be a valid index of a char in
# the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

# Solution 1:
def missing_char(str, n):
    if len(str) == 0:
        return 0
    res = list(str)
    del res[n]
    return ''.join(res)

# Solution 2:
def missing_char(str, n):
    front = str[:n]
    back = str[n+1:]
    return front + back
