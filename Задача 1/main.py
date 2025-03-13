def print_range(M, N):
    for num in range(M, N + 1):
        print(num, end=', ' if num < N else '\n')

# Пример использования
M = 1
N = 5
print("Числа в промежутке:")
print_range(M, N)
