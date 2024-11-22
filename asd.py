def factorial(n):
    """
    Вычисляет факториал числа n.

    :param n: Целое число, для которого нужно вычислить факториал.
    :return: Факториал числа n.
    """
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Пример использования функции
if __name__ == "__main__":
    number = 5
    print(f"Факториал числа {number} равен {factorial(number)}")
#21312