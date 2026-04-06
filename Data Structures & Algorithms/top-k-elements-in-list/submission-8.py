'''
Breakdown:
- We are given a list of integers
- We are given an integer k
- We must return the k most frequent integers in the list
    (for example, the 5 most frequent integers)
- The answer is always unique
- The output can be in any order

Approach:
- Instantiate a hashmap that allows us to keep track of the
    number and its frequency.
- Create a frequency list based off the hashmap.
- Sort the frequency list using .sort().
- Instantiate an empty result list.
- Iterate through the sorted frequency list in reverse using a right pointer.
- Use k to control the while loop — once it reaches 0, the loop breaks.
- Only append the second value of each item (the number, not the frequency).
- Update the right pointer by subtracting 1.
- Return the result list containing only the k most frequent values.

Notes:
- When I created the frequency list I put the value n first, but then
    realized that the frequency should be first since .sort() sorts by the
    first element. This lets us iterate in reverse to grab the top k most
    frequent values, since .sort() sorts from least to greatest.

- When iterating with a while loop using k, I was confused about whether
    it would iterate again once k reaches 0. But if k = 2 for example,
    we iterate at k = 2 and k = 1, but not 0 since 0 breaks the while loop.
    This satisfies returning the k most frequent values.

- When adding an item to our result list, we only add the second value ([1])
    since we don't want the frequency, just the number. The frequency was only
    used to sort the list so we could iterate it accordingly.

- .get(n, 0) is a safe lookup — it grabs the current count for n
    (or 0 if we haven't seen it yet), then we add 1 and store it back.
    .get() itself isn't a counting method, it's just a safe way to retrieve
    a value with a fallback default. The counting comes from combining it with + 1.

- List comprehensions are shorthand for building a new list. The pattern is
    [expression for variable in iterable] — the part after for is the loop,
    and the part before for is what gets added each iteration. If the loop is
    updating a variable (like count += 1) instead of building a list, use a
    regular for loop.

Time complexity: O(n log n) since we iterate through nums once which is O(n),
but the .sort() on the frequency list is O(n log n) which dominates everything
else. The while k loop is at most O(k), and since k is always less than or
equal to n, it doesn't affect the overall complexity.

Space complexity: O(n) since the hashmap, frequency list, and result list all
scale with n. There's no separate m because the frequency list comes directly
from nums — if every number is unique, the most entries we'd have is n.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {} # tracks {number: frequency}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        freq = [[freq, n] for n, freq in mp.items()]
        freq.sort() # sorts by the first value of each list, which is the frequency

        res = []
        r = len(freq) - 1
        while k:
            res.append(freq[r][1]) # appends the number, not the frequency
            k -= 1
            r -= 1
        
        return res