# Longest Collatz Sequence

max_count = [0,0]
i = 13

while i <= 1000000:
    count = 0
    temp = i
    while temp != 1:
        if temp%2 ==0:
            temp /= 2
        else:
            temp = (3*temp) + 1
        count += 1

    if count > max_count[0]:
        max_count = [count, i]

    i += 1

print(max_count)
