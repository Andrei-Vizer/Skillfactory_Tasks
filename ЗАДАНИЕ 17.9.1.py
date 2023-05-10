def binary_search(array, n, left, right):
    middle = (left + right) // 2

    if left > right:
        return f"Порядковый номер числа перед введенным значением: {middle}.\nПорядковый номер числа после введенного значения: {middle + 1}."
    if n < fir[0]:
        return f"Числа меньше введенного значения нет.\nПорядковый номер числа больше  либо равно введеному значению: {fir.index(min(seq))}."
    if middle + 1 > fir.index(max(fir)):
        return f"Числа больше введенного значения нет.\nПорядковый номер числа меньше  либо равно введеному значению: {len(fir)-1}."

    if array[middle] == n:
        if middle - 1 < 0:
            return f"Числа меньше введенного значения нет.\nПорядковый номер числа, равно введенному значению: {middle}."
        else:
            return f"Порядковый номер числа меньше введенного значения: {middle - 1}.\nПорядковый номер числа, равно введенному значению: {middle}."
    elif n < array[middle]:
        return binary_search(array, n, left, middle - 1)
    else:
        return binary_search(array, n, middle + 1, right)


fir = input("Введите последовательность чисел через пробел: ")
seq = fir.replace(" ", "")

while seq.isdigit() is not True:
    print("Введены недопустимые символы.\nИспользуйте только цифры и пробел.")
    fir = input("Введите последовательность чисел через пробел: ")
    seq = fir.replace(" ", "")

num = int(input("Введите любое число: "))

fir = list(map(int, fir.split()))
fir.sort()
print(fir)

index = binary_search(fir, num, 0, len(fir)-1)
print(index)