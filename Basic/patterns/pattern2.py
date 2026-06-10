"""
(1)
*
* *
* * *
* * * * 
* * * * *

(2)

* * * * 
* * * 
* * 
*

0 -> 1
1 -> 2
2 -> 3
3 -> 


"""

n  = int(input("Enter a value :"))
# def pattern2(n):
#     for i in range(n):
#         for j in range(i , n):
#             print("*" , end=" ")
#         print()
# pattern2(n)


def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*" , end=" ")
        print()
pattern2(n)