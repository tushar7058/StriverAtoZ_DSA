"""

            *
          * * * 
        * * * * * 
       * * * * * * * 



"""


n = int(input("Enter a value: "))

def pattern6(n):
    for i in range(n):
        # print spaces
        for j in range(n - i - 1):
            print(" ", end=" ")
        
        # print stars
        for k in range(2 * i + 1):
            print("*", end=" ")
        
        print()

pattern6(n)