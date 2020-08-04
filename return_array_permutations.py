# You are given an array of integers. Return all the permutations of this
# array.
def permute(nums):
    l = []

    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
       left = nums[i]
       right = nums[:i] + nums[i+1:]

       for p in permute(right):
           l.append([left] + p)
    return l

print(permute([1, 2, 3]))