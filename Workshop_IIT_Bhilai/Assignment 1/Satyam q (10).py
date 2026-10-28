# Shaqib q10.py

def second_largest(nums):
    """
    Return the second largest unique number in the list.
    If it doesn’t exist, return None.
    """
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]
