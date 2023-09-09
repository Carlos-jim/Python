def fibonacci(n):
    
    aux = 1
    aux2 = 0
    
    for i in range(n):

        
        total = aux + aux2
        
        aux2 = aux
        aux = total
        
        print(total)
        
        
print(fibonacci(10))