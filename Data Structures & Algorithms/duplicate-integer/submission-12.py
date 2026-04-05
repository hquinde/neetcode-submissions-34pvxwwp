'''
Breakdown:

- we are given a list of numbers.
- return true if we find a duplicate.
- return false if we don't find a duplicate.

Approach:

- instantiate a set named seen.
- iterate through the list.
- if the current item is already in seen, return true.
- otherwise add it to seen and continue.
- once we finish the loop, return false since
  we were unable to find a duplicate.

Time Complexity: O(n) because we iterate through each item in nums.
Space Complexity: O(n) because we add each item into the set seen, so it's n and not some other variable like m since it is connected to the iterations.
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n) 
        return False
