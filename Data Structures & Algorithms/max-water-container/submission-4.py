class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''
        Breakdown:
        - we are given an array of integers called heights.
        - each integer (heights[i]) in the array represents
          the height of the ith bar.
        - we must choose two bars to form a container.
        - return the maximum amount of water a container can store.

        Approach:
        - set two pointers l and r.
        - instantiate result = 0 to keep track of the max area.
        - calculate the area, where the width is the distance
          between the right and left pointer (r - l), and the height
          is the minimum between the two bars.
        - set result to the maximum between the current result and the new area.
        - move the smaller bar inward because since the width is always shrinking,
          finding a taller bar is the only way to compensate for the lost width.
        - if both heights are the same, move both pointers inward since
          neither bar is better to keep, and it lets us find new values
          that could possibly give a larger area.
        - once we finish the while loop, return the result.

        Notes:
        - area = width * height
        - we don't need + 1 on (r - l) because the water sits between
          the bars, so the distance between index 0 and 3 is 3, not 4.
        - moving just one pointer when heights are equal also works,
          moving both is just slightly more efficient.

        Time Complexity: O(n) because we go through each item once.
        Space Complexity: O(1) since no matter how many times we iterate,
        we only hold one value in result.
        '''

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:  # left bar is shorter, move it
                l += 1
            elif heights[l] > heights[r]:  # right bar is shorter, move it
                r -= 1
            else:  # both equal, move both
                l += 1
                r -= 1

        return res











