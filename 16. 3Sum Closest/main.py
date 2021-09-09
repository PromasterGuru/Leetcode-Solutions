from typing import List

class Solution:
    def threeSumClosest(self, n: List[int], target: int) -> int:
        nums = sorted(n)
        closest = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                print( nums[i], nums[j], nums[k])
                if s <= target:
                    j+=1
                else:
                    k-=1
                closest = min(abs(closest - target), abs(s -target))
        return closest

if __name__ == "__main__":
    nums = [-1,2,1,-4] 
    target = 1
    sol = Solution()
    print(sol.threeSumClosest(nums, target))