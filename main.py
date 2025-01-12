import pygame
clock = pygame.time.Clock()  # Переменная, библиотека, значение, класс - это для анимации

pygame.init()
screen = pygame.display.set_mode((1200, 600))  # Устанавливаем размер окна
pygame.display.set_caption('GhostRun by Dashanimus')  # Название игры
icon = pygame.image.load('images/icon.png')  # icon - переменная, pygame - библиотека, .image - объект, load - метод
pygame.display.set_icon(icon)  # Указываем переменную icon

bg = pygame.image.load('images/bg.png').convert_alpha()  # background, конвертация в формат питона
bg = pygame.transform.scale(bg, (1000, 600))  # background scale


bg_sound = pygame.mixer.Sound('sounds/bg.mp3')  # Музыка игры
bg_sound.play(-1)  # (-1) - для зацикливания

walk_left = [
    pygame.image.load('images/player_left/Run_Left1.png').convert_alpha(),
    pygame.image.load('images/player_left/Run_Left2.png').convert_alpha()
]  # Список для анимации left

walk_right = [
    pygame.image.load('images/player_right/Run_Right1.png').convert_alpha(),
    pygame.image.load('images/player_right/Run_Right2.png').convert_alpha()
]  # Список для анимации right

player_anim_count = 0  # Переменная для анимации
bg_x = 0  # Переменная для анимации фона 1
bg_x1 = 1001  # Переменная для анимации фона 2

ghost = pygame.image.load('images/ghost.png').convert_alpha()  # Конвертация в формат питона
ghost_list_in_game = []

ghost_timer = pygame.USEREVENT + 1  # Подключили таймер для появления врагов
pygame.time.set_timer(ghost_timer, 3500)  # Враг появляется через 3 сек

label = pygame.font.Font('fonts/HussarMiloscOblique.otf', 35) # Переменная текста
loose_label = label.render('  Ой, призрак задет!', True, (255, 255, 255))
restart_label = label.render('> НАЧАТЬ СНАЧАЛА <', True, (0, 255, 255))
restart_label_rect = restart_label.get_rect(topleft=(400, 300))

gameplay = True

player_speed = 7  # Скорость игрока
player_x = 100  # Координата по горизонтали
player_y = 410  # Координата по вертикали

is_jump = False  # Переменная прыжка
jump_count = 11  # На ... позиций вверх

running = True  # Переменная, чтобы завершать цикл
while running:  # Это цикл

    screen.blit(bg, (bg_x, 0))  # Задний фон 1
    screen.blit(bg, (bg_x1, 0))  # Задний фон 2

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))  # Рисуем квадрат вокруг игрока

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):  # Перебираем весь список
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:  # Если враг за экраном, удаляем
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()  # Переменная нажатой кнопки
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))  # Анимация игрока left
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))  # Анимация игрока left right

        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 500:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True

        else:  # Процесс прыжка
            if jump_count >= -11:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2  # Возводим в степень и делим для плавности прыжка
                else:
                    player_y += (jump_count ** 2) / 2  # Опускаем игрока на поверхность
                jump_count -= 1
            else:  # Прыжок окончен
                is_jump = False
                jump_count = 9

        if player_anim_count == 1:
            player_anim_count = 0
        else:
            player_anim_count += 1  # К переменной добавляем 1, чтобы шла анимация игрока

        bg_x -= 8  # Переменная для скорости анимации фона 1
        bg_x1 -= 8  # Переменная для скорости анимации фона 2

        if bg_x <= -1001:  # Чтобы картинка не смещалась до такой степени, что мы её не видим
            bg_x = 1001
        elif bg_x1 <= -1001:
            bg_x1 = 1001

    else:
        screen.fill((0, 0, 0))
        screen.blit(loose_label, (310, 230))  # Выводим текст проигрыша
        screen.blit(restart_label, restart_label_rect)  # Выводим текст перезапуска

        mouse = pygame.mouse.get_pos()  # Когда нажимаем мышку - перезапуск
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 100
            player_y = 410
            ghost_list_in_game.clear()

    pygame.display.update()

    for event in pygame.event.get():  # Это цикл
        if event.type == pygame.QUIT:  # Кнопку выход нажали - выход
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1000, 430)))  # Добавление врага

    clock.tick(15)  # Анимация будет со скоростью 15 фреймов в сек
