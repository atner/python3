#enumerate
#цикл в списке, который также отслеживает индекс текущего элемента. 
students = ('James', 'Andrew', 'Mark')
for i, student in enumerate(students):
    print i, student
# вывод:
# 0 James
# 1 Andrew
# 2 Mark 


#set
#примеры
colours = set(['red', 'green', 'blue', 'yellow', 'orange', 'black', 'white'])
# либо используйте новейший синтаксис для объявления списка.
input_values = {'red', 'black', 'pizza'}
# получаем список допустимых цветов
valid_values = input_values.intersection(colours)
print(valid_values)
# вывод set(['black', 'red'])
# получаем список недопустимых цветов
invalid_values = input_values.difference(colours)
print(invalid_values)
# вывод set(['pizza'])
# если что-то не так, выкидываем исключение
if not input_values.issubset(colours):
    raise ValueError("Invalid colour: " + ", ".join(input_values.difference(colours)))
    
    
#Условные выражения
# делаем число всегда нечетным 
number = count if count % 2 else count - 1
# вызываем функцию, если объект не None 
name = user.name() if user is not None else 'Guest'
print("Hello", name)

#Списковое включение
numbers = [1, 2, 3, 4, 5, 6, 7]
squares = []
for num in numbers:
    squares.append(num * num)
# со сжатием списка 
squares = [num * num for num in numbers]

#добавим фильтрацию или условный оператор
numbers = [1, 2, 3, 4, 5, 6, 7]
# квадраты всех нечетных чисел
squares = [num * num for num in numbers if num % 2]
# умножаем четные числа на 2 и нечетные на 3
mul = [num * 3 if num % 2 else num * 2 for num in numbers]

#========================================= генераторы ======================
#Выражения-генераторы
#не вычисляет до того момента, пока не запросим значение
# выражение-генератор для квадратов всех чисел
squares = (num * num for num in numbers)
# в противном случае вы получите проблему с памятью
with open('/some/number/file', 'r') as f:
    squares = (int(num) * int(num) for num in f)
    # делаем что-то с этими числами

#Генераторы с использованием yield
import random
def random_numbers(high=1000):
    while True:
        yield random.randint(0, high)
     
#генераторы
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# Печатает все числа последовательности Фибоначчи, меньше 1000
for i in fibonacci_generator():
    if  i > 1000:
        break
    print(i)
#простые генераторы
a = (x * x for x in range(100))
# a объект-генератор
print(type(a))
# Сумма всех чисел
print(sum(a))
# В генераторе не осталось чисел
print(sum(a))
#================================================
    
#Словарное включение
teachers = {
    'Andy': 'English',
    'Joan': 'Maths',
    'Alice': 'Computer Science',
}
# используем  списковое включение
subjects = dict((subject, teacher) for teacher, subject in teachers.items())
# используем словарное включение 
subjects = {subject: teacher for teacher, subject in teachers.items()}


#zip
#zip()принимает несколько итераций и присоединяет n-й элемент каждого в кортеж- tuple. 
names = ('James', 'Andrew', 'Mark')
for i, name in zip(random_numbers(), names):
    print i, name
# вывод:
# 288 James
# 884 Andrew
# 133 Mark
dict(zip(names, random_numbers()))
# вывод: {'James': 992, 'Andrew': 173, 'Mark': 329} 

#========================================================= на все случаи ==================================

#Лямбда функции:
max_xy = lambda x,y: x if x > y else y

#Map функции:
n = [1,2,3,4]
print((map(lambda x:x**2 + 2, n)))

#Reduce функции:
n = [1,2,3,4]
print(reduce (lambda x,y: x*y, n))

#Filter функции:
n = [1,2,3,4]
print (list(filter(lambda x: x > 2, n)))

#Быстрая сортировка:
qsort = lambda l : l if len(l)<=1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])

#Расстояние между двумя точками:
dist = lambda w,v : (sum((wi - vi)**2 for wi,vi in zip(w,v)))**.5

#Значение числа Пи:
4*sum((-1.0)**(n%2) / (2*n + 1) for n in range(2010))

#Генерация непрерывного массива чисел:
print map(lambda x:x+1,range(0,20))

#Простые числа от 0 до 1000:
print (filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0, map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000))))

#Первые 20 чисел Фибоначчи:
print( map(lambda x,f=lambda x,f:(x<=1) or (f(x-1,f)+f(x-2,f)): f(x,f), range(20)) )

#Все возможные сочетания:
cross_product = [(a, b) for a in ['a', 'b', 'c'] for b in [1, 2, 3]]

#Отрезать конец одной строки и добавить его к другой:
def foo(string, numbers): return ', '.join(map(lambda s,n:s+str(n), [string for i in numbers], numbers))

#========================== Линейная алгебра ========================

#Умножение вектора на число:
def scale(A, x): return [ai*x for ai in A]
scale([3,4,5], 2)

# Сложение векторов:
A = [1, 2, 3]
B = [5, 8, 10]
def add(A, B): return [ai+bi for (ai, bi) in zip(A, B)]
add(A,B)

#Транспонирование матрицы:
a=[[1,2,3],[4,5,6],[7,8,9]]
inverted_a = [list(i) for i in zip(*a)]

#Другое

#Случайный элемент:
import random; random.choice(['alpha', 'beta', 'gamma', 'delta'])

#Задание списка или множества операций:
M = ['a', 'b', 'c', 'c', '1', '100', 'a10']
M.append('Beta')


