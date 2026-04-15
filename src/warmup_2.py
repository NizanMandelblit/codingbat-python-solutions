def string_times(str, n):
    """
    Given a string and a non-negative int n, return a larger string that is n
    copies of the original string.
    """
    str *= n
    return str


def front_times(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
    """
    front = str[:3]
    res = front*n
    return res


def string_bits(str):
    """"
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
    """
    res = ""
    i = 0
    for c in str:
        if i % 2 == 0:
            res += c
        i = i + 1
    return res


def string_splosion(str):
    """"
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    """
    res = ""
    for i in range(len(str) + 1):
        res += str[:i]
    return res


def last2(str):
    """"

    Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
    """
    pattren = str[-2:]
    count = 0
    for i in range(len(str)-2):
        if str[i:i+2] == pattren:
            count = count + 1
    return count


def array_count9(nums):
    """"
    Given an array of ints, return the number of 9's in the array.
    """
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


def array_front9(nums):
    """
    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

    """
    cntr = 0
    for num in nums:
        if num == 9 and cntr < 4:
            return True
        cntr += 1
    return False


def array123(nums):
    """
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

    """
    streak = 0
    for num in nums:
        if num == streak+1:
            streak += 1
            if streak == 3:
                return True
        elif num == 1:
            streak = 1
        else:
            streak = 0

    return False


def string_match(a, b):
    # Figure which string is shorter.
    shorter = min(len(a), len(b))
    count = 0

    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count = count + 1

    return count
