l = []

def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i*j
        if is_palindrome(str(product)):
            l.append(product)

print(max(l))