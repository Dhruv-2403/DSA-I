class Solution(object):
    def average(self, salary):
        
        x=sorted(salary)
        y=x[1:-1]

        return float(sum(y))/len(y)

        