class Solution:
    def isBalanced(self, num: str) -> bool:

        even=[]
        odd=[]
        for i in range(len(num)):
            if i%2==0:
                even.append(int(num[i]))
            else:
                odd.append(int(num[i]))
        if sum(even)==sum(odd):
            return True
        return False


        