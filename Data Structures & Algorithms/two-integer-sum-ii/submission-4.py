class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        - sorted in non-decreasing order meaning it goes from least to greatest,
          for example 2, 2, 3 is valid since 2 to 2 is non-decreasing
        - 1-indexed meaning we return indices starting at 1, not 0
        - must return [index1, index2] where index1 < index2
        - index1 != index2 so we can't use the same element twice
        - exactly one valid solution, must use O(1) additional space
        - O(1) space means the extra memory we use doesn't grow with input size,
          so two pointers is fine but a hashmap would not be

        approach:
        1. set two pointers l and r
        2. iterate using l < r (not <= since l == r would mean using the same element)
        3. calculate the current total
        4. if total > target, move right pointer inward (sum is too big)
        5. if total < target, move left pointer inward (sum is too small)
        6. if total == target, return [l + 1, r + 1] (convert to 1-indexed)

        why this works:
        - since the array is sorted, moving r left decreases the sum
          and moving l right increases the sum
        - this lets us narrow in on the target from both ends
        '''

        l, r = 0, len(numbers) - 1

        while l < r:
            t = numbers[l] + numbers[r]

            if t > target:  # sum too big, shrink from right
                r -= 1
                continue # go back to top, recalculate t with new l

            if t < target:  # sum too small, grow from left
                l += 1
                continue # go back to top, recalculate t with new l

            return [l + 1, r + 1]  # found it, return 1-indexed