# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1  

n = int (input('Введите количество элементов в массиве: '))
l = [0] * n
for i in range (len(l)):
    l[i] = int (input(f'Введите {i} элемент массива: '))
X = int (input('Введите искомый элемент X: '))
count = 0
for i in l:
    if i == X:
        count+=1  
    
  
print (f'Число {X} встречается {count} раз.')
