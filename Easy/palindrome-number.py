from math import remainder
from multiprocessing.reduction import duplicate


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

# No String Conversion Solution
class Solution:
  def isPalindrome(self, x: int) -> bool:
    # all negatives are false
    if abs(x) != x:
      return False
    # store reverse
    reverseNum = 0
    num = x

    while num > 0:
      # use modulus to get ones place number
      remainder = num%10
      reverseNum *=10
      reverseNum+=remainder
      num //=10
    
    return reverseNum == x