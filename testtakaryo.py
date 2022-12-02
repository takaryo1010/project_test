from distutils.util import subst_vars
import sys
from this import d
from turtle import back
import pygame
from pygame.locals import *
from dataclasses import *
import random
import os
import math
import copy
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#------------変数--------------------------------------------------------------

dx=0
dy=0
fps_clock = pygame.time.Clock()
screen_size=[1280, 720]
player=0
amplitude_value=0
count_mid=0
map_random=[1280/2,720/2]
count_mid2=0


#------------クラス------------------------------------------------------------

@dataclass
class Player:                               #プレイヤーについてのステータス
    name:str
    hp:int
    power:int
    speed:int

    def draw_player():#プレイヤーを表示をする
        pass#←書き始める時にpass消す


    def receive_damage(self,atack_damages):
        self.hp=self.hp-atack_damages
    #変更後============================================
    def shooting_player(self,x,y):
        if len(grapher.shoot_player_data)<5:
            center_x=int(x-rect_player[0])
            center_y=int(y-rect_player[1])
            
            if center_x==0:
                center_x=0.0000000001  
            elif center_y==0:
                center_y=0.0000000001
            θ=math.atan(center_y/center_x)
            if center_x>0:
                    dx=(math.cos(θ)*5)
                    dy=(math.sin(θ)*5)
                    
            if center_x<0:
                    dx=-(math.cos(θ)*5)
                    dy=-(math.sin(θ)*5)
            grapher.shoot_player_data.append(shooting_player(dx*3,dy*3,copy.deepcopy(rect_player)))
#変更後＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
@dataclass    
class shooting_player:
    dx :int
    dy :int
    rect:tuple

@dataclass
class Sleepiness:                           #睡魔についてのステータス
    x:int
    y:int
    hp:int
    power:int
    speed:int
@dataclass    
class shooting_midtest:
    dx :int
    dy :int
    rect:tuple   
@dataclass
class Midtest:                                 #課題(敵)についてのステータス
    name:str
    hp: int
    def draw_midtest(self,time,screen):
        global count_mid,map_random,count_mid2
        count_mid+=1
        count_mid2+=1
        
        if count_mid ==101:
            map_random.clear()
            map_random.append(random.randint(0,1280-200))
            map_random.append(random.randint(0,720-200))
            count_mid=0
       
        if time>=3 and self.hp>=0 and count_mid2<300:            
            rect_mid.move_ip(0,1)
        elif time>=3 and self.hp>=0:
            center_x=int(map_random[0]-rect_mid[0])
            center_y=int(map_random[1]-rect_mid[1])
            if center_x==0:
                center_x=0.0000000001  
            elif center_y==0:
                center_y=0.0000000001
            θ=math.atan(center_y/center_x)

            
            if center_x>0:
                x=math.cos(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value))
                y=math.sin(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value))
                rect_mid.move_ip(x,y)
            if center_x<0:
                x=math.cos(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value))
                y=math.sin(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value))
                rect_mid.move_ip(-x,-y) 
    def shoot_midtest(self):
        global shoot_midtest_data
        if count_mid==100:
            a=1
            for i in range(a):
                center_x=int(rect_mid[0]-rect_player[0])
                center_y=int(rect_mid[1]-rect_player[1])
                
                if center_x==0:
                    center_x=0.0000000001  
                elif center_y==0:
                    center_y=0.0000000001
                θ=math.atan(center_y/center_x)
                if center_x>0:
                        x=-(math.cos(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value)))
                        y=-(math.sin(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value)))
                        
                if center_x<0:
                        x=(math.cos(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value)))
                        y=(math.sin(θ)*3+18**(-2.1*math.radians(amplitude_value))*math.cos(5*math.radians(amplitude_value)))
                grapher.shoot_midtest_data.append(shooting_midtest(x*3,y*3,copy.deepcopy(rect_mid)))


midtest=Midtest("中間テスト",1000)

