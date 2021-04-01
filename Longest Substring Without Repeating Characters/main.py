class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxs = 0
        temp = ""
        l = 0
        for i in range(len(s)):
            if s[i] in temp:
                while temp[l] != s[i]:
                    l+=1
                temp = temp[l+1:]
        temp += s[i]            
            l = 0
            if len(temp) > maxs:
                maxs = len(temp)
        return maxs

if __name__ == "__main__":
    sol = Solution()
    tests = ["abcabcbb","bbbbb","pwwkew",""," ","dvdf","tmmzuxt"]
    for s in tests:
        print(sol.lengthOfLongestSubstring(s))