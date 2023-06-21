# Implementation Of Factorial Algorithm

# Main Function To Find The Factorial
def fact(n):
    # Base Case : If Number Is 1 Return 1
    if n==1:
        return 1
    # Recursive Call : The Product Of The Number Multiplied By The Factorial Of That Number Minus 1
    else:
        return (n*fact(n-1))
# Driver Code
n=int(input("Enter The Number: "))
print("Factorial Of Number",n,"is",fact(n))
