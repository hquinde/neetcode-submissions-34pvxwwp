class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Breakdown:
        - We are given a list of integers
        - We are given an integer k
        - We must return the k most frequent integers in the list. For example,
        the 5 most frequent integers in the list,
        - the answer is always unique
        - the output can be in any order

        Approach:

        We must return the actual integer value so I am thinking of 
        some how keeping track of the value and the values frequency 
        which could be like a count. Then we would sort the list by 
        it's frequency and loop through that list k times from the right
        to left, since those are the only values we want.


        Notes:

        

        Time complexity:
        Space complexity:
        '''

        mp = {} # we create a map that tracks {key: value} or {number: frequency}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1 # I want to understand this better, I need better clarification on the syntax.

        freq = [[freq, n] for n, freq in mp.items()]
        freq.sort() # sorts by the first value of the list, which would be freq right?

        res = []
        r = len(freq) - 1
        while k:
            res.append(freq[r][1]) # this gives us the second item which would be the value. Before we sorted by the freq which is the first value. This makes sense.
            k -= 1
            r -= 1
        
        return res











