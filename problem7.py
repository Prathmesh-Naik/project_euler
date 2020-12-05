def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


i = 10
count = 4

while True:
    if is_prime(i):
        count += 1
        print(i, count)
    if count == 10001:
        print(i)
        break
    i += 1
