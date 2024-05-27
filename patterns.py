for i in range(8):                  #rows
    for j in range(8):               #column
        print("*",end=" ")
    print(" ")    
    
    
    
    
    
print("TRIANGLE PATTERN")    

rows = 5  

for i in range(rows):           
    for j in range(i + 1):      
        print("*", end=" ")     
    print("") 
    
    
print("INVERTED TRIANGLE") 

rows = 6  

for i in range(rows):             
    print(" " * (rows - i - 1), end="") 
    print("*" * (i + 1))      