# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

#Вариант 1

# 

# if a == b == c:
#     print('Треугольник равносторонний.')
# if a == b or b ==c or a == c:
#     print('Треугольник равнобедренный.')
# if a > b + c or b > a + c or c > a + b:
#     print('Треугольника с такими сторонами не существует.')
# print('END')

#Вариант 2

def exist_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    return True

def triangle_type(a, b, c):
    if not exist_triangle(a, b, c):
        return "Треугольник не существует"

    if a == b and b == c:
        return "Равносторонний треугольник"
    elif a == b or b == c or a == c:
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"
    
a = float(input('Введите первую сторону треугольника: '))
b = float(input('Введите вторую сторону треугольника: '))
c = float(input('Введите третью сторону треугольника: '))

print(triangle_type(a, b, c))