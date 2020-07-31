# You are given an array of integers.
# Return the length of the longest consecutive elements sequence in the array.
# For example, the input array [100, 4, 200, 1, 3, 2] has the longest
# consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.
def longest_consecutive(nums):
    count, longest = 0, 0
    nums.sort()
    print(nums)
    for i in range(len(nums)-1):
        if (nums[i] + 1) == nums[i+1]:
            count+=1
            if count > longest:
                longest = count
        else:
            count = 0

    return longest + 1

print(longest_consecutive([100, 4, 200, 1, 3, 2, 5, 101, 102, 104, 103, 105]))