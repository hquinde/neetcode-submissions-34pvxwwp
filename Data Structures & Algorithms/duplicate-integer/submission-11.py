class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        '''
        Breakdown:

        - we are given a list of numbers.
        - we return true if we find a duplicate.
        - we return false if we don't find a duplicate.

        Approach:

        - we instantiate a set named seen.
        - we iterate through the list.
        - we add the current item into the set.
        - if an item is in the set seen return true.
        - if an item is not in the set seen we continue.
        - once we finish with the loop we return false
          since we were unable to find a duplicate.

        Time Complexity: O(n) because we iterate through each item in nums
        Space Complexity: O(n) because we add each item into the set seen in each iterate
                          so thats why it is n and not some other variable like m since it
                          is connected to the iterations.

        '''

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n) 
        return False
        