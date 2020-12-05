# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time

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
