import sys, pygame, random, math, os
from pygame.locals import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))

player_image=pygame.image.load("画像/player.png")
rect_player=player_image.get_rect()
background_tile=pygame.image.load("画像/haikei2.png")
back_size=background_tile.get_size()
keyboard_image=pygame.image.load("画像/keyboard1.png")
arrow=pygame.image.load("画像/矢印.png")
start_menu=pygame.image.load("画像/title.png")
#変更後=================================================================
sleepiness_image0=pygame.image.load("画像/enemy0.png")
sleepiness_image1=pygame.image.load("画像/enemy1.png")
sleepiness_image2=pygame.image.load("画像/enemy2.png")

img_gauge_green = pygame.image.load("画像/体力ゲージ50-100.png")
img_gauge_green = pygame.transform.scale(img_gauge_green, (200, 20))
img_gauge_yellow = pygame.image.load("画像/体力ゲージ20-50.png")
img_gauge_yellow = pygame.transform.scale(img_gauge_yellow, (200, 20))
img_gauge_red = pygame.image.load("画像/体力ゲージ1-20.png")
img_gauge_red = pygame.transform.scale(img_gauge_red, (200, 20))
img_gameover = pygame.image.load("画像/gameover.png")
bullet_player_image=pygame.image.load("画像/bulet_player.png")

class Mob:#プレイヤー、敵の親クラス

    def __init__(self, x, y, r, hp, attack, speed, various,):
        self.x = x
        self.y = y
        self.r = r
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.various = various
    
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

