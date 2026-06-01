import math

for num in range(1, 251):
    if num <= 1:
        continue
    elif num == 2:
        print(num)
    elif num % 2 == 0:
        continue
    else:
        limit = int(math.sqrt(num)) + 1
        for i in range(3, limit, 2):
            if num % i == 0:
                break
        else:
            print(num)