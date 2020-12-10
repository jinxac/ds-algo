class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        self.city = ""
        temp = {}
        for row in paths:
            temp[row[0]] = row[1]
                
        def getCity(key):
            if not key in temp:
                self.city = key
                return 
            getCity(temp[key])
        
        
        getCity(next(iter(temp)))
        return self.city
