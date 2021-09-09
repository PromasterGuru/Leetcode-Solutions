from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and nums[i] >= q[-1]:
                q.pop()
            q.append(nums[i])
        return q

        

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # nums = [1]
    # k = 1
    # nums = [1,-1]
    # k= 1
    # nums = [9,11]
    # k = 2
    nums = [4,-2]
    k= 2
    print(sol.maxSlidingWindow(nums, k))