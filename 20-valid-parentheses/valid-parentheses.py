class Solution:
    def isValid(self, s: str) -> bool:
        d={")":"(","]":"[","}":"{"}
        x=[]
        for i in s:
            if i in "({[":
                x.append(i)
            
            else:
                if not x or x[-1]!=d[i]:
                    return False

                x.pop()
        return not x
                    

      

        
            


            


               