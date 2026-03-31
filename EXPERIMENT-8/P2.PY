M = int(input("Enter starting number (M): "))
N = int(input("Enter ending number (N): "))

primes = []
for num in range(M, N+1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
print("Prime numbers between",M,"and",N,"are:")
print(primes)