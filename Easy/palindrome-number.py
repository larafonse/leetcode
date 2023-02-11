class Solution:
  def isPalindrome(self, x: int) -> bool:
    # convert num to string
    numString = str(x)
    # use a left and right starting index
    left, right = 0, len(numString)-1
    while left < right:
      # return false if index values do not match
      if numString[left] != numString[right]:
          return False
      left+=1
      right-=1
    return True