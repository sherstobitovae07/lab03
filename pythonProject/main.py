def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Условие для сортировки по возрастанию или убыванию
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Запрашиваем количество чисел
n = int(input("Введите количество чисел: "))

# Запрашиваем сами числа и добавляем их в список
numbers = []
for _ in range(n):
    number = int(input(f"Введите число {_+1}: "))
    numbers.append(number)

# Запрашиваем направление сортировки
direction = input("Введите направление сортировки (введите 'возрастание' или 'убывание'): ").strip().lower()

# Определяем порядок сортировки (по умолчанию - по возрастанию)
if direction == "убывание":
    ascending = False
else:
    ascending = True

# Сортируем список пузырьковой сортировкой
bubble_sort(numbers, ascending)

# Выводим отсортированный список
print("Отсортированные числа:", numbers)
