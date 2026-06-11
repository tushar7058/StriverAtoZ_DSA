"""

    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    *    


"""










class Solution:
    # Function to print the erect (upright) pyramid
    def erect_pyramid(self, N):
        for i in range(N):
            # Print spaces before stars
            print(" " * (N - i - 1), end="")
            # Print stars
            print("*" * (2 * i + 1), end="")
            # Print spaces after stars
            print(" " * (N - i - 1))
    
    # Function to print the inverted pyramid
    def inverted_pyramid(self, N):
        for i in range(N):
            # Print spaces before stars
            print(" " * i, end="")
            # Print stars
            print("*" * (2 * N - (2 * i + 1)), end="")
            # Print spaces after stars
            print(" " * i)

if __name__ == "__main__":
    N = 5
    obj = Solution()
    obj.erect_pyramid(N)
    obj.inverted_pyramid(N)
