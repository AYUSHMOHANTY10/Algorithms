def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
m=int(input("Enter The Number: "))
print("The factorial of number",m,"=",fact(m))