class Field:
    def __init__(self):
        self.width = 1280
        self.height = 780
        self.player = Player(x=640, y=360,r=80, hp=100, attack=10, speed=4, various=0) 
        self.enemys = list()
        self.bullets = list()
        self.bullet_flag = False
    
    
    def append_b(self, x, y, dx, dy):
        self.bullets.append(Bullet(x, y, dx, dy))

    def move_player(self, key, screen,level):
        
        if key[K_a] == 1:
            self.player.x -= self.player.speed*level
            if self.player.x < 160:
                self.player.x = 160
        if key[K_d] == 1:
            self.player.x += self.player.speed*level
            if self.player.x > 1280 - 86:
                self.player.x = 1280 - 86
        if key[K_w] == 1:
            self.player.y -= self.player.speed*level
            if self.player.y < 100:
                self.player.y = 100
        if key[K_s] == 1:
            self.player.y += self.player.speed*level
            if self.player.y > 720 - 86:
                self.player.y = 720 - 86
        self.player.print_mob(screen, player_image)

        if self.bullet_flag == False:

            if key[K_r] == 1:
                self.vect_bullet(223, 181)
                self.bullet_flag = True
            elif key[K_t] == 1:
                self.vect_bullet(398, 181)
                self.bullet_flag = True
            elif key[K_y] == 1:
                self.vect_bullet(588, 181)
                self.bullet_flag = True
            elif key[K_u] == 1:
                self.vect_bullet(763, 181)
                self.bullet_flag = True
            elif key[K_i] == 1:
                self.vect_bullet(943, 181)
                self.bullet_flag = True
            elif key[K_o] == 1:
                self.vect_bullet(1128, 181)
                self.bullet_flag = True
            elif key[K_f] == 1:
                self.vect_bullet(253, 371)
                self.bullet_flag = True
            elif key[K_g] == 1:
                self.vect_bullet(438, 371)
                self.bullet_flag = True
            elif key[K_h] == 1:
                self.vect_bullet(628, 371)
                self.bullet_flag = True
            elif key[K_j] == 1:
                self.vect_bullet(808, 371)
                self.bullet_flag = True
            elif key[K_k] == 1:
                self.vect_bullet(988, 371)
                self.bullet_flag = True
            elif key[K_v] == 1:
                self.vect_bullet(303, 551)
                self.bullet_flag = True
            elif key[K_b] == 1:
                self.vect_bullet(485, 551)
                self.bullet_flag = True
            elif key[K_n] == 1:
                self.vect_bullet(668, 551)
                self.bullet_flag = True
            elif key[K_m] == 1:
                self.vect_bullet(843, 551)
                self.bullet_flag = True
            
        
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
        #変更後==============================================================
        
        enemy_choice=random.choice([0,1,1,1,2,2])
        if enemy_choice==0:
            self.enemys.append(Enemy(x, y,r=80, hp=50, attack=30, speed=1,various=0))
        elif enemy_choice==1:
            self.enemys.append(Enemy(x, y,r=60, hp=20, attack=10, speed=2.5, various=1))
        elif enemy_choice==2:
            self.enemys.append(Enemy(x, y,r=45, hp=10, attack=5, speed=4, various=2))


    def move_sleep(self, screen,level):
        pcx = self.player.x + self.player.r/2
        pcy = self.player.y + self.player.r/2
    
        for c, enemy in enumerate(self.enemys):
            ecx = enemy.x + enemy.r/2
            ecy = enemy.y + enemy.r/2
            dx = enemy.speed 
            x = pcx - ecx
            y = pcy - ecy
            leng = math.sqrt(x ** 2 + y ** 2)
            if leng < 62.5:
                self.enemys.pop(c)
                self.player.receive_damege(enemy.attack)
            if x == 0:
                x = 0.0000000001  
            if y == 0:
                y = 0.0000000001
            
            θ = math.atan(y / x)
            if x>0:
                enemy.x += math.cos(θ) * dx*level
                enemy.y += math.sin(θ) * dx*level
            else:
                enemy.x -= math.cos(θ) * dx*level
                enemy.y -= math.sin(θ) * dx*level
            touch_frag=self.touch_b_e(enemy,c)
            #変更後=====================================================================
            if enemy.various==0 and touch_frag:
                enemy.print_mob(screen, sleepiness_image0)
            elif enemy.various==1 and touch_frag:
                enemy.print_mob(screen, sleepiness_image1)
            elif enemy.various==2 and touch_frag:
                enemy.print_mob(screen, sleepiness_image2)


    def draw_hp(self, screen):
        if self.player.hp >= 50:
            screen.blit(img_gauge_green,(1040,45))  #体力ゲージ
        elif self.player.hp <= 50 and self.player.hp >20:
            screen.blit(img_gauge_yellow,(1040,45))
        elif self.player.hp <= 20:
            screen.blit(img_gauge_red,(1040,45))

        pygame.draw.rect(screen,(0,0,0),[(520+self.player.hp)*2,45,(100-self.player.hp)*2,20]) 

    def vect_bullet(self, dx, dy):
        X = dx - self.player.x
        Y = dy - self.player.y
        if X == 0:
            X = 0.0000000001  
        if Y == 0:
            Y = 0.0000000001
        
        θ = math.atan(Y / X)
        v = 5
        if X > 0:
            vx = math.cos(θ) * v
            vy = math.sin(θ) * v
        else:
            vx = -(math.cos(θ) * v)
            vy = -(math.sin(θ) * v)

        self.bullets.append(Bullet(self.player.x, self.player.y, vx, vy))

    def touch_b_e(self,enemy,c):
        for c_b, bullet in enumerate(self.bullets):
                    ecx = enemy.x + enemy.r/2
                    ecy = enemy.y + enemy.r/2
                    bcx = bullet.x + 40
                    bcy = bullet.y + 40
                    x = bcx - ecx
                    y = bcy - ecy
                    leng = math.sqrt(x ** 2 + y ** 2)
                    if leng < 62.5:
                        enemy.receive_damege(self.player.attack)
                        if enemy.hp<=0 and len(self.enemys)!=0:
                            self.enemys.pop(c)
                        self.bullets.pop(c_b)
                        return False
        return True


    def move_bullet(self, screen,level):
        for bullet in self.bullets:
            bullet.x += bullet.dx*level
            bullet.y += bullet.dy*level
               
            screen.blit(bullet_player_image,(bullet.x, bullet.y))




