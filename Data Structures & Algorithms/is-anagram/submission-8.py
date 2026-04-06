'''
Breakdown:
- we are given two strings s and t.
- we return true if the two strings are anagrams of eachother.
- return false if they are not anagrams of eachother.
- an anagram is a string that contains the exact same character
  as another string but the order can be different.

Approach:
- if the lengths of s and t are not equal then we can return False
  since this violates the definition of an anagram
- we use two hashmaps to track the characters and its counts
  for strings s and t.
- we do if the character is in the specific map then we add by 1,
  else we set it to 1.

Time Complexity:
Space Complexity

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mp1 = {}
        mp2 = {}

        for i in range(len(s)):
            if s[i] in mp1:
                mp1[s[i]] += 1
            else:
                mp1[s[i]] = 1

            if t[i] in mp2:
                mp2[t[i]] += 1
            else:
                mp2[t[i]] = 1
        
        return mp1 == mp2
            
            










        