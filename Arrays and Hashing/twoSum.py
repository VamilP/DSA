# Yes, that's a good plan! So, to summarize, you're going to loop through the array, for each number you'll calculate the difference between the target and the current number, then you'll check if this difference is already in your stored values. If it is, you've found your pair and you can return the indices. If it's not, you'll store the current number and its index and move on to the next number. Does that sound like a plan?

# No problem, let's break it down. You're correctly calculating the difference between the target and the current number. Now, you need to check if this difference exists in your list. But, you also need to make sure that this difference is not the current number itself. So, add a condition to check if the index of the difference is not the same as the current index. Can you try adding this condition to your if statement?


# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i,j


def twoSum(nums, target):
    hash_map = {}
    for idx, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target-num],idx] 
        hash_map[num] = idx 
    return []

# nums = [2,7,11,15]
nums = [2,5,5,11]
# nums = [3,2,4]
# nums = [3,3]
target = 10
print(twoSum(nums, target))


