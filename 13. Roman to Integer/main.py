class Solution:
    def romanToInt(self, s: str) -> int:
        convertor = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
        n = 0
        l = len(s) - 1
        c = convertor[s[l]]
        while(l>=0):
            if convertor[s[l]] < c:
                n -= convertor[s[l]]
            else:
                n += convertor[s[l]]
            c = convertor[s[l]]
            l -= 1
        return n

if __name__ == "__main__":
    sol = Solution()
    s = "III"
    # s = "IV"
    # s = "IX"
    # s = "LVIII"
    # s = "MCMXCIV"
    print(sol.romanToInt(s))
