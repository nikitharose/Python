class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        s=""
        if(x>y):
            while(y>0):
                s=s+'AA'+'BB'
                y=y-1
                x=x-1
                if(z):
                    s=s+'AB'
                    z=z-1
            print(s)
        else:
            while(x>0):
                s=s+'BB'
                if(z):
                    s=s+'AB'
                    z=z-1
                s=s+'AA'
                x=x-1
                y=y-1
            print(x,y,z)
        
        res=len(s)+(z*2)
        z=0

        return (res+2 if x>0 or y>0 else res)

