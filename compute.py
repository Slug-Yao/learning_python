import math
a=input()
a=int(a)
sum=0
def main(num):
    return math.factorial(num)
for i in range(1,a+1):
    sum+=main(i)
print(sum)