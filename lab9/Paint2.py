import pygame
import math
import sys

WIDTH, HEIGHT = 640, 480
background_color = (255, 255, 255)
line_width = 2
CLOCK_RATE = 60 

canvas = None
current_tool = 'pencil' 


def line(surface, start, end, color, width): 
    try:
        pygame.draw.line(surface, color, start, end, width)
    except:
        pass

def rectangle(surface, p1, p2, color, width): 
    x1, y1 = p1
    x2, y2 = p2
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    pygame.draw.rect(surface, color, rect, width)

def circle(surface, p1, p2, color, width): 
    center_x = (p1[0] + p2[0]) // 2
    center_y = (p1[1] + p2[1]) // 2
    center = (center_x, center_y)

    final_r = int(math.hypot(p1[0] - center_x, p1[1] - center_y)) # Вычисляет радиус как расстояние от центра до одной из точек

    if final_r > 0:
        pygame.draw.circle(surface, color, center, final_r, width)

def draw_square(surface, p1, p2, color, width):
    x1, y1 = p1
    x2, y2 = p2
    side = min(abs(x1 - x2), abs(y1 - y2))
    
    x_start = min(x1, x2)
    y_start = min(y1, y2)
    
    if x2 < x1 and y2 < y1: # Движение вверх-влево
        x_start = max(x1 - side, x2)
        y_start = max(y1 - side, y2)
    elif x2 < x1: # Движение влево
        x_start = x1 - side
    elif y2 < y1: # Движение вверх
        y_start = y1 - side

    rect = pygame.Rect(x_start, y_start, side, side)
    pygame.draw.rect(surface, color, rect, width)

def draw_right_triangle(surface, p1, p2, color, width):
    x1, y1 = p1
    x2, y2 = p2
    points = [(x1, y1), (x2, y1), (x1, y2)]
    pygame.draw.polygon(surface, color, points, width)

def draw_equilateral_triangle(surface, p1, p2, color, width):
    x1, y1 = p1
    x2, y2 = p2
    side = abs(x2 - x1)
    
    h = int(side * (3**0.5) / 2)
    
    # Определяем, куда направлен треугольник (вверх или вниз)
    y_base = y2 # Основание по координате y второй точки
    
    x_peak = (x1 + x2) // 2 # Третья вершина (центр основания по x, и h по y)
    
    if y2 > y1: # Рисуем вверх (y уменьшается)
        y_peak = y_base - h
    else: # Рисуем вниз (y увеличивается)
        y_peak = y_base + h

    points = [(x1, y_base), (x2, y_base), (x_peak, y_peak)]
    pygame.draw.polygon(surface, color, points, width)


def draw_rhombus(surface, p1, p2, color, width):
    x1, y1 = p1
    x2, y2 = p2
    
    # Центр ромба
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    
    # Половины диагоналей
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    
    # Вершины ромба
    points = [
        (cx + dx, cy), # Правая
        (cx, cy - dy), # Верхняя
        (cx - dx, cy), # Левая
        (cx, cy + dy)  # Нижняя
    ]
    pygame.draw.polygon(surface, color, points, width)

def draw_freehand_stroke(start, end, width, color_mode):
    """
    Рисует непрерывную линию между двумя точками, используя круги. 
    Рисует на постоянном холсте (canvas).
    """
    global canvas, background_color
    
    # --- Fix 1: Корректное определение цвета для ластика ---
    if color_mode == 'eraser':
        color = background_color
    elif color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    else: 
        # Используем кортеж с текущим цветом, переданный из main
        color = color_mode 
    
    # Логика интерполяции точек
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        
        # Рисуем на постоянном холсте
        pygame.draw.circle(canvas, color, (x, y), width)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    global canvas, current_tool 
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(background_color)

    radius = 15
    current_color = (0,0,0)

    start_pos = None 
    is_drawing = False
    
    # Словарь для выбора функций отрисовки фигур
    shape_draw_functions = {
        'rect': rectangle,
        'circle': circle,
        'square': draw_square,
        'right_triangle': draw_right_triangle,
        'equilateral_triangle': draw_equilateral_triangle,
        'rhombus': draw_rhombus,
    }

    points = [] # Хранит точки для свободной кисти/ластика

    while True:
        
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_F4 and alt_held:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                # Выбор инструмента
                if event.key == pygame.K_p:
                    current_tool = 'pencil'
                elif event.key == pygame.K_r:
                    current_tool = 'rect'
                elif event.key == pygame.K_c:
                    current_tool = 'circle'
                elif event.key == pygame.K_e:
                    current_tool = 'eraser'
                elif event.key == pygame.K_s:
                    current_tool = 'square'
                elif event.key == pygame.K_t:
                    current_tool = 'right_triangle'
                elif event.key == pygame.K_q:
                    current_tool = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    current_tool = 'rhombus'

                # Выбор цвета
                elif event.key == pygame.K_1:
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    current_color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    current_color = (0, 0, 255)
                elif event.key == pygame.K_4:
                    current_color = (0,0,0)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Левый клик - начало рисования
                    is_drawing = True
                    start_pos = event.pos
                    
                    # Для кисти/ластика: начинаем отслеживание нового штриха
                    if current_tool in ('pencil', 'eraser'):
                        points = [event.pos] 
                    
                elif event.button == 4: # Увеличение размера кисти
                    radius = min(200, radius + 1)
                elif event.button == 5: # Уменьшение размера кисти
                    radius = max(1, radius - 1)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # Финализация фигуры/окончание штриха
                    is_drawing = False
                    end_pos = event.pos
                    
                    # Фиксация фигуры на холсте
                    if current_tool in shape_draw_functions and start_pos:
                        draw_func = shape_draw_functions[current_tool]
                        draw_func(canvas, start_pos, end_pos, current_color, line_width)
                    
                    start_pos = None
                    points = [] # Сброс точек штриха/фигуры
            
            elif event.type == pygame.MOUSEMOTION:
                if is_drawing:
                    position = event.pos
                    
                    # Логика для кисти/ластика рисует на canvas
                    if current_tool in ('pencil', 'eraser'):
                        # Определяем цвет для ластика или кисти
                        color_mode = 'eraser' if current_tool == 'eraser' else current_color
                        
                        if len(points) > 0:
                            # Рисуем на постоянном холсте canvas
                            draw_freehand_stroke(points[-1], position, radius, color_mode)
                        
                        points.append(position)
                        # Ограничиваем длину списка точек для оптимизации
                        points = points[-256:]


        screen.fill(background_color)
        
        screen.blit(canvas, (0,0))
        
        # 3. Предварительный просмотр фигуры (рисуем на screen)
        if is_drawing and start_pos and current_tool in shape_draw_functions:
            current_pos = pygame.mouse.get_pos()
            draw_func = shape_draw_functions[current_tool]
            # Рисуем только контур фигуры на текущем кадре
            draw_func(screen, start_pos, current_pos, current_color, line_width)
            
        pygame.display.flip()
        
        clock.tick(CLOCK_RATE)

if __name__ == '__main__':
    main()