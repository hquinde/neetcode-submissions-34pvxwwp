'''
Breakdown:
- we are given two strings s and t.
- return true if the two strings are anagrams of each other.
- return false if they are not.
- an anagram is a string that contains the exact same characters
    as another string but the order can be different.

Approach:
- if the lengths of s and t are not equal, return False
    since this violates the definition of an anagram.
- use two hashmaps to track the characters and their counts
    for strings s and t.
- for each character, if it's already in the map add 1,
    otherwise set it to 1.
- return whether mp1 == mp2.

Notes:
- can simplify the if/else with .get():
    mp1[s[i]] = mp1.get(s[i], 0) + 1
    .get(key, default) returns the value if the key exists,
    otherwise returns the default. So we get the current count
    (or 0 if new) and add 1.

- mp1 == mp2 checks that both dictionaries have the same keys
    and the same values for each key. If any key is missing or
    any value is different, it returns False.

Time Complexity: O(n) since we iterate through each character.
Space Complexity: O(n) since we use hashmaps to track each character,
and it is n since the hashmap size is connected to the input size.
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

