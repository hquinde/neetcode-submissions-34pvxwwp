'''
Breakdown:
- we are given a list of strings.
- we group all anagrams into sublists.
- the return output order does not matter.
- an anagram is a string that contains the exact same characters
    as another string but the order of the characters can be different.
- strings are only made up of lowercase letters.

Approach:
- instantiate a hashmap.
- the hashmaps key will have a code for that group of anagrams.
- the hashmaps value will be the group of anagrams that satisfy the
    key value (the code).
- we iterate through each string in the list.
- we establish a code for each string using the alphabet.
- we iterate through each character of that string.
- we update the code of the string using our characters we are iterating through.
- we make the key the code and the value the string.
- we return the values of the hashmap as a list.

Notes:
- lists cannot be a key since they are unhashable. Unhashable means
    Python can't convert it into a fixed number (a hash) to use as a
    dictionary key. Lists are unhashable because they are mutable,
    meaning they can be changed after creation (e.g. append, modify).
    Tuples are immutable, meaning they cannot be changed after creation,
    so Python can hash them and use them as keys.
- we do ord(char) - ord('a'), since 'a' is 0, so this would always
    give us positive numbers.
- a defaultdict automatically creates a default value for any key
    that doesn't exist yet, so instead of raising a KeyError, it initializes
    that key with a value produced by the factory function you provide.
    For example, an empty list for this problem.

Time Complexity: O(n * m) where n is the number of strings and m is the
average length of each string. It's not O(n^2) because the two loops iterate
over different things — strings and characters, not the same collection.
Space Complexity: O(n * m) since we store all the strings in the hashmap.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for string in strs:  # iterate through each string
            code = [0] * 26  # establish a blank code for that string
            for char in string:  # iterate through each character of that string
                code[ord(char) - ord('a')] += 1  # update the code using each character
            mp[tuple(code)].append(string)  # tuple because lists are unhashable
        return list(mp.values())  # return the grouped anagrams as a list