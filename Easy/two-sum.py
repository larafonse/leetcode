# Link: https://leetcode.com/problems/two-sum/description/
# Brute Force 
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      # iterate through each number
      for i in range(0, len(nums)):
          # check if number + any number in list equals target
          for j in range(i+1, len(nums)):
              if (nums[i] + nums[j]) == target:
                  return [i, j]
# Optimized Solution
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # create a list of visited map
    visitedMap = {}
    # iterate through each number
    for i in range(len(nums)):
      # check if current number - target exists in visited map
      print(target - nums[i] in visitedMap)
      if target - nums[i] in visitedMap:
        # true: return current number and visited value index
        return [i,visitedMap[target-nums[i]]]
      # false: store visited number and index in map 
      visitedMap[nums[i]]= i