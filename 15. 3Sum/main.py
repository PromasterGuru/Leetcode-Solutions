class Solution:
    def threeSum(self, nums):
        arr = []
        map = {nums[i]: i for i in range(len(nums))}
        if (len(list(map.keys())) == 1 and nums[0] == 0 and len(nums) > 3):
            return [[0]*3]
        for m in range(len(nums)-1):
            for n in range(m+1, len(nums)):
                target = (0 - (nums[m] + nums[n]))
                if((target in map) and (map[target] != n and map[target] != m)):
                    sorteditems = sorted([nums[n], nums[m], target]) 
                    if sorteditems not in arr:
                        arr.append(sorteditems)
                    break
        return  arr

if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))
