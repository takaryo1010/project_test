"""
やること

当たり判定を関数でまとめる→プレイヤー、敵、弾のデータを変数でまとめる(クラス定義)
関数の整理
コードの整理
スコア表示、スコア保存→CSVでいけるかな
などなど
押したところを光らせたい(キーボード部分)
"""
import sys, pygame, random, math, os
from pygame.locals import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#-----画像保管場所-----#
player_image=pygame.image.load("画像/player.png")
rect_player=player_image.get_rect()
background_tile=pygame.image.load("画像/haikei2.png")
back_size=background_tile.get_size()
keyboard_image=pygame.image.load("画像/keyboard1.png")
arrow=pygame.image.load("画像/矢印.png")
start_menu=pygame.image.load("画像/title.png")
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
img_cell=pygame.image.load("画像/cell.png")
#-----画像保管場所終わり-----#

#-----クラス定義-----#
class Mob:#プレイヤー、敵の親クラス

    def __init__(self, x, y, r, hp, attack, speed, various,):
        self.x = x
        self.y = y
        self.r = r
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.various = various
    
    def receive_damege(self, damages):#ダメージを受けた時にhpを減らす関数
        self.hp -= damages

    def print_mob(self, screen, img):#プレイヤー、敵を描画する関数（描画関数はblitで既に存在するが、コード簡略化するため）
        screen.blit(img, [self.x, self.y])

class Enemy(Mob): #敵のクラス（名前を区別するため。特に無し）

    pass

class Player(Mob):#プレイヤーのクラス（同上）

    pass

class Bullet:#弾のクラス定義

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class Field:#プレイ画面のクラス意義
    def __init__(self):
        self.width = 1280
        self.height = 780
        self.player = Player(x=640, y=360,r=80, hp=100, attack=100, speed=4, various=0) 
        self.enemys = list()#敵を格納しているリスト。今後種類を増やした時に、リストを分けるか、クラスや要素で仕分けるか...
        self.bullets = list()#弾のリスト
        self.key_flag = False
        self.bullet_flag = False#弾が発射されているかのフラッグ。連射するときのクールタイムを制御する
        self.cell_flag = False

    def move_player(self, key, screen,level):#プレイヤーの挙動を管理する関数。弾の向きも決める。
        #プレイヤーの速度
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

        x, y = 0, 0

        if key[K_r] == 1:
            x, y = 223, 181
            self.key_flag = True
        if key[K_t] == 1:
            x, y = 398, 181
            self.key_flag = True
        if key[K_y] == 1:
            x, y = 588, 181
            self.key_flag = True
        if key[K_u] == 1:
            x, y = 763, 181
            self.key_flag = True
        if key[K_i] == 1:
            x, y = 943, 181
            self.key_flag = True
        if key[K_o] == 1:
            x, y = 1128, 181
            self.key_flag = True
        if key[K_f] == 1:
            x, y = 253, 371
            self.key_flag = True
        if key[K_g] == 1:
            x, y = 438, 371
            self.key_flag = True
        if key[K_h] == 1:
            x, y = 628, 371
            self.key_flag = True
        if key[K_j] == 1:
            x, y = 808, 371
            self.key_flag = True
        if key[K_k] == 1:
            x, y = 988, 371
            self.key_flag = True
        if key[K_v] == 1:
            x, y = 303, 551
            self.key_flag = True
        if key[K_b] == 1:
            x, y = 485, 551
            self.key_flag = True
        if key[K_n] == 1:
            x, y = 668, 551
            self.key_flag = True
        if key[K_m] == 1:
            x, y = 843, 551
            self.key_flag = True
#=====================================
        if self.key_flag == True:
            if self.bullet_flag == False:
                self.vect_bullet(x, y)
                self.bullet_flag = True
            self.key_flag = False
            return x, y
