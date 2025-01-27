def pascal_triangle(n):
    spaces = n - 1
    for i in range(1, n+1):
        for s in range(1, spaces+1):
            print(' ', end='')
        c = 1 
        for j in range(1, i+1):
            print(c, end='  ')
            c = c * (i - j) // j 
        
        spaces -= 1  
        print()

# Calling the function for n=6
pascal_triangle(5)
