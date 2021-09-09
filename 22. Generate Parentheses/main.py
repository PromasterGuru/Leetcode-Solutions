from typing import List
class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     s = "("*n + ")"*n
    #     arr = []
    #     arr.append(s)
    #     i = 0
    #     # while i < n - 2:
    #     #     i += 1

    #     return arr
    def solution(A):
        S1 = [1,-1]*len(A)//2
        S2 = [-1,1]*len(A)//2
        sum1 = sum[(A[i] * S1[i] for i in range(len(A))]
        sum2 = sum[(A[i] * S2[j] for j in range(len(A))]
        return min(sum1,sum2)




if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))

# # ["()"]  -> 0
# # ["(())","()()"] -> 1
# # ["((()))","(()())","(())()","()(())","()()()"] -> 5

# "((()))",
# "(()())",
# "(())()",
# "()(())",
# "()()()"

# - Always ask questions throughout the process and speak throughout the whole process
# - Be comfortable when coding don't show you are guessing
# - Try to write more than one line of code
# - Describe how to build an application from scratch
# - Don't be nervous, be friendly
# - Use pseudocode when possible/necessary
# - Interviewer may go out of technical questions. Tie your skills to experience
# - Show your energy, give more than one answer
# 1. Design patterns 45 mins
# 2. Data Structures/Algorithms 45 mins

