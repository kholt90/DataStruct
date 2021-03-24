def k_th_smallest_distance(nums):
    nums_pairs = []
    for i in nums:
        for j in nums[i:]:
            nums_pairs.append((i, j))
    return nums_pairs

nums = [1, 3, 1]
print(k_th_smallest_distance(nums))

def k_th_smallest_distance(nums):
    nums.sort()
    for index in range(k):
        
