"""

* * * * 
* * *
* * 
*


"""
n = int(input("Enter a value :"))
def pattern4(n):
    for i in range(n):
        for j in range(i , n):
            print("*", end=" ")
        print()

pattern4(n)