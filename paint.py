from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circulo(start, end):
    up() #Terminar con el dibujo anterior
    goto(start.x, start.y) #Obtener las coordenadas del cursor
    down() #Comenzar a pintar
    radio = (end.x - start.x) #Calcular radio con las coordenadas del cursor
    begin_fill() #Rellenar figura
    circle(radio) #Función de la libreria
    end_fill() #Dejar de rellenar

def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    #ir a las coordenadas donde se hizo el primer click
    goto(start.x, start.y)
    down()
    begin_fill()
    #ciclo que se repite dos veces donde se dibujan dos de los lados del rectángulo
    for _ in range(2):
        #Dibujar la arista horizontal 
        forward(end.x - start.x)
        #girar
        left(90)
        #Dibujar la arista vertical
        forward(end.y - start.y)
        left(90)
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward((((end.x - start.x)**2) + ((end.y - start.y)**2))**(1/2))
        left(120)
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()