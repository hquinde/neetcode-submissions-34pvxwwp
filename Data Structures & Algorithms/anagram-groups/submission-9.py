class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Breakdown:
        - We are given a list of strings.
        - We group all anagrams into sublists.
        - the return output order does not matter.
        - an anagram is a string that contains the exact
        same character as another string but the order 
        of the characters can be different.
        - strings are only made up of lowercase letters

        Approach:
        - We instantiate a hashmap
        - The hashmaps key will have a code for that group of anagrams.
        - The hashmaps value will be the group of anagrams that satisfy the
          key value (the code).
        - we iterate through each string in the list.
        - we establish a code for each string using the alphabet
        - we iterate through each character of that string
        - we update the code of the string using our characters we are iterating through.
        - we make the key the code and the value the string.
        - we return the values of the hashmap as a list.



        Note:

        - list cannot me a key so we must use a tuple.
        - we do ord(char) - ord('a'), since 'a' is 0, so this would always give us
        postive numbers.
        - A defaultdict automatically creates a default value for any key 
        that doesn't exist yet, so instead of raising a KeyError, it initializes 
        that key with a value produced by the factory function you provide. For example,
        an empty list for this problem.



        '''

        mp = defaultdict(list)

        for string in strs: # iterate through each string
            code = [0] * 26 # establish a blank code for that string
            for char in string: # iterate through each character of that string
                code[ord(char) - ord('a')] += 1 # we now update the blank code for that string using each character
            mp[tuple(code)].append(string) # we use the updated code as the key and we append the string to that key.
        return list(mp.values()) # we return a list of the values, which are the strings we appended according the code.






