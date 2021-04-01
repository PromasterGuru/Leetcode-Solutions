class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        visited = {}
        for i in range(len(nums)):
            for m in visited:
                if (abs(m - nums[i])<= t and abs(i - visited[m]) <= k):
                    return True
            visited[nums[i]] = i
        return False

if __name__ == "__main__":
    sol = Solution()
    data = [
        {'nums': [1,2,3,1], 'k':3, 't':0},
        {'nums': [1,2,3,1], 'k':3, 't':0},
        {'nums': [1,5,9,1,5,9], 'k':2, 't':3}
        ]
    for m in data:
        print(sol.containsNearbyAlmostDuplicate(m['nums'], m['k'], m['t']))
        