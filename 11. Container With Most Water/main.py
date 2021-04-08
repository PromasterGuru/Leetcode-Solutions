from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l = 0
        r = len(height) - 1
        while l <= r:
            area = min(height[l], height[r]) * (r-l)
            if maximum < area:
                maximum = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maximum

if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    # height = [4,5]
    # height = [1,1]
    # height = [4,3,2,1,4]
    height = [1,2,1,4,2,1]
    print(sol.maxArea(height))