from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []
        # nums.sort()
        # visited = {}
        # for i in range(len(nums) - 3):
        #     for j in range(i+1, len(nums)-2):
        #         l = j+1
        #         r = len(nums) - 1
        #         while l < r:
        #             setNum = tuple(sorted([nums[i], nums[j], nums[l], nums[r]]))
        #             if (nums[i] + nums[j] + nums[l] + nums[r] == target) and setNum not in visited:
        #                 res.append([nums[i], nums[j], nums[l], nums[r]])
        #                 print([nums[i], nums[j], nums[l], nums[r]])
        #                 l += 1
        #                 r -= 1
        #             elif nums[i] + nums[j] + nums[l] + nums[r] > target:
        #                 r -= 1
        #             else:
        #                 l += 1
        #             visited[setNum] = 1
        # return res
        # board = [["","",""]]*3
        board = []
        for i in range(3):
            arr = []
            for j in range(3):
                arr.append("")
            board.append(arr)
        
        board[0][0] = "X"
        return board
    
    
if __name__=='__main__':
    sol = Solution()
    nums = [1 ,0,-1,0,-2,2]
    target = 0
    nums = [2,2,2,2,2]
    target = 8
    nums = [-4,-3,-2,-1,0,0,1,2,3,4]
    target = 0
    print(sol.fourSum(nums, target))
    
    i = -4
    j = -1
    l = 0,0,1,
    r = 4
    '''
    [[-4,-3,3,4],
    [-4,-2,2,4],
    [-4,-1,1,4],
    [-4,-1,2,3],
    [-4,0,0,4],
    [-4,0,1,3],
    [-3,-2,1,4],
    [-3,-2,2,3],
    [-3,-1,0,4],
    [-3,-1,1,3],
    [-3,0,0,3],
    [-3,0,1,2],
    [-2,-1,0,3],
    [-2,-1,1,2],
    [-2,0,0,2],
    [-1,0,0,1]]
    '''
    '''
    Mising
    -4,-1,2,3]
    [-3,-2,2,3]
    '''