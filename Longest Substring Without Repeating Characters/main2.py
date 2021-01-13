class Solution(object):
    def lengthOfLongestSubstring(self, s):
        smap = {}
        j = 0
        size = 0
        for i in range(len(s)):
            if s[i] in smap:
                j = max(smap[s[i]], j)
            smap[s[i]] = i+1
            size = max(size, i-j+1)
        return size


if __name__ == "__main__":
    sol = Solution()
    tests = ["abcabcbb","bbbbb","pwwkew",""," ","dvdf","tmmzuxt"]
    for s in tests:
        print(sol.lengthOfLongestSubstring(s))
