import time 

def caching_fibonacci():
    
    cache = {}

    def fibonacci(n):
        if n <= 0:
            cache[n] = n
            return 0
        if n == 1:
            cache[n] = n
            return 1 
        if n in cache:
            return cache[n]
        cache[n]=(fibonacci(n-2)+fibonacci(n-1))
        
        return cache[n]
            
    return fibonacci
    


fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(16))  # Виведе 610