@dataclass
class Grapher():
    list_sleepiness:list
    shoot_midtest_data:list
    shoot_player_data:list
    def __init__(self) -> None:
        self.list_sleepiness=[]
        self.shoot_midtest_data=[]
        self.shoot_player_data=[]
    def append_sleepiness(self,count,value_by_level,screen,screen_size):
        if 59==count:
            print(screen_size[0])
            map1=random.randint(-100,0)
            map2=random.randint(-100,int(screen_size[1]+100))
            map3=random.randint(screen_size[0],int(screen_size[0]+100))
            map4=random.randint(-100,int(screen_size[1]+100))
            map5=random.randint(-100,int(screen_size[0]+100))
            map6=random.randint(-100,0)
            map7=random.randint(-100,int(screen_size[0]+100))
            map8=random.randint(screen_size[1],screen_size[1]+100)

            map=[[map1,map2],[map3,map4],[map5,map6],[map7,map8]]
            map_choiced=random.choice(map)
            x=map_choiced[0]
            y=map_choiced[1]
            self.list_sleepiness.append(Sleepiness(x,y,int(value_by_level/60),int(value_by_level/30),random.randint(1,3)))
            
           
        for i in self.list_sleepiness:
            screen.blit(sleepiness_image,(i.x,i.y))





    def move_sleepiness(self,screen_size):
        global dx,dy,rect_player
        
        count=-1
        
        for i in self.list_sleepiness:
            count+=1
            center_x=int((rect_player[0]+120)-(i.x+67.5))
            center_y=int((rect_player[1]+120)-(i.y+67.5))
            
            r=((center_x**2)+(center_y**2))**(1/2)
            if r<62.5:
                
                self.list_sleepiness.pop(int(count))
                player.hp-=i.power
                
                print(player.hp)
                continue
            elif center_x==0:
                center_x=0.0000000001  
            elif center_y==0:
                center_y=0.0000000001
            

            θ=math.atan(center_y/center_x)
            r=(((center_y)**2)+((center_x)**2))**(1/2)
            if center_x>0:
                i.x+=math.cos(θ)*i.speed
                i.y+=math.sin(θ)*i.speed
            if center_x<0:
                i.x-=math.cos(θ)*i.speed
                i.y-=math.sin(θ)*i.speed

    #変更後============================================
    def draw_bulet_player(self,screen):
        for u,i in enumerate(self.shoot_player_data):
            for c,a in enumerate(self.list_sleepiness):
                center_x=int(a.x-i.rect[0])
                center_y=int(a.y-i.rect[1])
                if -60<=center_x<=0 and -60<=center_y<=0:
                    self.shoot_player_data.pop(u)
                    self.list_sleepiness.pop(c)
                
        for u,i in enumerate(self.shoot_player_data):
            i.rect.move_ip(i.dx,i.dy)
            if i.rect[0] >=1280 or i.rect[0]<=0 or i.rect[1]<=0 or i.rect[1]>=720:
                self.shoot_player_data.pop(u)
        for i in self.shoot_player_data:
            screen.blit(bulet_player_image,(i.rect))  

    def draw_bulet_Midtest(self,screen):
        for u,i in enumerate(self.shoot_midtest_data):
            
            center_x=int(rect_player[0]-i.rect[0])
            center_y=int(rect_player[1]-i.rect[1])
            if -60<=center_x<=0 and -60<=center_y<=0:
                player.hp-=3
                self.shoot_midtest_data.pop(u)
                
        for u,i in enumerate(self.shoot_midtest_data):
            i.rect.move_ip(i.dx,i.dy)
            
            if i.rect[0] >=1280 or i.rect[0]<=0 or i.rect[1]<=0 or i.rect[1]>=720:
                self.shoot_midtest_data.pop(u)

        for i in self.shoot_midtest_data:
            screen.blit(bulet_midtest_image,(i.rect))      


            

#------------関数---------------------------------------------------------------

def start():
    global player
    cursor=0
    while True:
        screen = pygame.display.set_mode((1280, 720))
        screen.fill((0,0,0))
        screen.blit(start_menu,(0,0))
        screen.blit(arrow,(280,300-cursor*120))#カーソルの位置設定
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
                    print(cursor)
                if event.key == K_s:
                    if cursor>-1:
                        cursor-=1
                    print(cursor)
            pressed_key = pygame.key.get_pressed()
        
            if pressed_key[K_SPACE]:
            #------------------------初期化欄-------------------------------------
                rect_player.center=(screen_size[0]/2,screen_size[1]/2)
                grapher.list_sleepiness.clear()


                player=decide_player()#テスト用プレイヤー宣言
                return main()                 # SPACEボタンが押されたらループ解除
            #----------------------------------------------------------------------
        pygame.display.update() 
        
def decide_player():
        
        return Player("sample",3,5,5)

def draw_field(screen,back_size):#画像読み込みのテスト
    screen.blit(background_tile,(0,0))

def move_player(player):
    global dx,dy,rect_player
    for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき 
            pressed_key = pygame.key.get_pressed()
            if pressed_key[K_a]:#移動系
                #dx+=player.speed  
                rect_player.move_ip(-player.speed,0)
            if pressed_key[K_d]:#移動系
                rect_player.move_ip(player.speed,0)
                #dx-=player.speed
            if pressed_key[K_w]:#移動系
                rect_player.move_ip(0,-player.speed)
                #dy+=player.speed
            if pressed_key[K_s]:#移動系
                rect_player.move_ip(0,player.speed)
                #dy-=player.speed
        #変更後＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
            if event.type == KEYDOWN:  # キーを押したとき
            # ESCキーならスクリプトを終了
                if event.key == K_SPACE:
                    #player.shooting_player(640,360)
                    print(rect_player)
                if event.key==K_r:
                    player.shooting_player(223,181)
                    print(grapher.shoot_player_data)
                if event.key==K_t:
                    player.shooting_player(398,181)
                if event.key==K_y:
                    player.shooting_player(588,181)
                if event.key==K_u:
                    player.shooting_player(763,181)
                if event.key==K_i:
                    player.shooting_player(943,181)
                if event.key==K_o:
                    player.shooting_player(1128,181)
                if event.key==K_f:
                    player.shooting_player(253,371)
                if event.key==K_g:
                    player.shooting_player(438,371)
                if event.key==K_h:
                    player.shooting_player(628,371)
                if event.key==K_j:
                    player.shooting_player(808,371)
                if event.key==K_k:
                    player.shooting_player(988,371)
                if event.key==K_v:
                    player.shooting_player(303,551)
                if event.key==K_b:
                    player.shooting_player(485,551)
                if event.key==K_n:
                    player.shooting_player(668,551)
                if event.key==K_m:
                    player.shooting_player(843,551)
                
