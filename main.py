# class Solution:
#     def solution(self, s, b):
#         pots = []
#         frag = ""
#         minpotholes = 0
#         for i,j in enumerate(s):
#             if j.lower() == "x":
#                 frag += j
#             if len(frag) >= b - 1:
#                 return b - 1
#             if (i == len(s) - 1 or j == ".") and len(frag) > 0:
#                 pots.append(len(frag))
#                 frag = ""

#         for n,m in enumerate(sorted(pots, reverse=True)):
#             if minpotholes + m + n + 1 <= b:
#                 minpotholes += m
#             else:
#                 minpotholes = b - (n + 1)
#                 break
#         return minpotholes

# if __name__ == "__main__":
#     sol = Solution()
#     s = "...XXX..X....XXX."
#     s = "..XXXXX"
#     s = ".X"
#     s = "X.X.XXX....x"
#     s = ".."
#     print(sol.solution(s,14))


# class Node:
#     def __init__(self, data = None, next = None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert(self, data):
#         newNode = 

# def solution(markdown):
#     markdown = markdown.lstrip()
#     splitted = markdown.split()
#     n = len(splitted[0])
#     if len(splitted) > 1 and splitted[0] == "#" * n and n <= 6:
#         return "<h{}>{}</h{}>".format(n, markdown[n:].strip(), n)
#     else:
#         return markdown

# print(solution("    ##### Header Header Header"))
# def getDivision(n):
#     s = str(n)
#     if n < 100 and int(s[0]) * int(s[1])> 70:
#         return n >= 89
#     return int(s[:-1]) >= 89 or int(s[1:]) >= 89

# def solution(l, arr):
#     ar = []
#     for i in range(len(arr)):
#         if(getDivision(arr[i])):
#             ar.append("Yes")
#         else:
#             ar.append("No")
#     return ar    

# if __name__ == '__main__':
#     print(solution(2, [256, 991, 89, 777]))

def fibonaci(n):
    # arr = [0,1]
    # i = 2
    # if n < 0:
    #     return -1
    
    # while i <= n:
    #     arr.append(arr[-1] + arr[-2])
    #     i += 1
    # return arr[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    print(n, end=" ")
    return (fibonaci(n-1)) + fibonaci(n-2)

if __name__ == "__main__":
    print(fibonaci(20))
