import pygame, os, sys
import random 
import time
import math

pygame.init()

Branco = (255, 255, 255)

x = 800
y = 600

relogio = pygame.time.Clock()


tela = pygame.display.set_mode((x, y))
pygame.display.set_caption ('Street Race')

diretorio = os.path.join('imagens', 'Player.png')
carro = pygame.image.load(diretorio)

diretorio = os.path.join('imagens', 'pista.jpg')
fundo = pygame.image.load(diretorio)


diretorio = os.path.join('imagens', 'Carro2.png')
carro2 = pygame.image.load(diretorio)

diretorio = os.path.join('imagens', 'Carro1.png')
carro3 = pygame.image.load(diretorio)

diretorio = os.path.join('imagens', 'Carro3.png')
carro4 = pygame.image.load(diretorio)

diretorio = os.path.join("imagens", "pessoa.png")
pessoa1 = pygame.image.load(diretorio)

diretorio = os.path.join('imagens', 'policial.png')
policial = pygame.image.load(diretorio)

diretorio = os.path.join("fontes", "Aero Matics Bold.ttf")
fonte = pygame.font.Font(diretorio, 24)
fonte2 = pygame.font.Font(diretorio, 48)
		
ax = 0
by = 0
criar = True
iraio = 22
def carros():
	global criar, ax, by, iraio
	key = pygame.key.get_pressed()
	if key[pygame.K_DOWN]:
		by = by + 2
	else:
		by = by + 6	
	if criar:
		ax = random.randint(214, 584)
		by = 0
		criar = False

	if by > 600:
		criar = True
			
	tela.blit(carro2, (ax - iraio, by - iraio))

ax3 = 350
by3 = 0
criar1 = True
iraio3 = 25
def carros2():
	global criar1, ax3, by3, iraio3, by
	key = pygame.key.get_pressed()
	if key[pygame.K_DOWN]:
		by3 = by3 + 4
	else:
		by3 = by3 + 8	

	if by > 300 and criar1:
		ax3 = random.randint(214, 584)
		by3 = 0
		criar1 = False

	if by3 > 600:
		criar1 = True
			
	tela.blit(carro3, (ax3 - iraio3, by3 - iraio3))
ax4 = 280
by4 = 0
criar2 = True
iraio4 = 27
def carros3():
	global criar2, ax4, by4, iraio4, by
	key = pygame.key.get_pressed()
	if key[pygame.K_DOWN]:
		by4 = by4 + 6
	else:
		by4 = by4 + 10	

	if by > 500 and criar2:
		ax4 = random.randint(214, 584)
		by4 = 0
		criar2 = False

	if by4 > 600:
		criar2 = True
			
	tela.blit(carro4, (ax4 - iraio4, by4 - iraio4))
	
xa = 620
yb = 0
aa = 0
travessia = True
larg = 54
alt = 74
frame = 0.0
praio = 40
def pessoa():
	global xa, yb, travessia, frame, aa, vel
	
	xa = xa - 2
	yb = yb + 2
		
	if travessia:
		yb = random.randint(140, 290)
		travessia = False
	
	if frame >= 1.0:
		aa = aa + 98
		frame = 0.0
	frame = frame + 0.1
	
	if aa >= (98*2):
		aa = 0
	
	if xa <= -200:
		xa = 620
		travessia = True
		
	tela.blit(pessoa1, (xa-praio, yb-praio), (aa, 0, larg, alt))  

ax1 = 424
by1 = 474
vida = 1
nraio = 24
def player():
	global ax1, by1, nraio
	
	key = pygame.key.get_pressed()

	if key[pygame.K_LEFT]:
		ax1 = ax1 - 5

	elif key[pygame.K_RIGHT]:
		ax1 = ax1 + 5
	
	if ax1 >= 584:
		ax1 = 584
	
	if ax1 <= 214:
		ax1 = 214
		
	tela.blit(carro, (ax1-nraio, by1-nraio))

px = 100
py = 0
multa = True
mraio = 0 
def policia():
	global px, py, multa
	
	py = py + 2
	if multa:
		py = random.randint(100, 250)
		multa = False
	
	if py >= 1200:
		py = 100
		multa = True
	
	tela.blit(policial, (px-mraio, py-mraio))  


x2 = 0
y2 = 0
race = True
def pista():
	global x2, y2, race 
		
	key = pygame.key.get_pressed()
	if key[pygame.K_DOWN]:
		y2 = y2 - 8
	if race:
		y2 = y2 + 20
		
	if y2 > 250:
		y2 = random.randint(0, 0)

	tela.blit(fundo, (x2, y2-200))	


	
def texto():
	surface = fonte.render("Vida = " + str(vida),True, Branco)
	tela.blit(surface, (10, 10))
	surface = fonte.render("Tempo: %.f" % segundo ,True, Branco)
	tela.blit(surface, (10, 40))
	
jogando = True
segundo = 120
while jogando:
	relogio.tick(60)

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			jogando = False
	
	segundo = segundo - 0.02
	
	if segundo <= 0:
		surface = fonte2.render("You Win!", True, Branco)
		tela.blit(surface, (300, 300))	
		jogando = False
		time.sleep(5)
		pygame.display.quit()	

	pista()
	carros()
	carros2()
	player()	
	texto()
		
	if segundo <= 85:
		pessoa()

	if segundo <= 65:
		policia()

	if segundo <= 50:
		carros3()
	
	distancia = math.sqrt((ax-ax1)**2 + (by - by1)**2)
	if distancia < (iraio+nraio):
		vida = 0
			
	distancia1 = math.sqrt((ax1-xa)**2 + (by1 - yb)**2)
	if distancia1 < (iraio+praio):
		vida = 0
				
	key = pygame.key.get_pressed()
	distancia2 = math.sqrt((by1-py)**2)
	if distancia2 < (iraio+mraio) and not key[pygame.K_DOWN]:
		vida = 0
	
	distancia3 = math.sqrt((ax1-ax3)**2 + (by1 - by3)**2)
	if distancia3 < (iraio3+nraio):
		vida = 0
	
	distancia4 = math.sqrt((ax1-ax4)**2 + (by1 - by4)**2)
	if distancia4 < (iraio4+nraio):
		vida = 0

	if vida <= 0:
		surface = fonte2.render("Game Over!", True, Branco)
		tela.blit(surface, (300, 300))	
		jogando = False
	
	pygame.display.update()
	
	if vida < 1: 
		time.sleep(5)	
		pygame.display.quit()
sys.exit()	
	 					

									
