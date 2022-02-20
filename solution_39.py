class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        candidates.sort()
        res = []
        def dfs(List, target, sum, vlist, answer):
            if(sum > target):
                return
            elif(sum == target):
                list = vlist.copy()
                list.sort()
                if(list not in answer):
                    
                    answer.append(list)
            else:
                for r in range(len(List)):
                    vlist.append(List[r])
                    dfs(List, target, sum + List[r], vlist, answer)
                    vlist.pop()
        dfs(candidates, target, 0, [], res)
        return res


