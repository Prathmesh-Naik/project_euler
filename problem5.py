def check_div(n):
    for i in range(11, 21):
        if n%i != 0:
            return False
    return True

i = 2520

while True:
    if check_div(i):
        print(i)
        break
    i += 2520
