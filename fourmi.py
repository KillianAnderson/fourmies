import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 500))
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

vitesse = 0.3
precedenteFourmiPos = 0

# Lancement de la game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(listFourmiGauche[0])
            running = False

    screen.fill((0, 0, 0))
    screen.blit(textZone, ((longueurScreen - largeur_element) // 2,50))
    rouge = 0

    for fourmi in listFourmiGauche:
        rouge+=1

        if(rouge == 8):
            pygame.draw.rect(screen, (20,200,20), (fourmi.position_x + 20, fourmi.position_y, fourmi.taille, 5) )
        else:
            pygame.draw.rect(screen, (220,20,20), (fourmi.position_x + 20, fourmi.position_y, fourmi.taille, 5) )

    for fourmi in listFourmiDroite:
        pygame.draw.rect(screen, (20,20,220), (fourmi.position_x - 50, fourmi.position_y, fourmi.taille, 5) )

    for index, fourmi in enumerate(listFourmiGauche):
        if index < (len(listFourmiGauche)-1):
            i = index+1
        else:
            i = 0

        precedenteFourmiPos = listFourmiGauche[index-1].position_x
        if (fourmi.position_x + fourmi.taille) >= listFourmiGauche[i].position_x or (fourmi.position_x + fourmi.taille) >= listFourmiDroite[0].position_x or fourmi.position_x <= (precedenteFourmiPos  + fourmi.taille) :
            fourmi.demiTour = not fourmi.demiTour
            collision +=1
        fourmi.position_x = fourmi.position_x + vitesse if not fourmi.demiTour else fourmi.position_x - vitesse
       

    for index, fourmi in enumerate(listFourmiDroite):
        if index < (len(listFourmiDroite)-1):
            # print(index)
            i = index+1
        else:
            i = 0
        
        precedenteFourmiPos = listFourmiDroite[index-1].position_x
        if (fourmi.position_x + fourmi.taille) <= listFourmiDroite[i].position_x or (fourmi.position_x + fourmi.taille) <= listFourmiGauche[0].position_x or (fourmi.position_x + fourmi.taille) >= precedenteFourmiPos:
            fourmi.demiTour = not fourmi.demiTour
            collision +=1
        fourmi.position_x = fourmi.position_x - vitesse if not fourmi.demiTour else fourmi.position_x + vitesse

    textZone = police.render("Collisions : " + str(collision), 1, (255,255,255))

    pygame.display.update()



pygame.quit()
sys.exit()