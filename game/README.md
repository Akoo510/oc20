# Space Defense

## Jeu : Jeux.py
* Le jeu est comparable à un "Plant vs Zombie" / Tower Defense
  * Tuer les ennemis avant qu'ils ne dépassent une certaine ligne
  * Survire le plus longtemps possible
* Facile à prendre en main et compréhensible
* Pas de capture d'écran du jeu, car pas encore fini

## Structure du jeu
* Différentes classes pour les ennemis
* Des bruitages
* Système de déplacement du personnage principal (WS)
* Système de projectiles pour tuer les ennemis (F)
* Vitesse des ennemis et apparition aléatoire (augmente avec le temps (Work in progress))

## Classes
* Différents personnages dans le jeu :
  * Personnage Principal
  
  <img width="47" alt="Capture d’écran 2021-04-19 à 18 26 58" src="https://user-images.githubusercontent.com/77661893/115271397-98965c80-a13d-11eb-9555-9ef6220b5071.png">

Il a la possibilité de tirer des projéctiles [F] infligeant 250 dommages
De se déplacer verticalement [W], [S] (respéctivement haut et bas)
A une barre de point de vie (1000pv)

 
  * Ennemi 1 - Mecha

 ![Mecha_walk_01](https://user-images.githubusercontent.com/77661930/120357345-a1b24600-c305-11eb-975e-9cf9ee9939b8.png)
 
  Il se déplace horizontalement avec une vitesse donnée
 A une hitbox
 A une barre de point de vie (2000pv)

  * Ennemi 2 - Gunman
  
  ![Gunman_img_03](https://user-images.githubusercontent.com/77661930/120357405-b393e900-c305-11eb-816d-3a06c301371b.png)
  
  Il se déplace horizontalement avec une vitesse donnée
 A une hitbox
 A une barre de point de vie (750pv)

  * Ennemi 3 - Cyborg

 ![Cyborg_img_01](https://user-images.githubusercontent.com/77661930/120357477-c9a1a980-c305-11eb-8fbb-8f781f5ccb37.png)
 
  Il se déplace horizontalement avec une vitesse donnée
 A une hitbox
 A une barre de point de vie (1250pv)

  * Projectiles

  <img width="86" alt="Capture d’écran 2021-04-19 à 18 27 23" src="https://user-images.githubusercontent.com/77661893/115271552-c085c000-a13d-11eb-82c0-a92cf80b9ab5.png">
  
  Émettent un son lors du lancement
 Infligent 250 dommages
 Ont une vitesse donnée
 Ont une hitbox et détectent lorsqu'elle rentre en contact avec celle des ennemies

  * Schéma des classes

![Class diagram](https://user-images.githubusercontent.com/77661930/120223792-70247680-c242-11eb-88d6-adf93ba317ae.png)

  * Exemple de classe (Player)
 
 class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprites = load_images('Player_img')
        self.pv = 1000
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.i = 0
        
    def update(self):
        if frame % 10 == 0:
            self.i = (self.i + 1) % len(self.sprites)
            self.image = self.sprites[self.i]


Le jeu n'étant pas terminé, nous ne pouvons pas vous montrer les différentes classes dans le code ainsi qu'une démonstration du jeu. Cela va bientôt être mis à jour.
