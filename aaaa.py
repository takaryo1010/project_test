import sys, pygame, random, math
from pygame.locals import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
player_image=pygame.image.load("画像/player.png")
rect_player=player_image.get_rect()
background_tile=pygame.image.load("画像/haikei2.png")
back_size=background_tile.get_size()
keyboard_image=pygame.image.load("画像/keyboard1.png")
arrow=pygame.image.load("画像/矢印.png")
start_menu=pygame.image.load("画像/title.png")
sleepiness_image=pygame.image.load("画像/enemy.png")
img_gauge_green = pygame.image.load("画像/体力ゲージ50-100.png")
img_gauge_green = pygame.transform.scale(img_gauge_green, (200, 20))
img_gauge_yellow = pygame.image.load("画像/体力ゲージ20-50.png")
img_gauge_yellow = pygame.transform.scale(img_gauge_yellow, (200, 20))
img_gauge_red = pygame.image.load("画像/体力ゲージ1-20.png")
img_gauge_red = pygame.transform.scale(img_gauge_red, (200, 20))
img_gameover = pygame.image.load("画像/gameover.png")

class Mob:#プレイヤー、敵の親クラス

    def __init__(self, x, y, hp, attack):
        self.x = x
        self.y = y
        self.hp = hp
        self.attack = attack
    
    def receive_damege(self, damages):
        self.hp -= damages

    def print_mob(self, screen, img):
        screen.blit(img, [self.x, self.y])

class Enemy(Mob): #敵のクラス

    pass

class Player(Mob):#プレイヤーのクラス

    pass

class Bullet:

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class Field: #画面のクラス（画面上で起こっている事をここで管理する）
    def __init__(self):
        self.width = 1280
        self.height = 780
        self.player = Player(640, 360, 100, 100) 
        self.enemys = list()

    def move_player(self, key, screen):
        player_v = 4
        if key[K_a] == 1:
            self.player.x -= player_v
            if self.player.x < 160:
                self.player.x = 160
        if key[K_d] == 1:
            self.player.x += player_v
            if self.player.x > 1280 - 86:
                self.player.x = 1280 - 86
        if key[K_w] == 1:
            self.player.y -= player_v
            if self.player.y < 100:
                self.player.y = 100
        if key[K_s] == 1:
            self.player.y += player_v
            if self.player.y > 720 - 86:
                self.player.y = 720 - 86
        self.player.print_mob(screen, player_image)

    def append_sleep(self):

        flag = random.randint(0, 3)
        if flag == 0:#上
            x = random.randint(205,1274)
            y = 148
        elif flag == 1:#下
            x = random.randint(205,1274)
            y = 717
        elif flag == 2:#右
            x = 1274
            y = random.randint(148, 717)
        else:#左
            x = 205
            y = random.randint(148, 717)
        
        self.enemys.append(Enemy(x, y, 10, 10))

    def move_sleep(self, screen):
        pcx = self.player.x + 40
        pcy = self.player.y + 40
        count = 0
    
        for enemy in self.enemys:
            ecx = enemy.x + 22.5
            ecy = enemy.y + 22.5
            dx = 2.5
            x = pcx - ecx
            y = pcy - ecy
            leng = math.sqrt(x ** 2 + y ** 2)
            if leng < 62.5:
                self.enemys.pop(count)
                self.player.hp -= enemy.attack
                print(self.player.hp)
            if x==0:
                x=0.0000000001  
            if y==0:
                y=0.0000000001
            
            θ = math.atan(y / x)
            if x>0:
                enemy.x+=math.cos(θ)*dx
                enemy.y+=math.sin(θ)*dx
            else:
                enemy.x-=math.cos(θ)*dx
                enemy.y-=math.sin(θ)*dx
            screen.blit(sleepiness_image, (enemy.x, enemy.y))
            count += 1

    def draw_hp(self, screen):
        if self.player.hp >= 50:
            screen.blit(img_gauge_green,(1040,45))  #体力ゲージ
        elif self.player.hp <= 50 and self.player.hp >20:
            screen.blit(img_gauge_yellow,(1040,45))
        elif self.player.hp <= 20:
            screen.blit(img_gauge_red,(1040,45))

        pygame.draw.rect(screen,(0,0,0),[(520+self.player.hp)*2,45,(100-self.player.hp)*2,20]) 

def time_count(time, screen):

    elapsed_minute = (time % 3600) // 60
    elapsed_second = (time % 3600 % 60)
    timer = f"{str(elapsed_minute).zfill(2)}:{str(elapsed_second).zfill(2)}"
    timer_font = pygame.font.SysFont("", 80)                   #フォントの設定 
    timer_text = timer_font.render(timer, True, (0,0,0))
    screen.blit(timer_text, (20,20))

def gameover(field):                                    #ゲームオーバーになったとき
    while True:
        screen = pygame.display.set_mode((1280, 720))
        screen.blit(background_tile,(0,0))
        screen.blit(keyboard_image,(160,100))
        pygame.draw.rect(screen,(0,0,0),[(520+field.player.hp)*2,45,(100-field.player.hp)*2,20])
        #これから時間表示する
        screen.blit(img_gameover,(0,0))

        font1 = pygame.font.SysFont(None, 80)
        font2 = pygame.font.SysFont(None, 50)
        text1 = font1.render("GAME OVER", True, (200,0,0))
        screen.blit(text1, (480, 150))
        text2 = font2.render("continue -c", True, (200,0,0))
        screen.blit(text2, (580, 300))
        text3 = font2.render("end -e", True, (200,0,0))
        screen.blit(text3, (610, 380))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            pressed_key = pygame.key.get_pressed()
            if pressed_key[K_c]:                   
                return start()
            if pressed_key[K_e]:
                pygame.quit()
                sys.exit()

def start():
    cursor = 0
    screen = pygame.display.set_mode((1280, 720))
    while True:
        
        screen.blit(start_menu,(0,0))
        screen.blit(arrow,(280,300-cursor*120))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    if cursor<1:
                        cursor+=1
                if event.key == K_s:
                    if cursor>-1:
                        cursor-=1
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pressed_key = pygame.key.get_pressed()
            if pressed_key[K_SPACE]:
                return main()
        pygame.display.update()

def main():
    count = 0
    time = 0
    ttime = 0
    fps_clock = pygame.time.Clock()
    fps_clock.tick(60)
    field = Field()
    pygame.init() 
    screen = pygame.display.set_mode((1280, 720))

    while True:
        screen.blit(background_tile,(0,0))
        count += 1
        if count % 60 == 0:
            time += 1
            count=0
        if count % 30 == 0:
            ttime += 1
            if ttime % 3 == 0:
                field.append_sleep()

        time_count(time, screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(keyboard_image,(160,100))
        key = pygame.key.get_pressed()
        if key[K_ESCAPE] == 1:
            pygame.quit()
            sys.exit()
        field.move_player(key, screen)
        field.move_sleep(screen)

        if field.player.hp <= 0:                                        #hpが0になったら
            return gameover(field)
        
        field.draw_hp(screen)

        pygame.display.update()

if __name__ == "__main__":
    start()