import pygame
import math

WIDTH, HEIGHT = 640, 480
background_color = (255, 255, 255)
line_width = 2

x = 0
y = 0
mode = 'blue'

def line(surface, start, end, color, width):
    """Рисует линию на заданной поверхности."""
    # Для создания более толстой линии без просветов
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

    final_r = int(math.hypot(p1[0] - center_x, p1[1] - center_y))

    if final_r > 0:
        pygame.draw.circle(surface, color, center, final_r, width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    global canvas
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(background_color)

    radius = 15

    current_tool = 'pencil'
    current_color = (0,0,0)

    start_pos = None
    is_drawing = False

    points = []

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

                elif event.key == pygame.K_1:
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_2:
                    current_color = (0, 255, 0)
                elif event.key == pygame.K_3:
                    current_color = (0, 0, 255)
                elif event.key == pygame.K_4:
                    current_color = (0,0,0)
            
            # Обработка нажатий мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Левая кнопка: Начало рисования/выделения
                    is_drawing = True
                    start_pos = event.pos
                    
                    # Имитация добавления точек для совместимости с drawLineBetween
                    points = [event.pos] 
                    
                elif event.button == 4: # Скролл вверх: Увеличить толщину
                    radius = min(200, radius + 1)
                elif event.button == 5: # Скролл вниз: Уменьшить толщину
                    radius = max(1, radius - 1)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # Левая кнопка отпущена: Фиксация фигуры
                    is_drawing = False
                    end_pos = event.pos
                    
                    # 1. Фиксация прямоугольника (Draw rectangle)
                    if current_tool == 'rect' and start_pos:
                        rectangle(canvas, start_pos, end_pos, current_color, line_width)
                    
                    # 2. Фиксация круга (Draw circle)
                    elif current_tool == 'circle' and start_pos:
                        circle(canvas, start_pos, end_pos, current_color, line_width)
                    
                    start_pos = None
                    points = [] # Очищаем точки после завершения рисования
            
            elif event.type == pygame.MOUSEMOTION:
                if is_drawing:
                    if current_tool in ('pencil', 'eraser'):
                        # 3. Ластик (Eraser) и Карандаш
                        # Для непрерывного рисования добавляем точки
                        position = event.pos
                        if points:
                            # Здесь используется слегка измененная drawLineBetween
                            # Она теперь рисует на CANVAS, а не на screen
                            color_mode = 'eraser' if current_tool == 'eraser' else current_color
                            drawLineBetween(canvas, len(points), points[-1], position, radius, color_mode)
                        points.append(position)
                        
                        # Удаление старых точек (как в оригинале)
                        points = points[-256:]
        screen.fill((255, 255, 255))
        screen.blit(canvas, (0,0))
        
        if is_drawing and start_pos and current_tool in ('rect', 'circle'):
            current_pos = pygame.mouse.get_pos()
            
            # Предварительный просмотр фигуры: рисуем на 'screen', а не на 'CANVAS'
            # (чтобы она исчезала в следующем кадре, если не зафиксирована)
            if current_tool == 'rect':
                rectangle(screen, start_pos, current_pos, current_color, line_width)
            elif current_tool == 'circle':
                circle(screen, start_pos, current_pos, current_color, line_width)
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
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