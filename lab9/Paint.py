import pygame
import math

WIDTH, HEIGHT = 640, 480
background_color = (255, 255, 255)
line_width = 2

x = 0
y = 0
mode = 'blue'

def line(surface, start, end, color, width): # draws a line in a surface
    # Для создания более толстой линии без просветов
    try:
        pygame.draw.line(surface, color, start, end, width)
    except:
        pass

def rectangle(surface, p1, p2, color, width): # draws a rectangle from two corner points
    x1, y1 = p1 # рисуетт прямоугольник по двум противоположным углам
    x2, y2 = p2
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) # creates a rect using the smallest x/y and absolute width/height
    pygame.draw.rect(surface, color, rect, width)

def circle(surface, p1, p2, color, width): # function for circle drawing
    center_x = (p1[0] + p2[0]) // 2
    center_y = (p1[1] + p2[1]) // 2
    center = (center_x, center_y)

    final_r = int(math.hypot(p1[0] - center_x, p1[1] - center_y)) # calculate radius using distance from center to one point

    if final_r > 0:
        pygame.draw.circle(surface, color, center, final_r, width)

def draw_square(surface, p1, p2, color, width):
    x1, y1 = p1
    x2, y2 = p2
    side = min(abs(x1 - x2), abs(y1 - y2))  # одинаковые стороны
    rect = pygame.Rect(min(x1, x2), min(y1, y2), side, side)
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
    points = [(x1, y2), (x2, y2), (x1 + side//2, y2 - h)]
    pygame.draw.polygon(surface, color, points, width)

def draw_rhombus(surface, p1, p2, color, width):
    x1, y1 = p1
    x2, y2 = p2
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    points = [(cx + dx, cy), (cx, cy - dy), (cx - dx, cy), (cx, cy + dy)]
    pygame.draw.polygon(surface, color, points, width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    global canvas # separate surface for permanent drawings
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(background_color)

    radius = 15

    current_tool = 'pencil'
    current_color = (0,0,0)

    start_pos = None # for shapes
    is_drawing = False

    points = [] # stores points for freehand drawing 

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
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

                elif event.key == pygame.K_1:
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    current_color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    current_color = (0, 0, 255)
                elif event.key == pygame.K_4:
                    current_color = (0,0,0)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click - start drawing
                    is_drawing = True
                    start_pos = event.pos
                    
                    points = [event.pos] # reset stroke tracking
                    
                elif event.button == 4: # increase brush size
                    radius = min(200, radius + 1)
                elif event.button == 5: # decrease brush size
                    radius = max(1, radius - 1)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # finalize shape
                    is_drawing = False
                    end_pos = event.pos
                    
                    # Фиксация прямоугольника
                    if current_tool == 'rect' and start_pos:
                        rectangle(canvas, start_pos, end_pos, current_color, line_width)
                    
                    # Фиксация круга
                    elif current_tool == 'circle' and start_pos:
                        circle(canvas, start_pos, end_pos, current_color, line_width)
                    
                    elif current_tool == 'square':
                        draw_square(canvas, start_pos, end_pos, current_color, line_width)

                    elif current_tool == 'right_triangle':
                        draw_right_triangle(canvas, start_pos, end_pos, current_color, line_width)

                    elif current_tool == 'equilateral_triangle':
                        draw_equilateral_triangle(canvas, start_pos, end_pos, current_color, line_width)

                    elif current_tool == 'rhombus':
                        draw_rhombus(canvas, start_pos, end_pos, current_color, line_width)

                    start_pos = None
                    points = [] # reset shape start point
            
            elif event.type == pygame.MOUSEMOTION:
                if is_drawing:
                    if current_tool in ('rect', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'):
                        # Для непрерывного рисования добавляем точки
                        position = event.pos
                        current_pos = pygame.mouse.get_pos()
                        if current_tool == 'rect':
                            rectangle(screen, start_pos, current_pos, current_color, line_width)

                        elif current_tool == 'circle':
                            circle(screen, start_pos, current_pos, current_color, line_width)

                        elif current_tool == 'square':
                            draw_square(screen, start_pos, current_pos, current_color, line_width)

                        elif current_tool == 'right_triangle':
                            draw_right_triangle(screen, start_pos, current_pos, current_color, line_width)

                        elif current_tool == 'equilateral_triangle':
                            draw_equilateral_triangle(screen, start_pos, current_pos, current_color, line_width)

                        elif current_tool == 'rhombus':
                            draw_rhombus(screen, start_pos, current_pos, current_color, line_width)
                        if points:
                            color_mode = 'eraser' if current_tool == 'eraser' else current_color
                            drawLineBetween(canvas, len(points), points[-1], position, radius, color_mode)

                        points.append(position)
                        
                        # Ограничиваем длину списка точек для оптимизации
                        points = points[-256:]
        screen.fill((255, 255, 255))
        screen.blit(canvas, (0,0))
        
        if is_drawing and start_pos and current_tool in ('rect', 'circle'):
            current_pos = pygame.mouse.get_pos()
            
            # Предварительный просмотр фигуры: рисуем на screen, а не на canvas
            # чтобы она исчезала в следующем кадре, если не зафиксирована
            if current_tool == 'rect':
                rectangle(screen, start_pos, current_pos, current_color, line_width)
            elif current_tool == 'circle':
                circle(screen, start_pos, current_pos, current_color, line_width)
        # draw all points
        i = 0
        while i < len(points) - 1:
            color_mode = background_color if current_tool == 'eraser' else current_color   # если текущий инструмент — ластик, нужно стирать цветом фона
            drawLineBetween(screen, i, points[i], points[i + 1], radius, color_mode)
            i += 1

        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'eraser':
        color = background_color
    else: 
        color = color_mode
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(canvas, color, (x, y), width)

main()