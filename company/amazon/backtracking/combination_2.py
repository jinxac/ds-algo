class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(remaining, counter, arr, start):
            if remaining == 0:
                res.append(arr[:])
                return
                
            if remaining <= 0:
                return
            
            for i in range(start, len(counter)):
                element, freq = counter[i]
                if freq <= 0:
                    continue
                
                arr.append(element)
                counter[i]  = (element, freq - 1)
                helper(remaining - element, counter, arr, i)
                counter[i] = (element, freq)
                arr.pop()
        
        
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        
        
        helper(target, counter, [], 0)
        
        return res
