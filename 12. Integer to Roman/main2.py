class Solution:
    def intToRoman(self, num: int) -> str:

        convertor = [
            [1000,"M"],
            [900, "CM"],
            [500,"D"],
            [400,"CD"],
            [100, "C"],
            [90,"XC"],
            [50,"L"],
            [40,"XL"],
            [10,"X"],
            [9,"IX"],
            [5,"V"],
            [4,"IV"],
            [1,"I"]
        ]

        index = 0
        roman = ""
        while(num):
            if convertor[index][0] <= num:
                roman += convertor[index][1]
                num -= convertor[index][0]
            else:
                index += 1
        return roman

if __name__ == "__main__":
   sol = Solution()
   num = 9
   print(sol.intToRoman(num))