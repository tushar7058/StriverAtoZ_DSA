"""
        
               * * * * * * *     
                * * * * *         
                  * * * 
                    *

                    
space star spcae

0     7      0
1     5      1
2     3      2



"""
n = int(input("Enter a value: "))

def pattern7(n):
    for i in range(n):
        # spaces
        for j in range(i):
            print(" ", end=" ")
        # stars
        for k in range(2*n - (2*i + 1)):
            print("*", end=" ")
        
        print()

pattern7(n)
    
    