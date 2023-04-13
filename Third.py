a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
d=int(input("Enter the 4th number: "))
e=a+b
f=a-b
g=c*d
h=float(c/d)
i=a+b+c+d
j=(a+b)*(a-b)
print(a,"+",b,"=",e)
print(a,"-",b,"=",f)
print(c,"*",d,"=",g)
print(c,"/",d,"=",h)
print(a,"+",b,"+",c,"+",d,"=",i)
print("(",a,"+",b,")","*","(",a,"-",b,")","=",j)
if a>b:
    print(a,"is greater.")
elif b>c:
    print(b,"is greater.")
elif c>d:
    print(c,"is greater.")
else:
    print(d,"is greater.")