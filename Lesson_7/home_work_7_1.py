# Реализовать класс Matrix (матрица). 
# Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, 
# расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() 
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() 
# для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица. 
# Подсказка: сложение элементов матриц выполнять поэлементно — 
# первый элемент первой строки первой матрицы складываем с 
# первым элементом первой строки второй матрицы и т.д.


from copy import deepcopy

class Matrix:
    """
    класс олицетворяющий матрицу
    матрица - система некоторых математических величин, 
    расположенных в виде прямоугольной схемы.
    """
    def __init__(self, matrix:list):
        """
        Инициализатор класса
        Принимает список из списков из которых будет строиться матрица
        """
        self.matrix = deepcopy(matrix)
        
    def __str__(self):
        """
        Перегрузка "Магического метода"
        срабатывает при передаче объекта функциям str() и print()
        преобразует объект к строке
        """
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)
    
    def __add__(self, other):
        """
        Перегрузка "Магического метода"
        срабатывает при участии объекта в операции сложения 
        в качестве операнда с левой стороны, 
        обеспечивает перегрузку оператора сложения.
        ВНИМАНИЕ:
            одно из условий сложения матриц является их одинаковый размер!
        """
        len_flag = True  # флаг соответсвия размеров матриц
        if len(self.matrix) != len(other.matrix):
            return "Матрицы нельзя сложить, их размер не совпадает!"
        elif len_flag: 
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    len_flag = False
        if not len_flag:
            return "Матрицы нельзя сложить, их размер не совпадает!"       
        else:
            result_matrix = []  # результатирующая матрица
            summa = []  # временный список для нахождения суммы
            for x in range(len(self.matrix)):
                for y in range(len(self.matrix[x])):
                    summa.append(self.matrix[x][y] + other.matrix[x][y])
                result_matrix.append(summa)
                summa = []
            return Matrix(result_matrix)
    
# списки из которых будут строиться матрицы    
first_matrix = [[31, 32], 
                [37, 43],
                [51, 86]]

second_matrix = [[3,  5,  32],
                 [2,  4,  6],
                 [-1, 64, -8]]

third_matrix = [[3, 5, 8, 3],
                [8, 3, 7, 1]]

# создание экземпляров класса Matrix
my_matrix_1 = Matrix(first_matrix)
my_matrix_2 = Matrix(second_matrix)
my_matrix_3 = Matrix(third_matrix)

# разделитель для более красивого вывода функции print()
separator = "----------------"

print(separator)
print(my_matrix_1)
print(separator)
print(my_matrix_2)
print(separator)
print(my_matrix_3)
print(separator)

# простенькие матрицы для проверки сложения
fifth_matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

sixth_matrix = [[9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]]

seventh_matrix = [[9, 8, 7, 2],
                [6, 5, 4],
                [3, 2, 1]]

my_matrix_4 = Matrix(fifth_matrix)
my_matrix_5 = Matrix(sixth_matrix)
my_matrix_6 = Matrix(seventh_matrix)

print(my_matrix_4 + my_matrix_5)
print(separator)
# и проверка сложения не равных матриц
print(my_matrix_4 + my_matrix_6)


