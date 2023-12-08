n= int(input("n: "))
a=n
sum=0
if(n>0):
    b=str(n)
    for i in range(len(b)):
        c=a%10
        sum=sum + c**len(b)
        a=a//10
print("sum of powers: ",sum)
if(sum==n):
    print("armstrong number")
else:
    print("not armstrong number")