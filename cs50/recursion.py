def loop(n):
    for i in range(n):
        for j in range(i+1):
            print('#', end='')
        print('') 
            
# loop(4)

def recursion(n):
    if n == 0:
        return
    recursion(n-1)
    for i in range(n):
        print('#', end='')
    print('')
        
recursion(3)