#==================================
    def vect_bullet(self, dx, dy):#弾のベクトルを決める関数
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
    
    def move_bullet(self, screen,level):#弾の動きを管理する関数
        for c_b, bullet in enumerate(self.bullets):
            bullet.x += bullet.dx*level
            bullet.y += bullet.dy*level
            for c_e, enemy in enumerate(self.enemys):
                ecx = enemy.x + 22.5
                ecy = enemy.y + 22.5
                bcx = bullet.x + 40
                bcy = bullet.y + 40
                x = bcx - ecx
                y = bcy - ecy
                leng = math.sqrt(x ** 2 + y ** 2)
                if leng < 62.5:
                    self.enemys.pop(c_e)
                    self.bullets.pop(c_b)
            
            screen.blit(bullet_player_image,(bullet.x, bullet.y))

    def append_sleep(self):#敵をリストに追加する関数

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
        
        enemy_choice=random.randint(0,2)
        if enemy_choice==0:
            self.enemys.append(Enemy(x, y,r=45, hp=100, attack=50, speed=1,various=0))
        elif enemy_choice==1:
            self.enemys.append(Enemy(x, y,r=45, hp=10, attack=10, speed=2.5, various=1))
        elif enemy_choice==2:
            self.enemys.append(Enemy(x, y,r=45, hp=10, attack=5, speed=4, various=2))



    def move_sleep(self, screen,level):#敵の動きを管理する関数
        pcx = self.player.x + 40
        pcy = self.player.y + 40
    
        for c, enemy in enumerate(self.enemys):
            ecx = enemy.x + 22.5
            ecy = enemy.y + 22.5
            dx = 2.5
            x = pcx - ecx
            y = pcy - ecy
            leng = math.sqrt(x ** 2 + y ** 2)
            if leng < 62.5:
                self.enemys.pop(c)
                self.player.hp -= enemy.attack
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
            if enemy.various==0:
                enemy.print_mob(screen, sleepiness_image0)
            elif enemy.various==1:
                enemy.print_mob(screen, sleepiness_image1)
            elif enemy.various==2:
                enemy.print_mob(screen, sleepiness_image2)

    def draw_hp(self, screen):#プレイヤーのhpを描画する関数
        if self.player.hp >= 50:
            screen.blit(img_gauge_green,(1040,45))
        elif self.player.hp <= 50 and self.player.hp >20:
            screen.blit(img_gauge_yellow,(1040,45))
        elif self.player.hp <= 20:
            screen.blit(img_gauge_red,(1040,45))

        pygame.draw.rect(screen,(0,0,0),[(520+self.player.hp)*2,45,(100-self.player.hp)*2,20]) 

#-----クラス定義終わり-----#

#-----関数定義-----#

def time_count(time, screen):#タイマーを描画する関数

    elapsed_minute = (time % 3600) // 60
    elapsed_second = (time % 3600 % 60)
    timer = f"{str(elapsed_minute).zfill(2)}:{str(elapsed_second).zfill(2)}"
    timer_font = pygame.font.SysFont("", 80)
    timer_text = timer_font.render(timer, True, (0,0,0))
    screen.blit(timer_text, (20,20))

def gameover(field):#ゲームオーバー画面の関数
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

def start():#スタート画面の関数
    cursor = 0
    screen = pygame.display.set_mode((1280, 720))
    while True:
        
        screen.blit(start_menu, (0, 0))
        screen.blit(arrow, (280, 300-cursor * 120))

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
        
        pygame.display.update()

def main(cursor):#ゲームプレイ中の関数
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
            ttime += 1 * level
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
        field.move_player(key, screen, level)
        field.move_sleep(screen, level)
        field.move_bullet(screen, level)
        #=================================================
        if field.bullet_flag == True:
            if field.key_flag == True:
                x, y = field.move_player(key, screen, level)
                screen.blit(img_cell,(x,y))
        #====================================================
        

        if field.player.hp <= 0:  
            return gameover(field)
        
        field.draw_hp(screen)

        pygame.display.update()

#-----関数定義終わり-----#

if __name__ == "__main__":
    start()