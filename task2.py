task_list_2 = []
elem = ''

while True:
    elem = input("Введите элемент списка: ")
    if elem == "fin":
        break
    task_list_2.append(elem)
    print("Для завершения заполнения списка напишите 'fin'")


if len(task_list_2) % 2 == 0:
    i = 0
    while i < len(task_list_2):
        elem = task_list_2[i]
        task_list_2[i] = task_list_2[i+1]
        task_list_2[i+1] = elem
        i += 2
else:
    i = 0
    while i < len(task_list_2) - 1:
        elem = task_list_2[i]
        task_list_2[i] = task_list_2[i + 1]
        task_list_2[i + 1] = elem
        i += 2
print(task_list_2)