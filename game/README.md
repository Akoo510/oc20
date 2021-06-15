# Space Defense

# Jeu : Jeux.py
* Le jeu est comparable à un "Plant vs Zombie" / Tower Defense
  * Tuer les ennemis avant qu'ils ne dépassent une certaine ligne
  * Survire le plus longtemps possible
* Facile à prendre en main et compréhensible
* Pas de capture d'écran du jeu, car pas encore fin

# Structure du jeu
* Différentes classes pour le jeu
* Des bruitages
* Système de déplacement du personnage principal (WS)
* Système de projectiles pour tuer les ennemis (F)
* Vitesse des ennemis et apparition aléatoire (augmente avec le temps)

# Classes
## Text 
* Crée un objet texte
* Dessine le texte au dessus de l'objet
* Traite le texte comme une image

## AnimatedSprite
* Crée une animation d'image
* Contient :
  * des images
  * des dossiers
  * rectangle de l'image
  * vitesse de l'image
  * texte attaché à l'image

## Player
* Crée un joueur avec :
  * 1000 point de vie
  * mouvement vertical (réaction au touches W/S UP/DOWN)
  * réaction au projectiles (tire avec la touche F)
  * fait des dégats au ennemis (250 points de vie)

## Enemy
* Crée un ennemi avec :
  * apparition à droite (aléatoire sur les 3 lignes)
  * mouvement vers la gauche
  * fait des dégats au joueur (100 points de vie en franchissant la bordure gauche)
  * revient à son point de départ lorsqu'il meurt/passe la bordure
  * une hitbox 
  * lorsqu'il meurt, il fait gagner 100 points de score au joueur

## Projectiles
* Crée un projectile avec :
  * mouvement latéral vers la droite
  * réagit avec la hitbox des ennemis
  * se fait détruire après collision avec la hitbox des ennemis
  * inflige 250 points de dégats
  * disparait lorsqu'il dépasse la bordure droite
  * un son lorsqu'il est lancé

## Game
* Va lancer le jeu
* Contient toutes les données importantes concernant le lancement du jeu et le déroulement de ce dernier
* Contient la boucle while
* Dessine les ennemis et le joueur
* Dessine le texte sur les ennemis, le joueur, score, etc.
* Possède un écran d'accueil et un écran de game over
* joue de la musique aléatoirement
* fait apparaître de plus en plus d'ennemi tous les 1000 points de scores

## Schéma des classes


 ## Exemple de classe (Player)
 
        class Player(AnimatedSprite):
            def __init__(self, folder, pv=1000):
               super().__init__(folder, pv)
               self.lane = 1
               self.player_pos = [130, 285, 420]
               self.rect.x = 50 
               self.rect.y = self.player_pos[1]
               self.pv = pv

            def keydown(self, event):
              """The player knows how to react to keys."""
               if event.key == K_w or event.key == K_UP:
                   if self.lane == 1 or self.lane == 0: 
                       self.rect.move_ip(0, -140)
                       self.lane +=1

               elif event.key == K_s or event.key == K_DOWN:
                   if self.lane == 1 or self.lane == 2:
                       self.rect.move_ip(0, 140)
                       self.lane -=1

               elif event.key == K_f:
                   Bullet.fire_sound.play()
                   Bullet.bullets.add(Bullet(self.rect.center))

WIP
