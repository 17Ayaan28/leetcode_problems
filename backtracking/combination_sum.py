class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(i, L):

            if (sum(L) == target):
                result.append(L.copy())
                return
            elif (sum(L) > target or i >= len(candidates)):
                return

            L.append(candidates[i])
            backtrack(i, L)
            L.pop()
            backtrack(i+1, L)

        
        backtrack(0, [])

        return result
