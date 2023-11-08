def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input("Введите количество чисел: "))

numbers = []
for i in range(n):
    number = float(input(f"Введите число {i+1}: "))
    numbers.append(number)

bubble_sort(numbers)

print("Отсортированный список по возрастанию:")
for number in numbers:
    print(number)
