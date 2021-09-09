class Solution:
        
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        res = ""
        while i < len(s) and j < len(p):
            # if s[:i] != res:
            #     return False
            if p[j] == ".":
                res += s[i]
            elif p[j] == "*":
                while i < len(s) and res + s[i] == s[:i+1]:
                    res += s[i]
            else:
                res += p[i]
            i += 1
            j += 1
        return res,s
                        
        
if __name__ == "__main__":
    sol = Solution()
    # s = "aa"
    # p = "p"
    # p = ".*"
    # p = "a*."
    # p = "a*"
    s = "aab"
    p = "c*a*b"
    # s = "mississippi"
    # p = "mis*is*p*."
    # s = "mississippi"
    # p = "mis*is*ip*."
    # s = "aaa"
    # p = "ab*ac*a"
    # s = "aaa"
    # p = "ab*a"
    print(sol.isMatch(s, p))