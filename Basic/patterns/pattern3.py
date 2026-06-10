"""

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5


"""

n = int(input("Enter a num :"))
def patttern3(n):
    for i in range(n):
        for j in range(i+1):
            print(j,end=" ")
        print()

patttern3(5)
