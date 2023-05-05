import math
import time
import turtle


# заполнялка отсутупов
def filler():
    print()
    print()
    print()
    print()
    print()


# предупреждение
print('Не рекомендуется вводить очень маленькие (<0.001) и очень большие (>1000) данные, из-за проблем с '
      'производительностью python в вычислениях больших значений')
filler()
_ = input('С предупреждением ознакомлен, несу ответственность за своё железо (ввести любой символ): ')
filler()

# параметры на ввод
q = float(input('Заряд частицы (с учётом знака, МикроКулонах): '))
m = float(input('Масса частицы (в Атомарных Единицах Массы): '))
v = float(input('Скорость частицы (в Метрах в Секунду): '))
angle = float(input('Угол вхождения частицы в поле (в Градусах): '))
B = float(input('Индукция магнитного поля (в Теслах): '))
E = float(input('Сила электрического поля (в Ньютонах на Кулон): '))
dt = float(input('Временной шаг (в СантиСекундах): ')) / 100
direct = int(input('Направление поля (1 на наблюдателя, 0 от наблюдателя): '))
mashtab = float(input('Введите степень приближения/отдаления (значение больше/меньше 1) поля: '))

filler()

# константы
x = 0  # стартовая позиция
y = 0
vx = v * math.cos(math.radians(angle))  # стартовая скорость по x
vy = v * math.sin(math.radians(angle))  # стартовая скорость по y

# окно черепахи и сама черепаха
canvas = turtle.Screen()
canvas.setworldcoordinates(-1.5 / mashtab, -1.5 / mashtab, 1.5 / mashtab, 1.5 / mashtab)
canvas.delay(0)
particle = turtle.Turtle()
particle.penup()
particle.hideturtle()
particle.speed(1)

# обозначение направления магнитного поля
if direct == 0:
    particle.pensize(3)
    particle.goto(-1.2 / mashtab, -1.2 / mashtab)
    particle.pendown()
    particle.goto(-1.5 / mashtab, -1.5 / mashtab)
    particle.penup()
    particle.goto(-1.5 / mashtab, -1.2 / mashtab)
    particle.pendown()
    particle.goto(-1.2 / mashtab, -1.5 / mashtab)
    particle.penup()
    particle.goto(-1.2 / mashtab, 1.2 / mashtab)
    particle.pendown()
    particle.goto(-1.5 / mashtab, 1.5 / mashtab)
    particle.penup()
    particle.goto(-1.5 / mashtab, 1.2 / mashtab)
    particle.pendown()
    particle.goto(-1.2 / mashtab, 1.5 / mashtab)
else:
    particle.pensize(10)
    particle.goto(-1.19 / mashtab, -1.19 / mashtab)
    particle.pendown()
    particle.goto(-1.21 / mashtab, -1.19 / mashtab)
    particle.goto(-1.21 / mashtab, -1.21 / mashtab)
    particle.goto(-1.19 / mashtab, -1.21 / mashtab)
    particle.goto(-1.19 / mashtab, -1.19 / mashtab)
    particle.penup()
    particle.goto(-1.19 / mashtab, 1.19 / mashtab)
    particle.pendown()
    particle.goto(-1.21 / mashtab, 1.19 / mashtab)
    particle.goto(-1.21 / mashtab, 1.21 / mashtab)
    particle.goto(-1.19 / mashtab, 1.21 / mashtab)
    particle.goto(-1.19 / mashtab, 1.19 / mashtab)
particle.pensize(10)
particle.penup()
particle.goto(-0.0001, 0)
particle.pendown()
particle.goto(0, 0)
particle.pensize(1)
particle.write("(0, 0)")

# debug
debug = 0

# цикл симуляции
while abs(particle.pos()) < 15:
    # силы
    fx = q * (E + vy * B)
    fy = q * (vx * B)

    # ускорения
    ax = fx / m
    ay = fy / m

    # обновление скоростей
    vx += ax * dt
    vy += ay * dt

    # обновление позиции
    if direct == 0:
        x += vx * dt
        y += vy * dt
    else:
        x += vx * dt
        y -= vy * dt

    # внтуреннее время модели
    print(f'Смоделировано: {debug * dt} секунд')
    debug += 1

    # сместить частицу
    particle.goto(x, y)

    # мини задержка, для просмотра в реальном времени
    time.sleep(0.01)

# Вывод финальных координат
particle.pensize(10)
particle.color("Blue")
particle.goto(x + 0.01, y)
particle.penup()
particle.goto(-1 / mashtab, 1 / mashtab)
particle.write(f"Финальные координаты: ({x}, {y})")

# закрытие окна
canvas.exitonclick()
