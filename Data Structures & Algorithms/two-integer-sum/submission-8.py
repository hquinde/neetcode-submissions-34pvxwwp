'''
Breakdown:
- we are given a list of integers.
- we are given a target.
- we return the indices i and j such that the sum of the
    items are equal to the target.
- i != j.
- there is at least one pair of indices.
- we return the smaller index first.

Approach:
- instantiate a hashmap.
- we need to keep track of the indices and the values so we use enumerate.
- calculate the remaining number by subtracting the current value from the target.
- if the remaining value is in the map then we return a list of the index of
    that key and the current index, which automatically is greater than
    the index before.
- else we store the current value as the key and the current index as the value.

Notes:
- we store the value as the key, not the remaining, because when a future
    number calculates its remaining, it needs to find an actual value that
    was seen before. If we stored the remaining, we'd be looking up the wrong thing.

Time Complexity: O(n) since we iterate through every item in the list.
Space Complexity: O(n) since the input n is connected to every iteration
we do with the for loop.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mp = {}
        for index, value in enumerate(nums):
            remaining = target - value
            if remaining in mp:
                return [mp[remaining], index]
            else:
                mp[value] = index
        