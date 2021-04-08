class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0 or len(s) == 0:
            return False
        if len(p) <= 1 and p not in ["*", "."] and s!= p:
            return False
        if p[-2:] == ".*":
            return True if len(s) > 0 else False
        if p[-2:] == "*.":
            i = -1
            while (abs(i) <= len(p) and p[i] in ["*", "."]):
                i -= 1
            return  True if p[i] == "*" else s[-1] == p[i]
        if p[-1] == ".":
            i = -1
            while p[i] == ".":
                i -= 1
            return p[i] == s[-1]
        if p[-1] == "*":
            return True
        
        else:
            return p[-1] == s[-1]
if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    p = "p"
    p = ".*"
    # p = "a*."
    p = "a*"
    s = "aab"
    p = "c*a*b"
    s = "mississippi"
    p = "mis*is*p*."
    s = "mississippi"
    p = "mis*is*ip*."
    print(sol.isMatch(s, p))