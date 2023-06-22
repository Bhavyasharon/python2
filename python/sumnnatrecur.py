def getsum(num):
    if num==0:
        return num
    return num+getsum(num-1)
num,sum=6,0
print(getsum(num))