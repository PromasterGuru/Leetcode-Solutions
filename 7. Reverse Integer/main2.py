class Solution:   
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0
        while num != 0:
            res = res*10 + (num%10)
            num = num//10
        res = res if x > 0 else -res
        return res if (res >= (-2**31) and res <= ((2**31) - 1)) else 0

if __name__ == "__main__":
    sol = Solution()
    n = 755
    n = -123
    print(sol.reverse(n))