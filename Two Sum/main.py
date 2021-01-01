class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        for i in range(len(nums)):
            if((target - nums[i]) in numMap):
                return [numMap[target - nums[i]], i]
            numMap[nums[i]] = i


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    nums = [3, 2, 4]
    target = 6
    nums = [3,3]
    target = 6
    print(sol.twoSum(nums, target))
