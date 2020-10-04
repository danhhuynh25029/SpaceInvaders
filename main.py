import pygame
import sys
import random
pygame.font.init()
win = pygame.display.set_mode((450,600))
pygame.display.set_caption("Game air")
clock = pygame.time.Clock()
back_ground = pygame.image.load('images/bg1.jpg')
player = pygame.image.load('images/player.png')
b_image = pygame.image.load('images/bullet.png')
bot_image = pygame.image.load('images/bot.png')
ex_image = pygame.image.load('images/no.png')
class Player(object):
   def __init__(self,x,y,health,score,image,end):
      self.x = x
      self.y = y
      self.health = health
      self.score = score
      self.image = image
      self.end = end
   def Draw(self):
      win.blit(self.image,(self.x,self.y))
   def Controll(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and self.x > 0:
         self.x -= 7
      if keys[pygame.K_RIGHT] and self.x < 350:
         self.x += 7
      if keys[pygame.K_UP] and self.y > 300:
         self.y -= 7
      if keys[pygame.K_DOWN] and self.y < 500:
         self.y += 7
class Bullet(object):
   def __init__(self,x,y,image):
      self.x = x
      self.y = y
      self.image = image
      self.run = False
   def Draw(self):
      if self.run == True:
         self.y += -20
      win.blit(self.image,(self.x,self.y))
class Bot(object):
   def __init__(self,x,y,image,death,tmp):
      self.x = x
      self.y = y
      self.image = image
      self.death = death
      self.tmp = tmp
   def Draw(self):
      #self.tmp = random.randint(1,10)
      if self.death == False:
         win.blit(self.image,(self.x,self.y))
         self.y += self.tmp
class explosive(object):
   def __init__(self,x,y,image,run):
      self.x = x
      self.y = y
      self.image = image
      self.run = run
   def Draw(self):
      if self.run == True:
         win.blit(self.image,(self.x,self.y))
p = Player(170,500,100,0,player,False)      
arr_b = []
arr_bot = []
def drawScore(score):
   myfont = pygame.font.SysFont("Times New Roman,Arial", 20,True)
   scoretext = myfont.render("Score: "+str(score), 1, (225,0,0))
   win.blit(scoretext, (5, 10))
def drawGame():
   win.blit(back_ground,(0,0))
   p.Draw()
   p.Controll()
   for i in arr_bot:
      i.Draw()
      if i.x > 450 or i.x < 0:
         arr_bot.pop(arr_bot.index(i))
      if i.y > 600:
         arr_bot.pop(arr_bot.index(i))
         p.end = True
      if i.death == True:
         arr_bot.pop(arr_bot.index(i))
      if 
   if len(arr_bot) < 5:
      x = random.randint(0,350)
      tmp = random.randint(1,10)
      b = Bot(x,-100,bot_image,False,tmp)
      arr_bot.append(b)
   keys = pygame.key.get_pressed()
   if keys[pygame.K_SPACE]:
      if len(arr_b) < 30:
         a = Bullet(p.x + 29,p.y,b_image)
         arr_b.append(a)
      for i in arr_b:
         i.run = True
   for i in arr_b:
      if i.y < 0:
         i.run = False
         #print(i.y)
      for j in arr_bot:
         if i.y <= j.y + 100 and i.x <= j.x + 100 and i.x >= j.x and j.death == False and i.run == True:
            j.death = True
            i.run = False
            tmp = explosive(j.x + 30,j.y+50,ex_image,True)
            tmp.Draw()
            p.score += 1
            break
      if i.run == False:
         arr_b.pop(arr_b.index(i))
      if i.run == True:
         i.Draw()
   #print(len(arr_b))

   #print(len(arr_bot))
   #print(len(arr_b))
   drawScore(p.score)
def Pause():
   pause = False
   if p.end == True:
      pause = True
   while pause:
      for e in pygame.event.get():
         win.fill((255,255,255))
         myfont = pygame.font.SysFont("Times New Roman,Arial", 20,True)
         scoretext = myfont.render(" Your Score: "+str(p.score), 1, (0,0,0))
         alert = myfont.render("Press c to countinue",1,(0,0,0))
         win.blit(scoretext, (450//2 - 70,600//2 ))
         win.blit(alert,(450//2 - 90,450))
         pygame.display.update()
         clock.tick(5)
         if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_c:
               pause = False
               p.score = 0
               p.end = False
               arr_bot.clear()
run = True
while run:
   clock.tick(27)
   for e in pygame.event.get():
      if e.type == pygame.QUIT:
         run = False
      if e.type == pygame.K_c:
         p.end = False
         p.score = 0
         arr_bot.clear()
   drawGame()
   Pause()
   pygame.display.update()
pygame.quit()
