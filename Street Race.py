import pygame, os, sys
import random 


pygame.init()


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
	by = by + 2

	tela.blit(carro2, (ax, by))
		

ax1 = 0
by1 = 0
def player():
	global ax1, by1
	
	key = pygame.key.get_pressed()

	if key[pygame.K_LEFT]:
		ax1 = ax1 - 5

	elif key[pygame.K_RIGHT]:
		ax1 = ax1 + 5
	
	if ax1 >= 160:
		ax1 = 160
	
	if ax1 <= - 220:
		ax1 = -220
	
	tela.blit(carro, (ax1 + 400, by1 + 450))
	

jogando = True

while jogando:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			jogando = False
	
	tela.blit(fundo, (0, 0))
	carros()
	player()	
	pygame.display.update()
	 					

									
