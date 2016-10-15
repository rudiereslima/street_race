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

diretorio = os.path.join("imagens", "pessoa.png")
pessoa1 = pygame.image.load(diretorio)

diretorio = os.path.join('imagens', 'policial.png')
policial = pygame.image.load(diretorio)

diretorio = os.path.join("fontes", "Aero Matics Bold.ttf")
fonte = pygame.font.Font(diretorio, 24)

		
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
		by = by + 5	
	if criar:
		ax = random.randint(214, 584)
		by = 0
		criar = False

	if by > 600:
		criar = True
			
	tela.blit(carro2, (ax - iraio, by - iraio))
	
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
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			jogando = False
	
	segundo = segundo - 0.02
	
	if segundo == 0:
		jogando = False
		time.sleep(5)
		pygame.display.quit()	

	pista()
	carros()
	player()	
	texto()
	policia()
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

	pygame.display.update()

	if vida < 1: 
		time.sleep(5)	
		pygame.display.quit()
sys.exit()	
	 					

									
