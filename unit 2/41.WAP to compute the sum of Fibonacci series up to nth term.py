n=int(input("Enter a number: "))
sum=0
a=0
b=1
for i in range(n):
    c=a+b
    sum+=c
    a=b
    b=c
print(sum)
