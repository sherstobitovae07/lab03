def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Меняем элементы, если текущий больше следующего
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input("Введите количество чисел: "))

# добавляем в список
numbers = []
for _ in range(n):
    number = int(input(f"Введите число {_+1}: "))
    numbers.append(number)

bubble_sort(numbers)

print("Отсортированные числа:", numbers)
