import pygame
import random

# "f" if flag
# "e" is event             /\
# moving on the arrows  <- \/ ->  

pygame.init()

field_size = 50
screen_width = 20
screen_height = 20
screen = pygame.display.set_mode((screen_height * field_size, screen_width * field_size))
count_bombs = 20


class Field():
    active = False
    bomb = False
    number = 0
    flag = False


field_pic = pygame.image.load("field.png")
field_pic = pygame.transform.scale(field_pic, (field_size, field_size))

coursor_pic = pygame.image.load("coursor.png")
coursor_pic = pygame.transform.scale(coursor_pic, (field_size, field_size))

bomb_pic = pygame.image.load("field.png")
bomb_pic = pygame.transform.scale(bomb_pic, (field_size, field_size))

zero_pic = pygame.image.load("zero.png")
zero_pic = pygame.transform.scale(zero_pic, (field_size, field_size))

one_pic = pygame.image.load("one.png")
one_pic = pygame.transform.scale(one_pic, (field_size, field_size))

two_pic = pygame.image.load("two.png")
two_pic = pygame.transform.scale(two_pic, (field_size, field_size))

three_pic = pygame.image.load("three.png")
three_pic = pygame.transform.scale(three_pic, (field_size, field_size))

four_pic = pygame.image.load("four.png")
four_pic = pygame.transform.scale(four_pic, (field_size, field_size))

five_pic = pygame.image.load("five.png")
five_pic = pygame.transform.scale(five_pic, (field_size, field_size))

six_pic = pygame.image.load("six.png")
six_pic = pygame.transform.scale(six_pic, (field_size, field_size))

end_pic = pygame.image.load("end.png")
end_pic = pygame.transform.scale(end_pic, (screen_height * field_size, screen_width * field_size))

flag_pic = pygame.image.load("flag.png")
flag_pic = pygame.transform.scale(flag_pic, (field_size, field_size))

field = []
for i in range(screen_height * screen_width):
    a = Field()
    field.append(a)
bombs_pos = 0

while True:
    if bombs_pos < count_bombs:
        a = random.randint(0, len(field) - 1)

        if field[a].bomb != True:
            field[a].bomb = True
            bombs_pos += 1
    else:
        break

i = 0
while i < screen_height:
    field[i:i + screen_width] = [field[i:i + screen_width]]
    i += 1

for i in range(screen_height):
    for j in range(screen_width):  # главный прогон
        if field[i][j].bomb == True:
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):  # прогон по первой окружности
                    if k < 0 or k >= screen_height or l < 0 or l >= screen_width or (k == i and l == j):
                        continue
                    if k == i and l == j:
                        field[k][l].number = -1
                        continue
                    bombs = 0
                    for m in range(k - 1, k + 2):
                        for n in range(l - 1, l + 2):  # прогон по второй окружности
                            if m < 0 or m >= screen_height or n < 0 or n >= screen_width:
                                continue
                            if field[m][n].bomb == True:
                                bombs += 1
                    field[k][l].number = bombs
                    bombs = 0

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j].bomb == True:
            field[i][j].number = -1

x = screen_width // 2
y = screen_height // 2

start = True
while start:
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.QUIT:
            pygame.quit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x - 1 >= 0:
        x -= 1
    elif pressed[pygame.K_RIGHT] and x + 1 < screen_width:
        x += 1
    elif pressed[pygame.K_UP] and y - 1 >= 0:
        y -= 1
    elif pressed[pygame.K_DOWN] and y + 1 < screen_height:
        y += 1
    elif pressed[pygame.K_e]:

        if field[y][x].flag == True:
            continue
        field[y][x].active = True
        if field[y][x].bomb == True:
            # screen.blit(bomb_pic, (i * field_size, j * field_size))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                screen.blit(end_pic, (0, 0))
                pygame.display.update()
    elif pressed[pygame.K_f]:
        if field[y][x].flag == True:
            field[y][x].flag = False
        else:
            field[y][x].flag = True
    for i in range(screen_height):
        for j in range(screen_width):
            # pygame.display.update()
            if field[i][j].active == False:
                if field[i][j].flag == True:
                    screen.blit(flag_pic, (j * field_size, i * field_size))
                else:
                    screen.blit(field_pic, (j * field_size, i * field_size))
            else:

                if field[i][j].number == -1:
                    screen.blit(bomb_pic, (j * field_size, i * field_size))
                if field[i][j].number == 0:
                    screen.blit(zero_pic, (j * field_size, i * field_size))
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            if k < 0 or k >= screen_height or l < 0 or l >= screen_width or (k == i and l == j):
                                continue
                            # if field[k][l].number==0:
                            field[k][l].active = True

                elif field[i][j].number == 1:
                    screen.blit(one_pic, (j * field_size, i * field_size))
                elif field[i][j].number == 2:
                    screen.blit(two_pic, (j * field_size, i * field_size))
                elif field[i][j].number == 3:
                    screen.blit(three_pic, (j * field_size, i * field_size))
                elif field[i][j].number == 4:
                    screen.blit(four_pic, (j * field_size, i * field_size))
                elif field[i][j].number == 5:
                    screen.blit(five_pic, (j * field_size, i * field_size))
                elif field[i][j].number == 6:
                    screen.blit(six_pic, (j * field_size, i * field_size))
    screen.blit(coursor_pic, (x * field_size, y * field_size))

    pygame.display.update()
