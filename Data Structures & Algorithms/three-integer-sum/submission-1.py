class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        '''
        - we are given an list made up of integers.
        - we need to return a list of all triplets, where
          the sum = 0.
        - the indice of an indivdual item in the triplet must be unique.
        - no duplicate triplets are allowed.
        - order doesn't matter.
        - according to the constraints the length of nums will be atleast 3

        Approach:
        - sort the list by their value.
        - establish a result list, that would allow us to add triplets.
        - instantiate a range loop, which counts as pointer i.
        - we do our first check for duplicates involving i.
        - instantiate another 2 pointers (j, k) inside range.
        - we use a while loop to track j and k.
        - track the total.
        - if the total is less than 0 then we move j inward
        - if the total is more than 0 then we move k inward
        - else we add the triplet, since both checks failed meaning it is now equal to 0
        - we move i and j inward
        - we do our second check involving j
        - we do our third check involving k
        
        checks break down that confused me:

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        - once i is greater than 0, meaning we are at the second item then
          we can now check wether the second item is equal to the previous 
          item and if they are then we can continue to the next item. This would
          allow us to skip duplicates before we even instantiate point j and k.

        while j < k and nums[j] == nums[j - 1]:
            j += 1

        - once we found our triplet we have already moved j inward by 1 shown 
          in the code when we found a triplet which was before the check, so 
          now we can check for duplicates, but before we do that we must first 
          make sure j stays below k and then we can check wether the current 
          value of j is equal to the past value of j, and if so we move j inward
          again.

        while j < k and nums[k] == nums[k + 1]:
            k -= 1

        - once we found our triplet we have already moved k inward by 1 shown
          the code when we found a triplet which was before the check, so now we
          can check for duplicates, but before we do that we must make sure j stays
          below k, then now we can check wether the current value of k is equal to the
          past value of k by doing + 1 since the pointer comes inward from right to left
          if they are equal then there is a duplicate so we move the k pointer again.

        Notes:

        - The checks are very important in this code, and allows for a better flow
          but thinking about where to put these checks must be strategic.

        - O(n log n ) is the time complexity of .sort()

        - We use m in this case instead of n because m and n are not connected but 
          in some cases we use n in both time and space complexity because they are 
          relative meaning they are connected.

        Time Complexity: O(n^2) because of the for loop and the while loop inside, which dominates O(n log n)

        Space Complexity: O(m) represents for the size of the result.
        '''

        nums.sort() # what is the time complexity on this? I feel like this makes it slower or possibly I can make this more efficient

        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0 :
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # check 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # check 2
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res





