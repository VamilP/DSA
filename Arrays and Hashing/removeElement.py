# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

def removeElement(nums, val):
    l = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[l] = nums[i]
            l += 1
            print(f"nums: {nums[l]}", end=" ")
    return l

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))