from typing import List
class Solution:
    # Xor/Bit Manipulation
    def singleNumber(self, nums: List[int]) -> int: 
        xor = 0
        for num in nums:
            xor ^= num
        return xor

if __name__ == "__main__":
    sol = Solution()
    nums0 = [2,2,1]
    nums1 = [2,2,1,1,3,4,4]
    nums2 = [3,2,3]
    print(sol.singleNumber(nums0))
    print(sol.singleNumber(nums1))
    print(sol.singleNumber(nums2))