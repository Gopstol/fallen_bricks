import sys
import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

fps = 60
fpsClock = pygame.time.Clock()

x1 = 280
y1 = 410
wh = 50
hw = 30

score = 0
nscore = 0



fallen = pygame.font.SysFont('Droid Sans', 150, WHITE)
bricks = pygame.font.SysFont('Droid Sans', 150, WHITE)
start = pygame.font.SysFont('Droid Sans', 50, PINK)
namelogo = pygame.font.SysFont('Ubuntu', 10, PINK)
starter = 0



minspeed = 1
speed = 2


W, H = 640, 480

myfont = pygame.font.SysFont('Droid Sans', 30, WHITE)

healthnumber = pygame.font.SysFont('Droid Sans', 30, WHITE)

x2 = random.randint(0, W-wh)
y2 = 0-hw
speed2 = random.randint(minspeed, speed)

x3 = random.randint(0, W-wh)
y3 = 0-hw
speed3 = random.randint(minspeed, speed)

x4 = random.randint(0, W-wh)
y4 = 0-hw
speed4 = random.randint(minspeed, speed)

#MONEY

xmoney = random.randint(0, W-wh)
ymoney = 0-hw
speedmoney = random.randint(minspeed, speed)




fillsc = 0

fillsce = 0

sc = pygame.display.set_mode((W, H))



scalpha = pygame.display.set_mode((W, H))
alp = pygame.Surface((640, 480))
alpha = 255


preleveltext = pygame.font.SysFont('Tahoma', 50, WHITE)
preleveltextdate = pygame.font.SysFont('Tahoma', 50, WHITE)
preleveltext2 = pygame.font.SysFont('Tahoma', 50, WHITE)
gameovertext = pygame.font.SysFont('Tahoma', 50, WHITE)
statscirclepos = 105
aftergood = 0

startanim = 0
thenanim = 0

health = 3


pygame.display.set_caption('Fallen bricks')


