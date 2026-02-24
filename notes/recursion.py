#BB 1st Recursion Notes
for num in range(1,11):
    if num % 2 == 0:
        print(num)

even = []

num = 10
sum = 1

for x in range(1,num +1):
    sum *= x
print(f"Loop: {sum}")

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(f"Recursion: {factorial(num)}")

fib = [1,1]

for i in range(1,11): 
    fib.append(fib[i-1] + fib[i])

print(f"Loop: {fib}")

numbers = []
def fibonacci(n):
    #numbers.append(n)
    if n == 2: 
        return 1
    elif n == 1: 
        return 0
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

print(f"Recursion: {fibonacci(11)}")