#-------------------------------------------------------------------------------
#-----------画像----------------------------------------------------------------
player_image=pygame.image.load("画像/player.png")
rect_player=player_image.get_rect()
rect_player.center=(screen_size[0]/2,screen_size[1]/2)
background_tile=pygame.image.load("画像/Background_tile.jpg")
back_size=background_tile.get_size()
keyboard_image=pygame.image.load("画像/keyboard1.png")
#================--変更==========================
midtest_image=pygame.image.load("画像/midtest.jpg")
rect_mid=midtest_image.get_rect()
rect_mid.center=(screen_size[0]/2-200,-200)
bulet_midtest_image=pygame.image.load("画像/bulet_midtest.jpg")

#==============================================================

bulet_player_image=pygame.image.load("画像/bulet_player.png")
arrow=pygame.image.load("画像/矢印.png")
start_menu=pygame.image.load("画像/title.png")
sleepiness_image=pygame.image.load("画像/enemy.png")



#-------------------------------------------------------------------------------
#---------test(消してもいいよ)---------------------------------------------------
def test1(): #playerのステータス変動テスト
    res=input()
    player=decide_player(res)
    print(player)
    a=input()
    player.receive_damage(10)
    print(player)
               
#-------------------------------------------------------------------------------
grapher=Grapher()
def main():                       #メイン:ゲームの動き全般はここ
    roop=1
    count = 0
    time = 0#fukuda
    
    global dx,dy,screen_size  
    pygame.init()                                               # Pygameの初期化
    
    screen = pygame.display.set_mode()                # 大きさ1280*720の画面を生成
    value_by_level=60
    
    while roop==1:
        
        count += 1
        move_player(player)
        draw_field(screen,back_size)
        screen.blit(keyboard_image,(160,100))
        screen.blit(player_image,rect_player.center)
        screen.blit(midtest_image,rect_mid.center)
        #test ----------------------------
        grapher.append_sleepiness(count,value_by_level,screen,screen_size)
        grapher.move_sleepiness(screen_size)
        #---------------------------------
        #イベント処理(基本関数以外のもの)----
        fps_clock.tick(60)
        #-------------------------------------------------------------------------
        midtest.draw_midtest(time,screen)
        midtest.shoot_midtest()
        grapher.draw_bulet_Midtest(screen)
        grapher.draw_bulet_player(screen)
        #---------------------------------
        #イベント処理(基本関数以外のもの)----
        #-----------------------------------------------------------------------
        #経過時間表示(越智編集)
        fps_clock.tick(60)
        
        if count % 60 == 0:
            time += 1
            count=0
            
        elapsed_minute = (time % 3600) // 60
        elapsed_second = (time % 3600 % 60)
        timer = f"{str(elapsed_minute).zfill(2)}:{str(elapsed_second).zfill(2)}"

        timer_font = pygame.font.SysFont("", 80)                   #フォントの設定 
        timer_text = timer_font.render(timer, True, (0,0,0))       #テキストの設定
        screen.blit(timer_text, (20,20))                         #スクリーンに表示
        
        #-----------------------------------------------------------------------
        #-------------------------加えたよ---------------------------------------
        if player.hp <= 0:                                        #hpが0になったら
            return gameover()
        #-----------------------------------------------------------------------
        

        pygame.display.update()  # 画面を更新
        
        screen=pygame.display.set_mode((1280,720))
        
#---------------------------加えたよ--------------------------------------------
def gameover():                                    #ゲームオーバーになったとき
    
    while True:
        screen = pygame.display.set_mode((1280, 720))
        screen.fill((0,0,0))
        #screen.blit(start_menu,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            #print(event)
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                
                pygame.quit()
                sys.exit()
            """
            if event.type == KEYDOWN:
                if event.key == K_w:
                    if cursor<1:
                        cursor+=1
                    print(cursor)
                if event.key == K_s:
                    if cursor>-1:
                        cursor-=1
                    print(cursor)
            """
            pressed_key = pygame.key.get_pressed()
        
            if pressed_key[K_e]:                   
                
                return start()                      #スタート画面へ
#-----------------------------------------------------------------          

if __name__ == "__main__":
    start=start()#簡単:-1 普通:0　難しい:1
    print(start)
#main()消したよ