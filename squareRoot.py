def average(a, b):
    return (a + b) / 2

def square_root(n, low, high):
    for _ in range(20):
        guess = average(low, high)
        if guess ** 2 == n:
            return guess
        elif guess ** 2 > n:
            high = guess
        else:
            low = guess
    return guess

result = square_root(25, 0, 11)

print(result) # 5.0