from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = {}
        prefix = ""
        for j in range(len(strs)):
            for k in range(len(strs[j])+1):
                if strs[j][:k] in prefixes:
                    prefixes[strs[j][:k]] += 1
                else:
                    prefixes[strs[j][:k]] = 1
                if prefixes[strs[j][:k]] % len(strs) == 0 and len(strs[j][:k]) > len(prefix):
                    prefix = strs[j][:k]
        return prefix

if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = ["a"]
    print(sol.longestCommonPrefix(strs))