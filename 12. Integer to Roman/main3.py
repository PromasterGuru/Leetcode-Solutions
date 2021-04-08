class Solution:
    def intToRoman(self, num: int) -> str:

        convertor = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
                     90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

        roman = ""
        for i in convertor:
            if i <= num:
                roman += convertor[i]*(num//i)
                num = num%i
        return roman

if __name__ == "__main__":
    sol = Solution()
    num = 1994
    print(sol.intToRoman(num))
