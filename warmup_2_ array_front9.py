# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

# Solution 1:
def array_front9(nums):
    it = len(nums) if len(nums) <= 4 else 4
    for i in range(it):
        if nums[i] == 9:
            return True
    return False

# Solution 2:
def array_front9(nums):
    num = 9
    index = nums.index(9) if num in nums else -1
    if 0 <= index < 4:
        return True
    else:
        return False
