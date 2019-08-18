from sudoku import *
import pygame

grid = easy()
def printtext(num = '0',x=0,y=0):
    if type(num) != str:
        num = str(num)
    if type(x) != int:
        x = int(x)
    if type(y) != int:
        y = int(y)

    myfont = pygame.font.SysFont('Comic Sans MS',30)
    textsurface = myfont.render(num,False,white)
    gameDisplay.blit(textsurface,(x,y))


def back(x=0,y=0):
    gameDisplay.blit(backg,(x,y))


def rect(x,y,width,height,color):
    pygame.draw.rect(gameDisplay,color,[x,y,width,height])

def quitgame():
    pygame.quit()
    quit()


def button(msg,x,y,w,h,inactive,active):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if ((y+h) > mouse[1] > y) & (( x+ w) > mouse[0] > x):
        color = active
    else:
        color = inactive

    pygame.draw.rect(gameDisplay,color,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf , textRect = text_objects(msg,smallText)
    textRect.center = (( x+ (w/2)),(y+(h/2)) )
    gameDisplay.blit(textSurf,textRect)
    if color == active and click[0] == 1:
        return True
    return False

def text_objects(text,font,color = (0,0,0)):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()




if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('sudoku solver')

    display_width = 1067
    display_height = 600
    disp = (display_width,display_height)
    gameDisplay = pygame.display.set_mode(disp)
    backgroundpic = "2.png"
    backg = pygame.image.load(backgroundpic)
    
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    gold = (212,175,55)
#    main = sudoku.main
    while True:
        back()
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                quitgame()
#        print(dir(sudoku))
        main()
        


