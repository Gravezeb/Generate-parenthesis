print("\n")
print("\n")
print("\t \t \t GenerateParenthesis")\

class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack()
        return result
    
solution = Solution()

n = 2
output = solution.generateParenthesis(n)
print(output)


print("\n")
