def is_prime(func):
    def wrapper(a, b, c):
        result1 = func(a, b, c)
        if result1 % 2 != 0 or result1 % 2 != 0:
            print('Простое')
        else:
            print('Составное')
        return result1
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_

result = sum_three(2, 3, 6)
print(result)
