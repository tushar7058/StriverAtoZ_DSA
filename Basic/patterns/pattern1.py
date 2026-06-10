"""

* * * *
* * * *
* * * *
* * * *

Rules to solve any patterns :

1. for the outer loop count the number of  lines
2. for the inner loop , focus on the columns & connect them somehow to the row .
3. whatever u r printing print them inside the inner for loop
4. observe symmetry in some patterns.


"""
# n = 4
# def printpatten(n):
#     for i in range(n):
#         for i in range(n):
#             print("*")
#         print()

# printpatten(n)



# def printpattern(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end=" ")
#         print()   # move to next line after each row

# printpattern(n)


n = 4
def printpattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()

printpattern(n)