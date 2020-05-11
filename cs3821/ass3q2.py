# maxI = 0 
# maxJ = 0
# def isPalindrome(string, i, j, table):
#     print(f'Running isPalindrome with i:{i}, j:{j}')
    
#     for i in range(i, j): 
#         if (i == j):
#             table[i][j] == True
#             return 
#         if (j < i): 
#             table[i][j] == False 
#             return 

#         if (table[i + 1][j - 1] == -1): table[i + 1][j - 1] == isPalindrome(string, i + 1, j - 1, table)

#         if (string[i] == string[j] and table[i+1][j-1]): 
#             if ((maxJ - maxI + 1) > (j - i + 1)): 
#                 maxI = i
#                 maxJ = j
#             table[i][j] = True 
#             return True
#         return isPalindrome(string, i, j - 1, table)

# def minPalindrome(string):
#     # Create a 2D table of size n * n where n = len(string)
#     table = [[-1 for x in range(len(string))] for y in range(len(string))]
#     nPalindromes = 0
#     isPalindrome(string, 0, len(string), table)
 
 
# minPalindrome("abcba") 
# for i in range(len(string)): 
#     print(f'i:{i}[')
#     for j in range(len(string)): 
#         print(f'{table[i][j]}, ') 
#     print("\n")
#-----------------------------------------------------------
def minPalindrome(string): 
    strLen = len(string) 
    minCost = [[-1 for i in range(strLen)] for i in range(strLen)] 
    isPal = [[False for i in range(strLen)] for i in range(strLen)] 

    # Base cases for when length is 1 
    for i in range(strLen): 
        minCost[i][i] = 0
        isPal[i][i] = True

    for substringLength in range(2, strLen + 1): 
        print(f'>>>> Looking through len: {substringLength}\n')
        for head in range(strLen - substringLength + 1): 
            tail = head + substringLength - 1 

            # Check if palindrone based on string size
            if substringLength == 2: isPal[head][tail] = (string[head] == string[tail]) 
            else: 
                isPal[head][tail] = ((string[head] == string[tail]) and (isPal[head+1][tail-1])) 
                print(f'@head: {head}, @tail: {tail}, isPal:{isPal[head][tail]}')

            # Cut the string further depending on if it's palindrone or not 
            if isPal[head][tail] == True: minCost[head][tail] = 0 
            else: 
                minCost[head][tail] = 10000000 
                for i in range(head, tail): 
                    minCost[head][tail] = min(minCost[head][tail], minCost[head][i] + minCost[i+1][tail] + 1) 
                    print(f'minCost[{head}][{tail}]: {minCost[head][tail]} is smaller compared to [{minCost[head][i]} + {minCost[i+1][tail]} + 1]')
    #####
    for i in range(len(string)): 
        for j in range(len(string)): 
            print(f'{minCost[i][j]}', end=", ") 
        print("\n")
    #####
    for i in range(len(string)): 
        for j in range(len(string)): 
            print(f'{isPal[i][j]}', end=", ") 
        print("\n")


    return minCost[0][strLen - 1] 
 
print(minPalindrome("ABBACAB")) 


#-----------------------------------------------------------
# Dynamic Programming Solution for  
# Palindrome Partitioning Problem  
  
# Returns the minimum number of  
# cuts needed to partition a string 
# such that every part is a palindrome 
def minPalPartion(str): 
      
    # Get the length of the string 
    n = len(str) 
      
    # Create two arrays to build the  
    # solution in bottom up manner  
    # C[i][j] = Minimum number of cuts  
    # needed for palindrome  
    # partitioning of substring str[i..j]  
    # P[i][j] = true if substring str[i..j]  
    # is palindrome, else false. Note that 
    # C[i][j] is 0 if P[i][j] is true  
    C = [[0 for i in range(n)]  
            for i in range(n)] 
    P = [[False for i in range(n)]  
                for i in range(n)] 
  
    # different looping variables 
    j = 0
    k = 0
    L = 0
      
    # Every substring of length  
    # 1 is a palindrome  
    for i in range(n): 
        P[i][i] = True;  
        C[i][i] = 0;  
          
    # L is substring length. Build the  
    # solution in bottom up manner by  
    # considering all substrings of  
    # length starting from 2 to n.  
    # The loop structure is same as  
    # Matrix Chain Multiplication problem   
    # (See https://www.geeksforgeeks.org / matrix-chain-multiplication-dp-8/ ) 
    for L in range(2, n + 1): 
          
        # For substring of length L, set  
        # different possible starting indexes  
        for i in range(n - L + 1): 
            j = i + L - 1 # Set ending index  
              
            # If L is 2, then we just need to 
            # compare two characters. Else  
            # need to check two corner characters 
            # and value of P[i + 1][j-1] 
            if L == 2:  
                P[i][j] = (str[i] == str[j]) 
            else: 
                P[i][j] = ((str[i] == str[j]) and 
                             P[i + 1][j - 1]) 
                               
            # IF str[i..j] is palindrome,  
            # then C[i][j] is 0 
            if P[i][j] == True: 
                C[i][j] = 0
            else: 
                  
                # Make a cut at every possible  
                # location starting from i to j, 
                # and get the minimum cost cut. 
                C[i][j] = 100000000
                for k in range(i, j): 
                    C[i][j] = min (C[i][j], C[i][k] + 
                                   C[k + 1][j] + 1) 
                                     
    # Return the min cut value for  
    # complete string. i.e., str[0..n-1]  
    return C[0][n - 1] + 1
  
# Driver code 
str = "ABBACAB"
print ('Min cuts needed for Palindrome Partitioning is',  
                                     minPalPartion(str)) 