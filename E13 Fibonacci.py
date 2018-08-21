times = int(input('How many fibonacci numbers?'))

def make_fib(num):
    fib = [1, 1]
    if num == 0:
        fib = []
    if num == 1:
        fib = [1]
    if num > 1:
        for i in range(num -2):
            fib.append(fib[-1] + fib[-2])

    print(fib)
    return fib

make_fib(times)