def time_count(time, screen):

    elapsed_minute = (time % 3600) // 60
    elapsed_second = (time % 3600 % 60)
    timer = f"{str(elapsed_minute).zfill(2)}:{str(elapsed_second).zfill(2)}"
    timer_font = pygame.font.SysFont("", 80)
    timer_text = timer_font.render(timer, True, (0,0,0))
    screen.blit(timer_text, (20,20))

def gameover(field):
    while True:
        screen = pygame.display.set_mode((1280, 720))
        screen.blit(background_tile,(0,0))
        screen.blit(keyboard_image,(160,100))
        pygame.draw.rect(screen,(0,0,0),[(520+field.player.hp)*2,45,(100-field.player.hp)*2,20])
        screen.blit(img_gameover,(0,0))

        for enemy in field.enemys:
            if enemy.various==0:
                screen.blit(sleepiness_image0, (enemy.x, enemy.y))
            if enemy.various==1:
                screen.blit(sleepiness_image1, (enemy.x, enemy.y))
            if enemy.various==2:
                screen.blit(sleepiness_image2, (enemy.x, enemy.y))


        field.player.print_mob(screen, player_image)
        font1 = pygame.font.SysFont(None, 80)
        font2 = pygame.font.SysFont(None, 50)
        text1 = font1.render("GAME OVER", True, (200,0,0))
        screen.blit(text1, (480, 150))
        text2 = font2.render("continue -c", True, (200,0,0))
        screen.blit(text2, (580, 300))
        text3 = font2.render("end -e", True, (200,0,0))
        screen.blit(text3, (610, 380))
    
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if key[K_c] == 1:
            return start()
        elif key[K_e] == 1 or key[K_ESCAPE] == 1:
            pygame.quit()
            sys.exit()
        
        pygame.display.update()
    
def level_check(cursor):
    if cursor==1:
        return 1.5
    elif cursor==0:
        return 1
    elif cursor==-1:
        return 0.75
    

            





def start():
    cursor = 0
    screen = pygame.display.set_mode((1280, 720))
    while True:
        
        screen.blit(start_menu, (0, 0))
        screen.blit(arrow, (280, 300-cursor * 120))
#なんでえええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええええ
        for event in pygame.event.get():
            #print(event)
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    if cursor<1:
                        cursor+=1
                if event.key == K_s:
                    if cursor>-1:
                        cursor-=1
          
        key = pygame.key.get_pressed()
        
        if key[K_SPACE] == 1:
            return main(cursor)
        print(cursor)
        pygame.display.update()

def main(cursor):
    level=level_check(cursor)
    count = 0
    b_count = 0
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
        if field.bullet_flag == True:
            b_count += 1
            if level == 1.5:
                if b_count % 15 == 0:
                    field.bullet_flag = False
                    b_count = 0
            else:
                if b_count % 30 == 0:
                    field.bullet_flag = False
                    b_count = 0

        if count % 60 == 0:
            time += 1
            count=0
        if count % 30 == 0:
            ttime += 1*level
            if ttime % 3 == 0:
                field.append_sleep()

        time_count(time, screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(keyboard_image,(160,100))
        key = pygame.key.get_pressed()
        if key[K_ESCAPE] == 1 or key[QUIT] == 1:
            pygame.quit()
            sys.exit()
        field.move_player(key, screen,level)
        field.move_sleep(screen,level)
        field.move_bullet(screen,level)

        if field.player.hp <= 0:  
            return gameover(field)
        
        field.draw_hp(screen)

        pygame.display.update()

if __name__ == "__main__":
    start()

"""
やること

当たり判定を関数でまとめる→プレイヤー、敵、弾のデータを変数でまとめる(クラス定義)
関数の整理
コードの整理
スコア表示、スコア保存→CSVでいけるかな
などなど
"""