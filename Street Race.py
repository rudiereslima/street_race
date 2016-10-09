import pygame, os, sys
import random 


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

diretorio = os.path.join("fontes", "Aero Matics Bold.ttf")
fonte = pygame.font.Font(diretorio, 24)


ax = 0
by = 0
criar = True

def carros():
	global criar, ax, by	
	if criar:
		ax = random.randint(180, 560)
		by = 0
		criar = False

	if by > 600:
		criar = True
	by = by + 10

	tela.blit(carro2, (ax, by))
		

ax1 = 400
by1 = 450
vida = 3
pontos = 0

def player():
	global ax1, by1
	
	key = pygame.key.get_pressed()

	if key[pygame.K_LEFT]:
		ax1 = ax1 - 5

	elif key[pygame.K_RIGHT]:
		ax1 = ax1 + 5
	
	if ax1 >= 560:
		ax1 = 560
	
	if ax1 <= 180:
		ax1 = 180
		
	tela.blit(carro, (ax1, by1))


x2 = 0
y2 = 0
race = True
def pista():
	global x2, y2, race 
	
	if race:
		y2 = y2 + 20
		
	
	if y2 > 250:
		y2 = random.randint(0, 0)

	tela.blit(fundo, (x2, y2-200))	

def texto():
	surface = fonte.render("Vida = " + str(vida),True, Branco)
	tela.blit(surface, (10, 10))
	surface = fonte.render("Pontos = " + str(pontos),True, Branco)
	tela.blit(surface, (10, 40))


jogando = True

while jogando:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			jogando = False
	
	pista()
	carros()
	player()	

	texto()
			

	pygame.display.update()

	
	 					

									
