n = 600851475143
max = 0

def is_prime(n):
    for i in range(2, int(n**(0.5))):
        if n%i == 0:
            return False
    return True

for i in range(1, int(n**(0.5))):
    if n%i == 0 and is_prime(i):
        max = i

print(max)