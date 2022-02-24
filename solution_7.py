class Solution:
    def reverse(self, x: int) -> int:
        def ReverseInteger(x):
            
            minus = False
            if(x < 0):
                minus = True
                x = abs(x)
            s = str(x)
            s = s[::-1]
            x = int(s)
            if(minus):
                x = -1 * x
            if((x > 2**31 -1) or (x < -2**31)):
                return 0
            return x
        
        return ReverseInteger(x)