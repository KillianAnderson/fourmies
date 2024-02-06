import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("La rencontre des fourmis")

# Affichage des collisions
collision = 0
police = pygame.font.Font(None, 60)
longueurScreen, hauteurScreen = screen.get_size()
textZone = police.render("Collisions : " + str(collision), 1, (255,255,255))
largeur_element = textZone.get_width()

# Créations des fourmis
class Fourmi : 
    def __init__(self, position_x, position_y, taille):
        self.position_x = position_x
        self.position_y = position_y
        self.taille = taille
        self.demiTour = False

nombreFourmiGauche = 15
nombreFourmiDroite = 7

listFourmiGauche = []
listFourmiDroite = []

for i in range(nombreFourmiGauche):
    listFourmiGauche.append(Fourmi(i*40, 250, 10))

for i in range(nombreFourmiDroite):
    listFourmiDroite.append(Fourmi(longueurScreen - i*40, 250, 10))

vitesse = 0.5
precedenteFourmiPos = 0

# Lancement de la game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(textZone, ((longueurScreen - largeur_element) // 2,50))

    for fourmi in listFourmiGauche:
        pygame.draw.rect(screen, (220,20,20), (fourmi.position_x + 20, fourmi.position_y, fourmi.taille, 5) )
    for fourmi in listFourmiDroite:
        pygame.draw.rect(screen, (20,20,220), (fourmi.position_x - 50, fourmi.position_y, fourmi.taille, 5) )

    for index, fourmi in enumerate(listFourmiGauche):
        if index < (len(listFourmiGauche)-2):
            i = index+1
        else:
            i = 0
        if index > 2:
            precedenteFourmiPos = listFourmiGauche[index-1].position_x
        if (fourmi.position_x + fourmi.taille) == listFourmiGauche[i].position_x or (fourmi.position_x + fourmi.taille) == listFourmiDroite[0].position_x or fourmi.position_x == (precedenteFourmiPos  + fourmi.taille) :
            fourmi.demiTour = True; 
        fourmi.position_x = fourmi.position_x + vitesse if not fourmi.demiTour else fourmi.position_x - vitesse
        print("Fourmi 1 : ", fourmi.position_x)
        print("Fourmi 2 : ", listFourmiGauche[i].position_x)

    for index, fourmi in enumerate(listFourmiDroite):
        if index < (len(listFourmiDroite)-2):
            i = index+1
        else:
            i = 0
        if index > 2:
            precedenteFourmiPos = listFourmiDroite[index-1].position_x
        if (fourmi.position_x + fourmi.taille) == listFourmiDroite[i].position_x or (fourmi.position_x + fourmi.taille) == listFourmiGauche[0].position_x or (fourmi.position_x + fourmi.taille) == precedenteFourmiPos:
            fourmi.demiTour = True; 
        fourmi.position_x = fourmi.position_x - vitesse if not fourmi.demiTour else fourmi.position_x + vitesse
        
    


    



    pygame.display.update()



pygame.quit()
sys.exit()