class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        c = ""
        s = s.strip()
        if (len(s) <= 1 and not s.isdigit()): return 0
        while not s[i].isdigit():
            c += s[i]
            if (len(c) > 1 or c != "+" and c != "-"): return 0
            i += 1
        start = i
        while i < len(s) and s[i].isdigit():
            i += 1

        res = -int(s[start: i]) if c == "-" else int(s[start: i])
        if res < -2**31: return -2**31
        elif res > (2**31) - 1: return (2**31) - 1
        else: return res

            
                   
if __name__ == "__main__":
    sol = Solution()
    s = "The fire is  432"
    s = "4193 with words"
    s = "   -42"
    s = "   -+42"
    s = "3.14159"
    s = "-000012"
    s = "  -0012a42"
    # s = "00000-42a1234"
    # s = "     c99"
    # s = ""
    s = "+"
    s = "  "
    print(sol.myAtoi(s))