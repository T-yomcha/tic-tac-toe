import pygame
import sys

def check_win(mas, sign):
    zero = 0
    for row in mas:
        zero += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
        if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
            return sign
        if mas[0][2] == sign and mas[1][col] == sign and mas[2][0] == sign:
            return sign
        if zero == 0:
            return "Piece"
        else:
            return False
pygame.init()
size_block = 100
size = (340, 340)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("krestiki-noliki")

width = height = 100

red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)

margin = 10

mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            #print(f'x = {x_mouse} y = {y_mouse}')
            col = x_mouse // (margin + width)
            row = y_mouse // (margin + height)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
            query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * width + (col + 1) * margin
                y = row * height + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, width, height))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 5)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()