while True:
    #start menu
    while True:
        sc.fill((0, 0, 0))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()


        starter += 1
        fallensurface = fallen.render('FALLEN', False, (0, 200, 64))
        brickssurface = bricks.render('BRICKS', False, (0, 200, 100))
        sc.blit(fallensurface, (0, 0))
        sc.blit(brickssurface, (0, 80))

        namelogosurface = namelogo.render("Guli studio  2019", False, (255, 255, 255))
        sc.blit(namelogosurface, (520, 460))


        if (starter >= 120 and starter <= 240) or starter >= 241:
            startsurface = start.render("press space to start", False, (230, 50, 230))
            sc.blit(startsurface, (100, 400))

        if starter == 240:
            starter = 0


        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            starter = 241
        if starter >= 350:

            health = 3
            score = 0
            alpha = 255

            break


        pygame.display.update()
        pygame.display.flip()



    while True:
        sc.fill((0, 0, 0))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

        stats = 1
        f = open('stats1', 'r')
        fl = f.read()
        f.close

        stats = 0
        f = open('stats0', 'r')
        flf = f.read()
        f.close

        preleveltextsurface = preleveltext.render('High score: '+ str(flf), False, (255, 255, 255))
        preleveltext2surface = preleveltext2.render('Last: ' + str(fl), False, (255, 255, 255))
        preleveltextdatesurface = preleveltextdate.render('Start', False, (0, 255, 255))
        sc.blit(preleveltextsurface, (75, 100))
        sc.blit(preleveltext2surface, (185, 200))
        sc.blit(preleveltextdatesurface, (225, 400))

        pygame.draw.circle(sc, WHITE, (200, 430), 10)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            startanim = 0
            thenanim = 1

        if startanim == 0:
            preleveltextdatesurface = preleveltextdate.render('Start', False, (0, 255, 255))
            sc.blit(preleveltextdatesurface, (225, 400))
        if startanim < 60 and startanim > 0:
            preleveltextdatesurface = preleveltextdate.render('Start', False, (255, 255, 255))
            sc.blit(preleveltextdatesurface, (225, 400))

        if thenanim == 1:
            startanim += 1

        if startanim == 60:
            preleveltextdatesurface = preleveltextdate.render('Start', False, (0, 255, 255))
            sc.blit(preleveltextdatesurface, (225, 400))
        elif startanim == 90:
            break

        pygame.display.update()
        pygame.display.flip()


    while True:

            #alpha screen
        while True:


            sc.fill((0,0,0))

            starter = 0


            pygame.draw.rect(sc, WHITE, (x1, y1, wh, hw))

            alp.set_alpha(alpha)
            alp.fill((0, 0, 0))
            scalpha.blit(alp, (0,0))

            alpha -= 1

            if alpha <= 0:

                break

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()






            pygame.display.update()
            pygame.display.flip()


        # Game loop.
        while True:
            sc.fill((0,0,0))

            fillsce = 0

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()

            textsurface = myfont.render(str(score), False, (255,255,255))
            healthnumbersurface = healthnumber.render(str(health), False, (255, 20, 20))


            pygame.draw.rect(sc, WHITE, (x1, y1, wh, hw))

            if y2 < H:
                pygame.draw.rect(sc, GRAY, (x2, y2, wh, hw))

            else:
                x2 = random.randint(0, W-wh)
                y2 = 0-hw
                speed2 = random.randint(minspeed, speed)


            if y3 < H:
                pygame.draw.rect(sc, GRAY, (x3, y3, wh, hw))
            else:
                x3 = random.randint(0,W-wh)
                y3 = 0 -hw
                speed3 = random.randint(minspeed, speed)

            if y4 < H:
                pygame.draw.rect(sc, GRAY, (x4, y4, wh, hw))
            else:
                x4 = random.randint(0,W-wh)
                y4 = 0-hw
                speed4 = random.randint(minspeed, speed)

            if ymoney < H:
                pygame.draw.circle(sc, YELLOW, (xmoney, ymoney),  int(wh/2), int(hw/2))
            else:
                xmoney = random.randint(0,W-wh)
                ymoney = 0-hw
                speedmoney = random.randint(minspeed, speed)


            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x1 >= 0:
                x1 -= 4
            elif keys[pygame.K_RIGHT] and (x1 + wh) <= W:
                x1 += 4



            y2 += speed2

            y3 += speed3

            y4 += speed4

            ymoney += speedmoney

            if ((y1 - y2 < hw and y1 - y2 >= 0) or (y2 - y1 < hw and y1 - y2 <= hw)) and  ((x1 - x2 < wh and x1 - x2 >= 0) or (x2 - x1 < wh and x1 - x2 <= wh)):
                y2 = H
                health -= 1
                break

            if ((y1 - y3 < hw and y1 - y3 >= 0) or (y3 - y1 < hw and y1 - y3 <= hw)) and  ((x1 - x3 < wh and x1 - x3 >= 0) or (x3 - x1 < wh and x1 - x3 <= wh)):
                y3 = H
                health -= 1
                break

            if ((y1 - y4 < hw and y1 - y4 >= 0) or (y4 - y1 < hw and y1 - y4 <= hw)) and  ((x1 - x4 < wh and x1 - x4 >= 0) or (x4 - x1 < wh and x1 - x4 <= wh)):
                y4 = H
                health -= 1
                break

            if ((y1 - ymoney < hw and y1 - ymoney >= 0) or (ymoney - y1 < hw and y1 - ymoney <= hw)) and  ((x1 - xmoney < wh and x1 - xmoney >= 0) or (xmoney - x1 < wh and x1 - xmoney <= wh)):
                ymoney = H
                score = score + 50

            nscore += 1

            if nscore == 30:
                score += 1
                nscore = 0


            sc.blit(textsurface,(0,0))
            sc.blit(healthnumbersurface, (625, 0))

            pygame.display.update()
            pygame.display.flip()


        #death
        while fillsce <= 60:


            sc.fill((255, 0, 0))
            pygame.draw.rect(sc, WHITE, (x1, y1, wh, hw))

            # if fillsc <= 30:
            #     sc.fill((255, 0, 0))
            # elif fillsc >= 30:
            #     sc.fill((0, 0, 0))
            #
            # fillsc += 1
            fillsce += 1

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()

            if fillsce == 60:
                print(score)
                print(fillsce)

                alpha = 155
                x2 = random.randint(0, W - wh)
                y2 = 0 - hw
                speed2 = random.randint(minspeed, speed)

                x3 = random.randint(0, W - wh)
                y3 = 0 - hw
                speed3 = random.randint(minspeed, speed)

                x4 = random.randint(0, W - wh)
                y4 = 0 - hw
                speed4 = random.randint(minspeed, speed)

                # MONEY

                xmoney = random.randint(0, W - wh)
                ymoney = 0 - hw
                speedmoney = random.randint(minspeed, speed)

                print(health)
                break
            startanim = 0
            thenanim = 0

            pygame.display.update()
            pygame.display.flip()
            if flf == '':
                flf = '0'
            if health <= 0:
                if score > int(flf):
                    f = open('stats0', 'w')
                    f.write(str(score))
                    f.close
                    f = open('stats1', 'w')
                    f.write(str(score))
                    f.close
                elif score <= int(flf):
                    f = open('stats1', 'w')
                    f.write(str(score))
                    f.close
                break
        if health <= 0:
            while True:
                sc.fill((0, 0, 0))

                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        exit()

                stats = 1
                f = open('stats1', 'r')
                fl = f.read()
                f.close

                stats = 0
                f = open('stats0', 'r')
                flf = f.read()
                f.close

                preleveltextsurface = preleveltext.render('High score: ' + str(flf), False, (255, 255, 255))
                preleveltext2surface = preleveltext2.render('Last: ' + str(fl), False, (255, 255, 255))
                preleveltextdatesurface = preleveltextdate.render('Ok', False, (0, 255, 255))

                gameoversurface = gameovertext.render('Game Over', False, (100, 200, 150))

                sc.blit(preleveltextsurface, (75, 100))
                sc.blit(preleveltext2surface, (185, 200))
                sc.blit(preleveltextdatesurface, (225, 400))

                sc.blit(gameoversurface, (185, 10))

                pygame.draw.circle(sc, WHITE, (200, 430), 10)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    startanim = 0
                    thenanim = 1

                if startanim == 0:
                    preleveltextdatesurface = preleveltextdate.render('Ok', False, (0, 255, 255))
                    sc.blit(preleveltextdatesurface, (225, 400))
                if startanim < 60 and startanim > 0:
                    preleveltextdatesurface = preleveltextdate.render('Ok', False, (255, 255, 255))
                    sc.blit(preleveltextdatesurface, (225, 400))

                if thenanim == 1:
                    startanim += 1

                if startanim == 60:
                    preleveltextdatesurface = preleveltextdate.render('Ok', False, (0, 255, 255))
                    sc.blit(preleveltextdatesurface, (225, 400))
                elif startanim == 90:
                    break

                x2 = random.randint(0, W - wh)
                y2 = 0 - hw
                speed2 = random.randint(minspeed, speed)

                x3 = random.randint(0, W - wh)
                y3 = 0 - hw
                speed3 = random.randint(minspeed, speed)

                x4 = random.randint(0, W - wh)
                y4 = 0 - hw
                speed4 = random.randint(minspeed, speed)

                # MONEY

                xmoney = random.randint(0, W - wh)
                ymoney = 0 - hw
                speedmoney = random.randint(minspeed, speed)

                pygame.display.update()
                pygame.display.flip()


            if health <= 0:
                print('hi')
                break
fpsClock.tick(fps)
