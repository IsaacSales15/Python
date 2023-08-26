import pygame
from pygame.locals import*
from OpenGL.GL import*

lagura_Janela = 640

altura_Janela = 480

xDabola = 0
yDaBola = 0
tamanhoDaBola = 20
velocidadeDaBolaX = 0.250
velocidadeDaBolaY = 0.250

yJogador1 = 0
yJogador2 = 0

def xDoJogador1():
    return -lagura_Janela / 2 + laguraDosJogadores() / 2

def xDoJogador2():
    return -lagura_Janela / 2 - laguraDosJogadores() / 2

def laguraDosJogadores():
    return tamanhoDaBola

def alturaDosJogadores():
    return 3 * tamanhoDaBola

def atualizar():
    global xDabola, yDaBola, velocidadeDaBolaX, velocidadeDaBolaY, yJogador1, yJogador2

    xDabola = xDabola + velocidadeDaBolaX
    yDaBola = yDaBola + velocidadeDaBolaY

    if (xDabola + tamanhoDaBola / 2 > xDoJogador2() -laguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yJogador2 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yJogador2 + alturaDosJogadores() / 2 ):
        velocidadeDaBolaX = -velocidadeDaBolaX
    
    if (xDabola + tamanhoDaBola / 2 > xDoJogador1() + laguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yJogador1 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yJogador1 - alturaDosJogadores() / 2 ):
        velocidadeDaBolaX = -velocidadeDaBolaX
    
    if yDaBola + tamanhoDaBola / 2 > altura_Janela / 2:
        velocidadeDaBolaY = -velocidadeDaBolaY

    if yDaBola - tamanhoDaBola / 2 < -altura_Janela / 2:
        velocidadeDaBolaY = -velocidadeDaBolaY

    if xDabola < -lagura_Janela / 2 or xDabola > lagura_Janela / 2:
        xDabola = 0
        yDaBola = 0

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        yJogador2 = yJogador2 + 0.5
        yJogador1 = yJogador1 + 0.5

    if keys[K_s]:
        yJogador2 = yJogador2 - 0.5
        yJogador1 = yJogador1 - 0.5

    if keys[K_UP]:
        yJogador2 = yJogador2 + 0.5
        yJogador1 = yJogador1 + 0.5
    
    if keys[K_DOWN]:
        yJogador2 = yJogador2 - 0.5
        yJogador1 = yJogador1 - 0.5


def retanguloDesenhar(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():
    glViewport(0, 0, lagura_Janela, altura_Janela)

    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(-lagura_Janela / 2, lagura_Janela / 2, -altura_Janela / 2, altura_Janela / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    retanguloDesenhar(xDabola, yDaBola, tamanhoDaBola, tamanhoDaBola, 1, 1, 0)
    retanguloDesenhar(xDoJogador1(), yJogador1, laguraDosJogadores(), alturaDosJogadores(), 1,0,0)
    retanguloDesenhar(xDoJogador2(), yJogador2, laguraDosJogadores(), alturaDosJogadores(), 0,0,1)

    pygame.display.flip()

pygame.init()
pygame.display.set_mode((lagura_Janela, altura_Janela), DOUBLEBUF | OPENGL )


while True:
    atualizar()
    desenhar()
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.event.pump()