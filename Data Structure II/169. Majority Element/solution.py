from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        candidate = -1
        for c in nums:
            if votes == 0:
                candidate = c
            if candidate == c:
                votes += 1
            else:
                votes -= 1
        return candidate

if __name__ == "__main__":
    sol = Solution()
    nums0 = [3,2,3]
    nums1 = [2,2,1,1,1,2,2]
    nums2 = [3,2,3]
    print(sol.majorityElement(nums0))
    print(sol.majorityElement(nums1))
    print(sol.majorityElement(nums2))