import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 600))  # Устанавливаем размер окна
pygame.display.set_caption('Test Sample')  # Название игры

icon = pygame.image.load('images/icon.png')  # icon - переменная, pygame - библиотека, .image - объект, load - метод
pygame.display.set_icon(icon)  # Указываем переменную icon

square = pygame.Surface((700, 300))  # Surface - Класс "Поверхность"
square.fill('Blue')

myfont = pygame.font.Font('fonts/HussarMiloscOblique.otf', 40) # myfont - переменная, font - свойство,
# Font - класс (параметры - название шрифта, его размер)
text_surface = myfont.render('Press "F" key', True, 'White')  # False/True - сглаживание текста

player = pygame.image.load('images/snakes.png')

running = True  # Переменная, чтобы завершать цикл
while running:  # Это цикл

    pygame.draw.circle(screen, 'Green', (850, 150),30)  # method circle, parameter surface (screen/square),
   # coordinates (250, 150), radius (30)
    screen.blit(square, (10, 0))  # screen - переменная, blit - метод для размещения изображения на экране, копирует
    # пиксели изображения с одной поверхности на другую, square - ранее созданный объект, () - его кортеж = координаты
    screen.blit(text_surface, (300, 100))
    screen.blit(player, (100, 50))

    pygame.display.update()

    for event in pygame.event.get():  # Это цикл
        if event.type == pygame.QUIT:  # Кнопку выход нажали - выход
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:  # Нажали кнопку - меняем цвет
            if event.key == pygame.K_f:
                screen.fill((184, 0, 0))  # Заливка фона, RGB в качестве параметра (кортеж)
