from itertools import permutations

a = '123456789'
flag = True
i = len(a)


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


while flag:
    p = permutations(a[:i])
    p = reversed(sorted(list(p)))

    for j in p:
        number = int(''.join(j))
        if is_prime(number):
            print(number)
            flag = False
            break

    i -= 1
