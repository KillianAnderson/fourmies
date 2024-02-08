import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 800))
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

print(listFourmiDroite[0])

listFourmiGaucheRect = []
listFourmiDroiteRect = []




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
    rouge = 0

    for fourmi in listFourmiGauche:
        listFourmiGaucheRect.append(pygame.Rect(fourmi.position_x, fourmi.position_y, fourmi.taille, 5))
    for fourmi in listFourmiDroite:
        listFourmiDroiteRect.append(pygame.Rect(fourmi.position_x, fourmi.position_y, fourmi.taille, 5))

    for fourmi in listFourmiGaucheRect:
        pygame.draw.rect(screen, (220,20,20), fourmi)

    for fourmi in listFourmiDroiteRect:
        pygame.draw.rect(screen, (20,20,220), fourmi)
    
    print(listFourmiDroiteRect[0])

    # for index, fourmi in enumerate(listFourmiGauche):
    #     precedenteFourmiPos = listFourmiGauche[index-1].position_x
    #     if index < (len(listFourmiGauche)-1):
    #         i = index+1
    #         if (fourmi.position_x + fourmi.taille) >= listFourmiGauche[i].position_x or (fourmi.position_x + fourmi.taille) >= listFourmiDroite[6].position_x or fourmi.position_x <= (precedenteFourmiPos + fourmi.taille) :
    #             if (index > 1):
    #                 fourmi.demiTour = not fourmi.demiTour
    #                 collision +=1

    #     fourmi.position_x = fourmi.position_x + vitesse if not fourmi.demiTour else fourmi.position_x - vitesse
       

    # for index, fourmi in enumerate(listFourmiDroite):
    #     precedenteFourmiPos = listFourmiDroite[index-1].position_x
    #     if index < (len(listFourmiDroite)-1):
    #         i = index+1
    #         if (fourmi.position_x + fourmi.taille) <= listFourmiDroite[i].position_x or (fourmi.position_x + fourmi.taille) <= listFourmiGauche[14].position_x or (fourmi.position_x + fourmi.taille) >= precedenteFourmiPos:
    #             if (index > 1):
    #                 fourmi.demiTour = not fourmi.demiTour
    #                 collision +=1            
        
    #     fourmi.position_x = fourmi.position_x - vitesse if not fourmi.demiTour else fourmi.position_x + vitesse
        
    for index, fourmi in enumerate(listFourmiGaucheRect):
        if index < (len(listFourmiGaucheRect)-1):
            i = index+1
            if (fourmi.colliderect(listFourmiGaucheRect[i]) or fourmi.colliderect(listFourmiDroiteRect[6])) :
                if (index > 1):
                    listFourmiGauche[index].demiTour = not listFourmiGauche[index].demiTour
                    collision +=1

        listFourmiGauche[index].position_x = listFourmiGauche[index].position_x + vitesse if not listFourmiGauche[index].demiTour else listFourmiGauche[index].position_x - vitesse
       

    for index, fourmi in enumerate(listFourmiDroiteRect):
        if index < (len(listFourmiDroiteRect)-1):
            i = index+1
            if (fourmi.colliderect(listFourmiDroiteRect[i]) or fourmi.colliderect(listFourmiGaucheRect[14])):
                if (index > 1):
                    fourmi.demiTour = not fourmi.demiTour
                    collision +=1            
        
        listFourmiDroite[index].position_x = listFourmiDroite[index].position_x - vitesse if not listFourmiDroite[index].demiTour else listFourmiDroite[index].position_x + vitesse
    
    textZone = police.render("Collisions : " + str(collision), 1, (255,255,255))
    pygame.display.update()



pygame.quit()
sys.exit()