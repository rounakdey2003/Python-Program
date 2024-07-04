def twoSum(nums, target):
  seen = {}
  for i, v in enumerate(nums):
    remaining = target - v
    if remaining in seen:
      return [seen[remaining], i]
    seen[v] = i
  return None

nums = [7,2,4,5]
target = 9
print(twoSum(nums,target))