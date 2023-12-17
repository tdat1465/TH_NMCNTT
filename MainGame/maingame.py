import pygame, sys, time, random, os
import tkinter as tk
import tkinter.messagebox as messagebox
from email.message import EmailMessage
import smtplib
from pygame.locals import *
from tkinter import *
from PIL import ImageTk,Image

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(10)
FPS = 60
fpsClock = pygame.time.Clock()

#Cửa sổ games
screen_size=(1280,720)

#Thêm background
bg=pygame.transform.scale(pygame.image.load(r'MainGame\Image\background.jpg'),screen_size)
road=pygame.transform.scale(pygame.image.load(r'MainGame\Image\road.jpg'),(1280,400))
start_road=pygame.transform.scale(pygame.image.load(r'MainGame\Image\start_road.jpg'),(1280,400))
finish_road=pygame.transform.scale(pygame.image.load(r'MainGame\Image\finish_road.jpg'),(1280,400))
end_bg=1000
start_bg=200

#Load ảnh nút
back_ms_bt_img=pygame.image.load(r'MainGame\Image\back_ms_bt.jpg')
next_ms_bt_img=pygame.image.load(r'MainGame\Image\next_ms_bt.jpg')
play_bt_img=pygame.image.load(r'MainGame\Image\start_bt.jpg')
dis_ms_bt_img=pygame.image.load(r'MainGame\Image\disable_ms_bt.jpg')
en_ms_bt_img=pygame.image.load(r'MainGame\Image\enable_ms_bt.jpg')
help_bt_img=pygame.image.load(r'MainGame\Image\help_bt.jpg')
profile_bt_img=pygame.image.load(r'MainGame\Image\profile_bt.jpg')
save_bt_img=pygame.image.load(r'MainGame\Image\save_bt.jpg')
shop_bt_img=pygame.image.load(r'MainGame\Image\shop_bt.jpg')
return_bt_img=pygame.image.load(r'MainGame\Image\back_bt.jpg')
minigame_bt_img=pygame.image.load(r'MainGame\Image\minigame_bt.jpg')

#Maps
map1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\bg1.jpg'),(1280,720))
map2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\bg2.jpg'),(1280,720))
map3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\bg3.jpg'),(1280,720))
map4=pygame.transform.scale(pygame.image.load(r'MainGame\Image\bg4.jpg'),(1280,720))
map5=pygame.transform.scale(pygame.image.load(r'MainGame\Image\bg5.jpg'),(1280,720))
pick_map1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\pick_bg1.jpg'),(400,300))
pick_map2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\pick_bg2.jpg'),(400,300))
pick_map3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\pick_bg3.jpg'),(400,300))
pick_map4=pygame.transform.scale(pygame.image.load(r'MainGame\Image\pick_bg4.jpg'),(400,300))
pick_map5=pygame.transform.scale(pygame.image.load(r'MainGame\Image\pick_bg5.jpg'),(400,300))
maps=[map1,map2,map3,map4,map5]
pick_maps=[pick_map1,pick_map2,pick_map3,pick_map4,pick_map5]

#Load ảnh xe
car_pic2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\car.jpg'),(150,150))
car_pic1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\car.jpg'),(150,150))
item_pic=pygame.image.load(r'MainGame\Image\item.jpg')



cars0_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars0_0.jpg'),(150,150))
cars0_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars0_1.jpg'),(150,150))
cars0_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars0_2.jpg'),(150,150))
cars0_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars0_3.jpg'),(150,150))
cars0=[cars0_0,cars0_1,cars0_2,cars0_3]

cars1_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars1_0.jpg'),(150,150))
cars1_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars1_1.jpg'),(150,150))
cars1_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars1_2.jpg'),(150,150))
cars1_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars1_3.jpg'),(150,150))
cars1=[cars1_0,cars1_1,cars1_2,cars1_3]

cars2_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars2_0.jpg'),(150,150))
cars2_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars2_1.jpg'),(150,150))
cars2_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars2_2.jpg'),(150,150))
cars2_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars2_2.jpg'),(150,150))
cars2=[cars2_0,cars2_1,cars2_2,cars2_3]

cars3_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars3_0.jpg'),(150,150))
cars3_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars3_1.jpg'),(150,150))
cars3_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars3_2.jpg'),(150,150))
cars3_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars3_3.jpg'),(150,150))
cars3=[cars3_0,cars3_1,cars3_2,cars3_3]

cars4_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars4_0.jpg'),(150,150))
cars4_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars4_1.jpg'),(150,150))
cars4_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars4_2.jpg'),(150,150))
cars4_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars4_3.jpg'),(150,150))
cars4=[cars4_0,cars4_1,cars4_2,cars4_3]

cars5_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars5_0.jpg'),(150,150))
cars5_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars5_1.jpg'),(150,150))
cars5_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars5_2.jpg'),(150,150))
cars5_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars5_3.jpg'),(150,150))
cars5=[cars5_0,cars5_1,cars5_2,cars5_3]

cars6_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars6_0.jpg'),(150,150))
cars6_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars6_1.jpg'),(150,150))
cars6_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars6_2.jpg'),(150,150))
cars6_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars6_3.jpg'),(150,150))
cars6=[cars6_0,cars6_1,cars6_2,cars6_3]

cars7_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars7_0.jpg'),(150,150))
cars7_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars7_1.jpg'),(150,150))
cars7_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars7_2.jpg'),(150,150))
cars7_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars7_3.jpg'),(150,150))
cars7=[cars7_0,cars7_1,cars7_2,cars7_3]

cars8_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars8_0.jpg'),(150,150))
cars8_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars8_1.jpg'),(150,150))
cars8_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars8_2.jpg'),(150,150))
cars8_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars8_3.jpg'),(150,150))
cars8=[cars8_0,cars8_1,cars8_2,cars8_3]

cars9_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars9_0.jpg'),(150,150))
cars9_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars9_1.jpg'),(150,150))
cars9_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars9_2.jpg'),(150,150))
cars9_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars9_3.jpg'),(150,150))
cars9=[cars9_0,cars9_1,cars9_2,cars9_3]

cars10_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars10_0.jpg'),(150,150))
cars10_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars10_1.jpg'),(150,150))
cars10_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars10_2.jpg'),(150,150))
cars10_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars10_3.jpg'),(150,150))
cars10=[cars10_0,cars10_1,cars10_2,cars10_3]

cars11_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars11_0.jpg'),(150,150))
cars11_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars11_1.jpg'),(150,150))
cars11_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars11_2.jpg'),(150,150))
cars11_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars11_3.jpg'),(150,150))
cars11=[cars11_0,cars11_1,cars11_2,cars11_3]

cars12_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars12_0.jpg'),(150,150))
cars12_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars12_1.jpg'),(150,150))
cars12_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars12_2.jpg'),(150,150))
cars12_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars12_3.jpg'),(150,150))
cars12=[cars12_0,cars12_1,cars12_2,cars12_3]

cars13_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars13_0.jpg'),(150,150))
cars13_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars13_1.jpg'),(150,150))
cars13_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars13_2.jpg'),(150,150))
cars13_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars13_3.jpg'),(150,150))
cars13=[cars13_0,cars13_1,cars13_2,cars13_3]

cars14_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars14_0.jpg'),(150,150))
cars14_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars14_1.jpg'),(150,150))
cars14_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars14_2.jpg'),(150,150))
cars14_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars14_3.jpg'),(150,150))
cars14=[cars14_0,cars14_1,cars14_2,cars14_3]

cars15_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars15_0.jpg'),(150,150))
cars15_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars15_1.jpg'),(150,150))
cars15_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars15_2.jpg'),(150,150))
cars15_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars15_3.jpg'),(150,150))
cars15=[cars15_0,cars15_1,cars15_2,cars15_3]

cars16_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars16_0.jpg'),(150,150))
cars16_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars16_1.jpg'),(150,150))
cars16_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars16_2.jpg'),(150,150))
cars16_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars16_3.jpg'),(150,150))
cars16=[cars16_0,cars16_1,cars16_2,cars16_3]

cars17_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars17_0.jpg'),(150,150))
cars17_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars17_1.jpg'),(150,150))
cars17_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars17_2.jpg'),(150,150))
cars17_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars17_3.jpg'),(150,150))
cars17=[cars17_0,cars17_1,cars17_2,cars17_3]

cars18_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars18_0.jpg'),(150,150))
cars18_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars18_1.jpg'),(150,150))
cars18_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars18_2.jpg'),(150,150))
cars18_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars18_3.jpg'),(150,150))
cars18=[cars18_0,cars18_1,cars18_2,cars18_3]

cars19_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars19_0.jpg'),(150,150))
cars19_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars19_1.jpg'),(150,150))
cars19_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars19_2.jpg'),(150,150))
cars19_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars19_3.jpg'),(150,150))
cars19=[cars19_0,cars19_1,cars19_2,cars19_3]

cars20_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars20_0.jpg'),(150,150))
cars20_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars20_1.jpg'),(150,150))
cars20_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars20_2.jpg'),(150,150))
cars20_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars20_3.jpg'),(150,150))
cars20=[cars20_0,cars20_1,cars20_2,cars20_3]

cars21_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars21_0.jpg'),(150,150))
cars21_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars21_1.jpg'),(150,150))
cars21_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars21_2.jpg'),(150,150))
cars21_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars21_3.jpg'),(150,150))
cars21=[cars21_0,cars21_1,cars21_2,cars21_3]

cars22_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars22_0.jpg'),(150,150))
cars22_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars22_1.jpg'),(150,150))
cars22_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars22_2.jpg'),(150,150))
cars22_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars22_3.jpg'),(150,150))
cars22=[cars22_0,cars22_1,cars22_2,cars22_3]

cars23_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars23_0.jpg'),(150,150))
cars23_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars23_1.jpg'),(150,150))
cars23_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars23_2.jpg'),(150,150))
cars23_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars23_3.jpg'),(150,150))
cars23=[cars23_0,cars23_1,cars23_2,cars23_3]

cars24_0=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars24_0.jpg'),(150,150))
cars24_1=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars24_1.jpg'),(150,150))
cars24_2=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars24_2.jpg'),(150,150))
cars24_3=pygame.transform.scale(pygame.image.load(r'MainGame\Image\Cars\cars24_3.jpg'),(150,150))
cars24=[cars24_0,cars24_1,cars24_2,cars24_3]

cars_img=[cars0,cars1,cars2,cars3,cars4,cars5,cars6,cars7,cars8,cars9,cars10,cars11,cars12,cars13,cars14,cars15,cars16,cars17,cars18,cars19,cars20,cars21,cars22,cars23,cars23]

#Ảnh nút
start_bt_img=pygame.image.load(r'MainGame\Image\start_bt.jpg')
buff_start_img=pygame.image.load(r'MainGame\Image\startbuff.jpg')
buff_start_ed_img=pygame.image.load(r'MainGame\Image\start_buff.jpg')
buff_gold_img=pygame.image.load(r'MainGame\Image\goldbuff.jpg')
buff_gold_ed_img=pygame.image.load(r'MainGame\Image\gold_buff.jpg')
guide_img=pygame.transform.scale(pygame.image.load(r'MainGame\Image\guide.png'),(720,720))

#Thêm âm thanh
flash_sound=pygame.mixer.Sound(r'MainGame\Sound\Effect\flash.mp3')
back_sound=pygame.mixer.Sound(r'MainGame\Sound\Effect\back.mp3')
tele_sound=pygame.mixer.Sound(r'MainGame\Sound\Effect\teleport.mp3')
car_sound=pygame.mixer.Sound(r'MainGame\Sound\Effect\car_sound.mp3')

#Màu
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
#Tham số
current_money=20000
#Set font
font = pygame.font.SysFont("Consolas", 50, bold=True, italic=False)
new_font = pygame.font.SysFont("Consolas", 30, bold=True, italic=False)
ms_font=pygame.font.SysFont("Consolas", 20, bold=True, italic=False)
name_font=pygame.font.SysFont("Consolas", 30, bold=False, italic=False)
history_font=pygame.font.SysFont("Consolas", 20, bold=False, italic=False)
time_font=pygame.font.SysFont("Consolas", 200, bold=False, italic=False)
#Hàm
#Vẽ chữ
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    surface.blit(text_obj, text_rect)      
def screen_resize(new_screen_size):
    screen = pygame.display.set_mode(new_screen_size,pygame.RESIZABLE)  
#Class
class User():
    def __init__(self,username):
        self.money = current_money
        self.htr_in = 1
        self.hrt = ''
        self.username=username
        #Tạo đường dẫn
        self.path='MainGame/'+self.username+'_history'
        if os.path.exists(self.path) == False:
            os.mkdir(self.path)
        self.file_list = os.listdir(self.path)
    def create_player_history(self):#tạo một lần duy nhất cho 1 user
        if os.path.exists(self.path) == False:
            os.mkdir(self.path)
    def history_saved(self,screen):
        self.image_file = self.path + '/history'+str(self.htr_in)+'.png'
        pygame.image.save(screen,self.image_file)
        self.htr_in +=1
    def get_file_name(self,index):
        name = ''
        if index < len(self.file_list):
            name = self.file_list[index][:-4]
        return name
    def money_update(self,player,buff_gold):
        if player.rank == 1:
            if buff_gold:
                self.money += 10000
            else:
                self.money += 5000
        if player.rank == 2:
            if buff_gold:
                self.money += 2000
            else:
                self.money += 1000
        else:
            if buff_gold:
                self.money-=4000
            else:
                self.money -= 2000
    def money_change(self,dif):
        self.money+=dif
class Car():
    name=''
    color=(0,0,0)
    def __init__(self,screen,skill,image,lane,better_start=False):
        self.image=image
        self.y=280+(lane-1)*80
        self.better_start=better_start
        self.screen=screen
        self.skill = skill
        #tạo biến để chạy xe nếu xe chạy = 1 ko chạy = 0
        self.run = 1
        #vận tốc xe
        self.v = 20
        self.skill_active = False
        #thời gian hồi skill
        self.skill_cycle = 120
        #thời gian skill
        self.skill_duration = 10
    def active_skill(self,road_time,road_finish):
        #Skill tăng tốc độ
        if self.skill == 2 and self.skill_active == False:
            self.v = int(self.v*1.8)
            self.skill_active = True
        #Mặc định cho các xe
        elif road_finish == True:
            self.run = 1
        #Skill khoảng một thời gian thì tăng tốc tạm thời
        elif self.skill == 3 and road_time != 0:
            if self.skill_active == False:
                self.skill_cycle += 2
                self.run = 0
            if self.skill_cycle >= 720:
                self.skill_cycle = 0
                self.skill_active = True
                self.v = int(self.v*0.2) 
            if self.skill_active:
                self.run = 1
                self.skill_duration -= 1
                if self.skill_duration < 0:
                    self.skill_active = False
                    self.v *= 10
                    self.skill_duration = 20
        #tăng tốc nhanh trong thời gian ngắn(xài được 1 lần duy nhất)
        elif self.skill == 4:
            if self.skill_active:
                self.skill_duration -= 0.5
                self.run = 1
            if self.skill_duration < 0:
                self.skill_active = False
            if self.skill_cycle > 0 and road_time > random.randint(5,10):
                self.skill_cycle -= 50
                self.skill_active = True
    def draw(self,x,rank):
        self.x=x
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.screen.blit(self.image,self.rect)
        self.rank=rank
    def is_in(self,x,y):
        if self.x>=x-50 and self.x<=x+50 and self.y==y:
            return True
    def finish(self):
        if self.x>=end_bg:
            return True
    def check_ranked(self):
        if self.finish() and self.rank == 0:
            return True
        if self.rank>0:
            return False
class Item():
    image=pygame.transform.scale(item_pic,(50,50))
    exist=False
    def __init__(self):
        pass
    def draw(self,x,y,screen):
        self.screen=screen
        self.rect=self.image.get_rect(center=(x,y))
        self.screen.blit(self.image,self.rect)
    def affect(self,x,buff_skill):
        self.type=random.randint(0,4)
        if self.type==0 or self.type==2:
            x-=100*buff_skill
            pygame.mixer.Channel(4).play(back_sound)
        elif self.type==1 or self.type==3:
            x+=100*buff_skill
            pygame.mixer.Channel(5).play(flash_sound)
        else:
            pass
        return x
    
class Buttons():
    def __init__(self,height,width,image,x,y,screen):
        self.height=height
        self.width=width
        self.img=pygame.transform.scale(image,(height,width))
        self.x=x
        self.y=y
        self.rect=self.img.get_rect()
        self.screen=screen
    def draw(self):
        self.rect.topleft=(self.x,self.y)
        self.screen.blit(self.img,self.rect)
    def is_in(self,x,y):
        if x>self.x and x<self.x+self.height and y>self.y and y<self.y+self.width:
            return True
#Nhạc
class Music():
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def play(self):
        pygame.mixer.Channel(3).play(self.sound,-1)
    def stop(self):
        pygame.mixer.Channel(3).stop()

#Tạo đối tượng nhạc
music1=Music("Don't let me down - Illenium Remix",pygame.mixer.Sound(r'MainGame\Sound\Music\dont-let-me-down-illenium-remix.mp3'))
music2=Music("Lost Sky - Dreams Pt.II",pygame.mixer.Sound(r'MainGame\Sound\Music\dreams-pt-ii.mp3'))
music3=Music("Lost Sky - Where we start", pygame.mixer.Sound(r'MainGame\Sound\Music\Lost Sky - Where We Started.mp3'))
music4=Music("Cartoon - On & On",pygame.mixer.Sound(r'MainGame\Sound\Music\on-and-on.mp3'))

musics=[music1,music2,music3,music4]

#Minigame

def snakeGame(gameSurface):
    # load hình ảnh
    m = 20 # kích thước chiều cao và chiều rộng
    Imgbody = pygame.transform.scale(pygame.image.load(r'MainGame\minigame\snake\snake_b.png'),(m,m))
    Imghead = pygame.transform.scale(pygame.image.load(r'MainGame\minigame\snake\snake_h.png'),(m,m))
    Imgfood = pygame.transform.scale(pygame.image.load(r'MainGame\minigame\snake\apple.png'),(m,m))
    # tạo cửa sổ
    
    # màu sắc
    red = pygame.Color(255,0,0)
    blue = pygame.Color(65,105,255)
    black = pygame.Color(0,0,0)
    white = pygame.Color(255,255,255)
    gray = pygame.Color(128,128,128)
    # khai báo biến
    snakepos = [100,60]
    snakebody = [[100,60],[80,60],[60,60]]
    foodx = random.randrange(1,71)
    foody = random.randrange(1,45)
    if foodx % 2 != 0: foodx += 1
    if foody % 2 != 0: foody += 1
    foodpos = [foodx * 10, foody * 10]
    foodflat = True
    direction = 'RIGHT'
    changeto = direction
    score = 0
    # hàm gameover
    def game_over():
        gfont = pygame.font.SysFont('consolas',40)
        gsurf = gfont.render('Game over!',True,red)
        grect = gsurf.get_rect()
        grect.midtop = (640,300)
        gameSurface.blit(gsurf,grect)
        show_score(0)
        pygame.display.flip()
        time.sleep(3) #time wait to exit
    # hàm show_score
    def show_score(choice = 1):
        sfont = pygame.font.SysFont('consolas',20)
        ssurf = sfont.render('Score: {0}'.format(score),True,black)
        srect = ssurf.get_rect()
        if choice == 1:
            srect.midtop = (70,20)
        else:
            srect.midtop = (640,350)
        gameSurface.blit(ssurf,srect)
    # vòng lặp chính
    while True:
        pygame.time.delay(80) # tốc độ chơi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # xử lý phím
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN:
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.evet.Event(pygame.QUIT))
        # hướng đi
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        # cập nhật vị trí mới
        if direction == 'RIGHT':
            snakepos[0] += m
        if direction == 'LEFT':
            snakepos[0] -= m
        if direction == 'UP':
            snakepos[1] -= m
        if direction == 'DOWN':
            snakepos[1] += m
        #cơ chế thêm khúc dài ra
        snakebody.insert(0,list(snakepos))
        if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
            score += 1
            foodflat = False
        else:
            snakebody.pop()
        # sản sinh covid
        if foodflat == False:
            foodx = random.randrange(1,127)
            foody = random.randrange(1,71)
            if foodx %2 != 0: foodx += 1
            if foody %2 != 0: foody += 1
            foodpos = [foodx * 10, foody * 10]
        foodflat = True
        #  cập nhật lên cửa sổ
        gameSurface.fill(white)
        for pos in snakebody:
            gameSurface.blit(Imgbody,pygame.Rect(pos[0],pos[1],m,m))
            #pygame.draw.rect(gameSurface,blue,pygame.Rect(pos[0],pos[1],m,m))
        gameSurface.blit(Imghead,pygame.Rect(snakebody[0][0],snakebody[0][1],m,m)) # head
        gameSurface.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))
        #pygame.draw.rect(gameSurface,gray,pygame.Rect(foodpos[0],foodpos[1],m,m))
        # xử lý di chuyển đụng 4 cạnh biên
        if snakepos[0] > 1260 or snakepos[0] < 20:
            game_over()
            return score
        if snakepos[1] > 700 or snakepos[1] < 20:
            game_over()
            return score
        # xử lý tự ăn chính mình
        for b in snakebody[1:]:
            if snakepos[0] == b[0] and snakepos[1] == b[1]:
                game_over()
                return score
        # đường viền
        pygame.draw.rect(gameSurface,gray,(10,10,1260,700),2)
        show_score()
        pygame.display.flip()



    





#Vào đua
def run_game(map_index,char,buff_gold,better_start,user,player_name,screen):
    #Phát âm thanh
    pygame.mixer.Channel(3).play(car_sound,-1)
    #Khởi tạo xe 
    player_img=cars_img[char][0]
    com1_char=random.randint(0,24)
    com2_char=random.randint(0,24)
    com3_char=random.randint(0,24)
    com4_char=random.randint(0,24)
    while com1_char==char or com2_char==char or com3_char==char or com4_char==char:
        com1_char=random.randint(0,24)
        com2_char=random.randint(0,24)
        com3_char=random.randint(0,24)
        com4_char=random.randint(0,24)

    player=Car(screen,char//5,player_img,3,better_start)
    com1=Car(screen,com1_char//5,cars_img[com1_char][0],1)
    com2=Car(screen,com2_char//5,cars_img[com2_char][0],2)
    com3=Car(screen,com3_char//5,cars_img[com3_char][0],4)
    com4=Car(screen,com4_char//5,cars_img[com4_char][0],5)

    #Set tên
    player.name = player_name
    com1.name = 'com1'
    com2.name ='com2'
    com3.name ='com3'
    com4.name ='com4'
    
    #Map
    bg=maps[map_index]
    
    #Khởi tạo biến item
    item1=Item()
    enough_item=False
    num_item=0
    #Các tham số
    if player.better_start: 
        player_x=start_bg+100
    else:
        player_x=start_bg
    com1_x=start_bg
    com2_x=start_bg
    com3_x=start_bg
    com4_x=start_bg
    #Rank
    player_rank=0
    com1_rank=0
    com2_rank=0
    com3_rank=0
    com4_rank=0

    #Tham số trong vòng lặp game
    running=True
    bg_x=0
    road_x=0
    rank=1
    ranked=False
    check_rank = True
    road_finish=False
    road_time=0    
    index=0

    #Vòng lặp game
    start=False
    start_time=False
    time=180
    while running:
        fpsClock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                start_time=True
        if start_time:
            time-=1
            if time==0:
                start=True
                start_time=False
    
        #Vẽ background
        screen.blit(bg,(bg_x,0))
        screen.blit(bg,(bg_x+1280,0))
        #Vẽ đường
        if road_time==0:
            screen.blit(start_road,(road_x,240))
            screen.blit(road,(road_x+1280,240))
        elif road_time>=20:
            screen.blit(finish_road,(road_x,240))
        else:
            screen.blit(road,(road_x,240))
            screen.blit(road,(road_x+1280,240))
        road_speed=20

        #Vẽ xe
        if index>=3:
            index=0
        else:
            index+=1
        player.image=cars_img[char][index]
        com1.image=cars_img[com1_char][index]
        com2.image=cars_img[com2_char][index]
        com3.image=cars_img[com3_char][index]
        com4.image=cars_img[com4_char][index]
        player.draw(player_x,player_rank)
        com1.draw(com1_x,com1_rank)
        com2.draw(com2_x,com2_rank)
        com3.draw(com3_x,com3_rank)
        com4.draw(com4_x,com4_rank)

        #Cho đường, background chạy
        if start:
            #Animation
            if index>=3:
                index=0
            else:
                index+=1
            player.image=cars_img[char][index]
            com1.image=cars_img[com1_char][index]
            com2.image=cars_img[com2_char][index]
            com3.image=cars_img[com3_char][index]
            com4.image=cars_img[com4_char][index]
            
            #Vẽ đường
            if not(road_finish):
                road_x-=road_speed
                if road_x<-1280:
                    road_x=0
                    road_time+=1
                if road_time==20:
                    road_finish=True
                bg_x-=2
                if bg_x<-1280:
                    bg_x=0
            else:
                road_speed=0
                    
        #Cập nhật toạ độ cho xe
            if player_x<0:
                player_x=0
            if com1_x<0:
                com1_x=0
            if com2_x<0:
                com2_x=0
            if com3_x<0:
                com3_x=0
            if com4_x<0:
                com4_x=0

            #Nếu đường đã chạy hết, cho xe dùng ở đích
            if player_x < 540 and com1_x < 540 and com2_x < 540 and com3_x < 540 and com4_x < 540:
                player.run = 1
                com1.run = 1
                com2.run = 1
                com3.run = 1
                com4.run = 1
            elif road_finish:
                player.run = 1
                com1.run = 1
                com2.run = 1
                com3.run = 1
                com4.run = 1
            else:
                player.run = 0
                com1.run = 0
                com2.run = 0
                com3.run = 0
                com4.run = 0
            #skill
            player.active_skill(road_time,road_finish)
            com1.active_skill(road_time,road_finish)
            com2.active_skill(road_time,road_finish)
            com3.active_skill(road_time,road_finish)
            com4.active_skill(road_time,road_finish)
            

            
            if not(player.finish()):
                player_x+=random.randint(0,player.v)*player.run
                if player_x>1100:
                    player_x=1100
            if not(com1.finish()):
                com1_x+=random.randint(0,com1.v)*com1.run
                if com1_x>1100:
                    com1_x=1100
            if not(com2.finish()):
                com2_x+=random.randint(0,com2.v)*com2.run
                if com2_x>1100:
                    com2_x=1100
            if not(com3.finish()):
                com3_x+=random.randint(0,com3.v)*com3.run
                if com3_x>1100:
                    com3_x=1100
            if not(com4.finish()):
                com4_x+=random.randint(0,com4.v)*com4.run
                if com4_x>1100:
                    com4_x=1100
            #Đưa item vào

            if not(enough_item): #Nếu chưa đủ 2 item đang xuất hiện
                #Nếu item 1 chưa xuất hiện
                if not(item1.exist):
                    lane_item1=random.randint(1,5)
                    item1_y=280+(lane_item1-1)*80
                    item1_x=random.randint(600,1000)
                    if item1_x<end_bg:
                        item1.exist=True
                        num_item+=1
                #Vẽ item 1
                if item1.exist:
                    item1.draw(item1_x,item1_y,screen)
                    item1_x-=road_speed
                    if item1_x<0:
                        item1.exist=False
                        num_item-=1
                    
                    #Xử lý nếu xe chạm vào item
                    if player.is_in(item1_x,item1_y):
                        if player.skill == 0:#tăng hiệu ứng của bùa
                            player_x=item1.affect(player_x,1.5)
                            num_item-=1
                            item1.exist=False
                        elif player.skill == 1:#skill 1 kháng bùa
                            player_x=item1.affect(player_x,0)
                            num_item-=1
                            item1.exist=False
                        else:
                            player_x=item1.affect(player_x,1)
                            num_item-=1
                            item1.exist=False
                    if com1.is_in(item1_x,item1_y):
                        if com1.skill == 0:
                            com1_x=item1.affect(com1_x,1.5)
                            num_item-=1
                            item1.exist=False
                        elif com1.skill == 1:
                            com1_x=item1.affect(com1_x,0)
                            num_item-=1
                            item1.exist=False
                        else:
                            com1_x=item1.affect(com1_x,1)
                            num_item-=1
                            item1.exist=False
                    if com2.is_in(item1_x,item1_y):
                        if com2.skill == 0:
                            com2_x=item1.affect(com2_x,1.5)
                            num_item-=1
                            item1.exist=False
                        elif com2.skill == 1:
                            com2_x=item1.affect(com2_x,0)
                            num_item-=1
                            item1.exist=False
                        else:
                            com2_x=item1.affect(com2_x,1)
                            num_item-=1
                            item1.exist=False
                    if com3.is_in(item1_x,item1_y):
                        if com3.skill == 0:
                            com3_x=item1.affect(com3_x,1.5)
                            num_item-=1
                            item1.exist=False
                        elif com3.skill == 1:
                            com3_x=item1.affect(com3_x,0)
                            num_item-=1
                            item1.exist=False
                        else:
                            com3_x=item1.affect(com3_x,1)
                            num_item-=1
                            item1.exist=False
                    if com4.is_in(item1_x,item1_y):
                        if com4.skill == 0:
                            com4_x=item1.affect(com4_x,1.5)
                            num_item-=1
                            item1.exist=False
                        elif com4.skill == 1:
                            com4_x=item1.affect(com4_x,0)
                            num_item-=1
                            item1.exist=False
                        else:
                            com4_x=item1.affect(com4_x,1)
                            num_item-=1
                            item1.exist=False
                
                if num_item>1:
                    enough_item=True
                else:
                    enough_item=False
            #Xếp hạng
            #Thêm road_finish để tránh lỗi chưa chạy hết đường mà mới chạy đến cuối màn hình đã xếp hạng
            if player.check_ranked() and road_finish:
                player_rank=rank
                rank+=1
            if com1.check_ranked() and road_finish:
                com1_rank=rank
                rank+=1
            if com2.check_ranked() and road_finish:
                com2_rank=rank
                rank+=1
            if com3.check_ranked() and road_finish:
                com3_rank=rank
                rank+=1
            if com4.check_ranked() and road_finish:
                com4_rank=rank
                rank+=1
            #Kết thúc
            #Thêm điều kiện xếp hạng xong mới kết thúc vì xe cuối cùng không gọi hàm 
            if (player.finish() and com1.finish() and com2.finish() and com3.finish() and com4.finish()) and road_finish and (not(player.check_ranked()) and not(com1.check_ranked()) and not(com2.check_ranked()) and not(com3.check_ranked()) and not(com4.check_ranked())):
                start=False
                ranked=True
            # bảng xếp hạng
        if ranked:
            check_rank = ranked_rs(r'MainGame\Image\bxh.jpg',screen_size[0]/2,4*screen_size[1]/5,player,com1,com2,com3,com4,user,screen)
        #Vẽ thời gian
        if start_time and time>=120:
                draw_text("3",time_font,red,screen,screen_size[0]/2,screen_size[1]/2)
        elif start_time and time>=60:
                draw_text("2",time_font,(255,253,85),screen,screen_size[0]/2,screen_size[1]/2)
        elif start_time and time>0:
                draw_text("1",time_font,(0,255,0),screen,screen_size[0]/2,screen_size[1]/2)
        pygame.display.update()
        
        #thoát ra menu
        if check_rank ==False:
            user.money_update(player,buff_gold)
            break
    return player_rank
def shopping(screen,user,buff_gold,buff_start):
    #Khởi tạo nút
    buy_buff_gold=Buttons(200,100,buff_gold_img,340,360,screen)
    buy_better_start=Buttons(200,100,buff_start_img,740,360,screen)
    quit_bt=Buttons(200,100,return_bt_img,540,570,screen)
    time=0
    #Vòng lặp
    running_shop=True
    while running_shop:
        fpsClock.tick(FPS)
        spot = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if buy_buff_gold.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    if not(buff_gold):
                        if user.money>=2000:
                            user.money_change(-2000)
                            buff_gold=True
                        else:
                            draw_text("Bạn không đủ vàng!",ms_font,white,screen,screen_size[0]/2,screen_size[1]/2)
                            time=120
                if buy_better_start.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    if not(buff_start):
                        if user.money>=2000:
                            user.money_change(-2000)
                            buff_start=True
                        else:
                            draw_text("Bạn không đủ vàng!",ms_font,white,screen,screen_size[0]/2,screen_size[1]/2)
                            time=120
                if quit_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    running_shop=False
            if buy_buff_gold.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif buy_better_start.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif quit_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        if buff_gold:
            buy_buff_gold.img=pygame.transform.scale(buff_gold_ed_img,(200,100))
        if buff_start:
            buy_better_start.img=pygame.transform.scale(buff_start_ed_img,(200,100))
        if time<=0:
            screen.blit(bg,(0,0))
            buy_better_start.draw()
            buy_buff_gold.draw()
            quit_bt.draw()
        else:
            time-=1
        pygame.display.update()
    return (buff_gold,buff_start)

def set_name(screen):
    sname=""
    count = 0
    name=True
    type_name =False
    name_gap = Buttons(19*screen_size[0]/40,screen_size[1]/12,item_pic,screen_size[0]/4,screen_size[1]/4,screen)
    accept_bt = Buttons(screen_size[1]/12,screen_size[1]/12,next_ms_bt_img,29*screen_size[0]/40,screen_size[1]/4,screen)
    while name:
        count +=1
        if (count // 150) % 2 == 0:
            name_dis = sname + '_'
        else:
            name_dis = sname
        spot = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type==MOUSEBUTTONDOWN:
                if accept_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    name = False
                    return sname
                if name_gap.is_in(spot[0],spot[1]):
                    type_name = True
            if type_name == True and event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    sname = sname[:-1]
                elif event.key == K_RETURN:
                    name = False
                    return sname
                else:
                    sname += event.unicode
            if name_gap.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_IBEAM)
            elif accept_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        screen.blit(bg,(0,0))
        name_gap.draw()
        screen.fill(white,name_gap.rect)
        accept_bt.draw()
        if type_name:
            text_obj = font.render(name_dis,1,black)
            text_rect = text_obj.get_rect(topleft = (screen_size[0]/4,screen_size[1]/4))
            screen.blit(text_obj,text_rect)
        else:
            text_obj = font.render('Enter car\'s name here',1,(190,190,190))
            text_rect = text_obj.get_rect(topleft = (screen_size[0]/4,screen_size[1]/4))
            screen.blit(text_obj,text_rect)
        pygame.display.flip()
        pygame.display.update()



def pick_map(buff_gold,buff_start,current_user,player_name,char,screen):
    pick_bt=Buttons(200,100,start_bt_img,540,570,screen)
    next_bt=Buttons(100,100,next_ms_bt_img,980,340,screen)
    back_bt=Buttons(100,100,back_ms_bt_img,200,340,screen)
    skill=(char - char%5)/5
    player_img=cars_img[char]
    index=0
    run_map=True
    while run_map:
        fpsClock.tick(FPS)
        spot = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type==MOUSEBUTTONDOWN:
                #Chọn map
                if pick_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    run_map=False
                    run_game(index,char,buff_gold,buff_start,current_user,player_name,screen)
                #Chuyển map muốn chọn
                if next_bt.is_in(spot[0],spot[1]):
                    index+=1
                    if index>4:
                        index=0
                if back_bt.is_in(spot[0],spot[1]):
                    index-=1
                    if index<0:
                        index=4
            if pick_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif next_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif back_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        screen.blit(bg,(0,0))
        pick_bt.draw()
        next_bt.draw()
        back_bt.draw()
        screen.blit(pick_maps[index],(440,210))
        pygame.display.update()

def pick_char(screen,username):
    pick1=Buttons(200,200,cars3_0,280,160,screen)
    pick2=Buttons(200,200,cars7_0,540,160,screen)
    pick3=Buttons(200,200,cars13_0,800,160,screen)
    pick4=Buttons(200,200,cars19_0,410,400,screen)
    pick5=Buttons(200,200,cars20_0,670,400,screen)
    return_bt=Buttons(150,150,return_bt_img,0,0,screen)
    accept=0
    index=0
    run_map=True
    while run_map:
        fpsClock.tick(FPS)
        spot = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type==MOUSEBUTTONDOWN:
                #Di chuyển giữa các bước chọn
                if accept==0:
                    if pick1.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        index=1
                        accept+=1
                    if pick2.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        index=2
                        accept+=1
                    if pick3.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        index=3
                        accept+=1
                    if pick4.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        index=4
                        accept+=1
                    if pick5.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        index=5
                        accept+=1
                    if return_bt.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        accept-=1
                        index=0
                
                elif accept==1:
                    if pick1.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        return 5*(index-1)
                    if pick2.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        return 5*(index-1)+1
                    if pick3.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        return 5*(index-1)+2
                    if pick4.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        return 5*(index-1)+3
                    if pick5.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        return 5*(index-1)+4
                    if return_bt.is_in(spot[0],spot[1]):
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        accept-=1
                        index=0

            if pick1.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif pick2.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif pick3.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif pick4.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif pick5.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        if index==0:
            pick1.img=pygame.transform.scale(cars3_0,(pick1.height,pick1.width))
            pick2.img=pygame.transform.scale(cars7_0,(pick2.height,pick2.width))
            pick3.img=pygame.transform.scale(cars13_0,(pick3.height,pick3.width))
            pick4.img=pygame.transform.scale(cars19_0,(pick4.height,pick4.width))
            pick5.img=pygame.transform.scale(cars20_0,(pick5.height,pick5.width))
        if index==1:
            pick1.img=pygame.transform.scale(cars0_0,(pick1.height,pick1.width))
            pick2.img=pygame.transform.scale(cars1_0,(pick1.height,pick1.width))
            pick3.img=pygame.transform.scale(cars2_0,(pick1.height,pick1.width))
            pick4.img=pygame.transform.scale(cars3_0,(pick1.height,pick1.width))
            pick5.img=pygame.transform.scale(cars4_0,(pick1.height,pick1.width))
        if index==2:
            pick1.img=pygame.transform.scale(cars5_0,(pick1.height,pick1.width))
            pick2.img=pygame.transform.scale(cars6_0,(pick1.height,pick1.width))
            pick3.img=pygame.transform.scale(cars7_0,(pick1.height,pick1.width))
            pick4.img=pygame.transform.scale(cars8_0,(pick1.height,pick1.width))
            pick5.img=pygame.transform.scale(cars9_0,(pick1.heig1ht,pick1.width))
        if index==3:
            pick1.img=pygame.transform.scale(cars10_0,(pick1.height,pick1.width))
            pick2.img=pygame.transform.scale(cars11_0,(pick1.height,pick1.width))
            pick3.img=pygame.transform.scale(cars12_0,(pick1.height,pick1.width))
            pick4.img=pygame.transform.scale(cars13_0,(pick1.height,pick1.width))
            pick5.img=pygame.transform.scale(cars14_0,(pick1.height,pick1.width))
        if index==4:
            pick1.img=pygame.transform.scale(cars15_0,(pick1.height,pick1.width))
            pick2.img=pygame.transform.scale(cars16_0,(pick1.height,pick1.width))
            pick3.img=pygame.transform.scale(cars17_0,(pick1.height,pick1.width))
            pick4.img=pygame.transform.scale(cars18_0,(pick1.height,pick1.width))
            pick5.img=pygame.transform.scale(cars19_0,(pick1.height,pick1.width))
        if index==5:
            pick1.img=pygame.transform.scale(cars20_0,(pick1.height,pick1.width))
            pick2.img=pygame.transform.scale(cars21_0,(pick1.height,pick1.width))
            pick3.img=pygame.transform.scale(cars22_0,(pick1.height,pick1.width))
            pick4.img=pygame.transform.scale(cars23_0,(pick1.height,pick1.width))
            pick5.img=pygame.transform.scale(cars24_0,(pick1.height,pick1.width))
        screen.blit(bg,(0,0))
        pick1.draw()
        pick2.draw()
        pick3.draw()
        pick4.draw()
        pick5.draw()
        return_bt.draw()
        if accept==-1:
            main_menu(username)
        pygame.display.update()

#Sảnh chờ
def main_menu(username):
    current_user = User(username)
    current_user.create_player_history()
    screen=pygame.display.set_mode(screen_size,pygame.RESIZABLE)
    pygame.display.set_caption("Car Bet")
    icon=pygame.image.load(r'MainGame\Image\car.jpg')
    pygame.display.set_icon(icon)

    #Khởi tạo nút
    profile_bt = Buttons(200,100,profile_bt_img,20,20,screen)
    start_bt=Buttons(200,100,start_bt_img,540,570,screen)
    shop_bt=Buttons(100,100,shop_bt_img,50,570,screen)
    minigame_bt=Buttons(100,100,minigame_bt_img,50,310,screen)
    next_music_bt=Buttons(30,30,next_ms_bt_img,1050,100,screen)
    back_music_bt=Buttons(30,30,back_ms_bt_img,1000,100,screen)
    stop_music_bt=Buttons(30,30,dis_ms_bt_img,940,100,screen)
    guide_bt=Buttons(70,70,help_bt_img,1160,600,screen)

    #Nhạc
    ms_index=0
    is_play=False
    stop=False

    #Thời gian hiện chữ
    time=0

    #Tham số của người chơi
    buff=(False,False)
    char=-1
    player_name='2'
    draw_guide=False
    running_menu=True
    #Vòng lặp
    while running_menu:
        fpsClock.tick(FPS)
        #Lấy tọa độ chuột
        spot = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            #Thay đổi kích thước màn hình
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type==pygame.MOUSEBUTTONDOWN:
                #Xử lý thao tác trên các nút
                #Nút vào game
                if start_bt.is_in(spot[0],spot[1]):
                    time = 0
                    running_menu=False
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    char=pick_char(screen,username)
                    player_name = set_name(screen)
                    if char>=0:
                        pick_map(buff[0],buff[1],current_user,player_name,char,screen)
                    buff=(False,False)
                    running_menu=True
                #Nút shop
                if shop_bt.is_in(spot[0],spot[1]):
                    time = 0
                    running_menu=False
                    #đổi lại hình dạng chuột ban đầu sau khi click
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    buff=shopping(screen,current_user,buff[0],buff[1])
                    running_menu=True
                #Nút show profile
                if profile_bt.is_in(spot[0],spot[1]):
                    time = 0
                    running_menu=False
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    profile_display(current_user,screen)
                    running_menu=True
                #Nút minigame
                if minigame_bt.is_in(spot[0],spot[1]):
                    if current_user.money<=2000:
                        time = 0
                        running_menu=False
                        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                        score=snakeGame(screen)
                        current_user.money_change(score*100)
                        running_menu=True
                    else:
                        draw_text("Khi dưới 2000 vàng mới được chơi minigame!", ms_font, white, screen, 640,360)
                        time = 240
                #Nút chuyển nhạc
                if next_music_bt.is_in(spot[0],spot[1]):
                    ms_index+=1
                    is_play=False
                    if ms_index>=len(musics):
                        ms_index=0
                if back_music_bt.is_in(spot[0],spot[1]):
                    ms_index-=1
                    is_play=False
                    if ms_index<0:
                        ms_index=len(musics)-1
                if stop_music_bt.is_in(spot[0],spot[1]) and not(stop):
                    stop_music_bt.img=pygame.transform.scale(en_ms_bt_img,(30,30))
                    musics[ms_index].stop()
                    stop=True
                elif stop_music_bt.is_in(spot[0],spot[1]) and stop:
                    stop_music_bt.img=pygame.transform.scale(dis_ms_bt_img,(30,30))
                    musics[ms_index].play()
                    stop=False
                if guide_bt.is_in(spot[0],spot[1]):
                    draw_guide=True
                if not(guide_bt.is_in(spot[0],spot[1])) and draw_guide:
                    draw_guide=False
                


            #Thay đổi hình dạng chuột
            if start_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif shop_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif profile_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif minigame_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif next_music_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif back_music_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif stop_music_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif guide_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        if time <= 0:
            screen.blit(bg,(0,0))
        else:
            time-=1
        #Vẽ nút
        profile_bt.draw()
        shop_bt.draw()
        start_bt.draw()
        minigame_bt.draw()
        next_music_bt.draw()
        back_music_bt.draw()
        stop_music_bt.draw()
        guide_bt.draw()
        if draw_guide:
            screen.blit(guide_img,(280,0))
        #Phát nhạc
        if not(is_play) and not(stop):
            musics[ms_index].play()
            is_play=True
        #Tên Nhạc
        draw_text(musics[ms_index].name,ms_font,white,screen,1040,75)
        pygame.display.update()

def ranked_rs(image,width,height,player,com1,com2,com3,com4,user,screen):
    rank_surface = pygame.Surface((25 * screen_size[0]/ 64 ,55 * screen_size[1]/ 72))
    rank_surface.fill((255, 0, 0))
    rank_img = pygame.transform.scale(pygame.image.load(image),(25 * screen_size[0]/ 64 ,55 * screen_size[1]/ 72))
    rank_rect = rank_img.get_rect(topleft=(0,0))
    running_rank = True
    home_bt = Buttons(screen_size[0]/16,screen_size[1]/8,return_bt_img,screen_size[0]/4,9*screen_size[1]/10,screen)
    save_bt = Buttons(screen_size[0]/16,screen_size[1]/8,save_bt_img,3*screen_size[0]/4,9*screen_size[1]/10,screen)
    lt = [player,com1,com2,com3,com4]

    # sắp xếp thứ tự xếp hạng
    j=0
    while j < len(lt):
        i=j
        sw=False
        while i < len(lt)-1:
            if lt[i].rank > lt[i+1].rank :
                sw = True
                temp=lt[i]
                lt[i]=lt[i+1]
                lt[i+1]=temp
            i+=1
        if sw == False:
            break
    while running_rank:
        fpsClock.tick(FPS)
        spot=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if home_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    running_rank = False
                if save_bt.is_in(spot[0],spot[1]):
                    user.history_saved(screen)
            if home_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif save_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else :
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)

        screen.blit(rank_surface,((screen_size[0] - 25 * screen_size[0]/ 64) / 2,(screen_size[1] - 55 * screen_size[1]/ 72) / 2))
        rank_surface.blit(rank_img, rank_rect)
        #vẽ nút
        home_bt.draw()
        save_bt.draw()
        draw_text('1',new_font,black,rank_surface,screen_size[0]/16,17*screen_size[1]/72)
        draw_text('2',new_font,black,rank_surface,screen_size[0]/16,25*screen_size[1]/72)
        draw_text('3',new_font,black,rank_surface,screen_size[0]/16,33*screen_size[1]/72)
        draw_text('4',new_font,black,rank_surface,screen_size[0]/16,41*screen_size[1]/72)
        draw_text('5',new_font,black,rank_surface,screen_size[0]/16,49*screen_size[1]/72)

        draw_text(lt[0].name,new_font,lt[0].color,rank_surface,screen_size[0]/4,17*screen_size[1]/72)
        draw_text(lt[1].name,new_font,lt[1].color,rank_surface,screen_size[0]/4,25*screen_size[1]/72)
        draw_text(lt[2].name,new_font,lt[2].color,rank_surface,screen_size[0]/4,33*screen_size[1]/72)
        draw_text(lt[3].name,new_font,lt[3].color,rank_surface,screen_size[0]/4,41*screen_size[1]/72)
        draw_text(lt[4].name,new_font,lt[4].color,rank_surface,screen_size[0]/4,49*screen_size[1]/72)
        pygame.display.flip()
    return False



def History(user,display,page,screen):
    run = True
    hrt_surf = pygame.transform.scale(pygame.image.load(user.path+'/'+user.file_list[display+page*5]),(screen_size[0],screen_size[1]))
    hrt_rect = hrt_surf.get_rect(topleft=(0,0))
    return_bt = Buttons(screen_size[0]/24,screen_size[0]/24,return_bt_img,23*screen_size[0]/24,screen_size[1]-screen_size[0]/24,screen)
    while run:
        fpsClock.tick(FPS)
        spot=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type == MOUSEBUTTONDOWN:
                if return_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    run = False
            if return_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        screen.blit(hrt_surf,hrt_rect)
        return_bt.draw()
        pygame.display.flip()




def profile_display(user,screen):
    run = True
    page = 0
    display = -1
    max_dis = len(user.file_list) % 5 -1
    return_bt = Buttons(screen_size[0]/24,screen_size[0]/24,return_bt_img,23*screen_size[0]/24,screen_size[1]-screen_size[0]/24,screen)
    next_bt = Buttons(screen_size[0]/24,screen_size[0]/24,next_ms_bt_img,3*screen_size[0]/4,8*screen_size[1]/9,screen)
    back_bt = Buttons(screen_size[0]/24,screen_size[0]/24,back_ms_bt_img,screen_size[0]/4,8*screen_size[1]/9,screen)
    History1_bt = Buttons(screen_size[0],screen_size[1]/10,item_pic,0,3*screen_size[1]/9,screen)
    History2_bt = Buttons(screen_size[0],screen_size[1]/10,item_pic,0,4*screen_size[1]/9,screen)
    History3_bt = Buttons(screen_size[0],screen_size[1]/10,item_pic,0,5*screen_size[1]/9,screen)
    History4_bt = Buttons(screen_size[0],screen_size[1]/10,item_pic,0,6*screen_size[1]/9,screen)
    History5_bt = Buttons(screen_size[0],screen_size[1]/10,item_pic,0,7*screen_size[1]/9,screen)
    lists = ['','','','','']
    color = [black,black,black,black,black]
    while run:
        fpsClock.tick(FPS)
        if len(user.file_list) % 5 != 0:
            max_page = len(user.file_list) // 5 + 1
        else :
            max_page = len(user.file_list) // 5 
        for i in range(5):
            lists[i] = user.get_file_name(i+page*5)
        spot=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type == MOUSEBUTTONDOWN:
                if return_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    run = False
                if next_bt.is_in(spot[0],spot[1]):
                    if page < max_page-1:
                        page += 1
                if back_bt.is_in(spot[0],spot[1]):
                    if page >= 1:
                        page -= 1
                if History1_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 0)):
                    display = 0
                if History2_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 1)):
                    display = 1
                if History3_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 2)):
                    display = 2
                if History4_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 3)):
                    display = 3
                if History5_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 4)):
                    display = 4
                if display >= 0:
                    History(user,display,page,screen)
                    display = -1
        if return_bt.is_in(spot[0],spot[1]):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
        elif next_bt.is_in(spot[0],spot[1]):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
        elif back_bt.is_in(spot[0],spot[1]):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
        elif History1_bt.is_in(spot[0],spot[1])  and (page != max_page-1 or (page == max_page-1 and max_dis >= 0)):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            color[0] = (0,255,0)
        elif History2_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 1)):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            color[1] = (0,255,0)
        elif History3_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 2)):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            color[2] = (0,255,0)
        elif History4_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 3)):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            color[3] = (0,255,0)
        elif History5_bt.is_in(spot[0],spot[1]) and (page != max_page-1 or (page == max_page-1 and max_dis >= 4)):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            color[4] = (0,255,0)
        else:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        if not(History1_bt.is_in(spot[0],spot[1])):
            color[0] = (0,0,0)
        if not(History2_bt.is_in(spot[0],spot[1])):
            color[1] = (0,0,0)
        if not(History3_bt.is_in(spot[0],spot[1])):
            color[2] = (0,0,0)
        if not(History4_bt.is_in(spot[0],spot[1])):
            color[3] = (0,0,0)
        if not(History5_bt.is_in(spot[0],spot[1])):
            color[4] = (0,0,0)
    #vẽ màn hình, nút
        screen.fill((220,220,220))
        return_bt.draw()
        next_bt.draw()
        back_bt.draw()
        History1_bt.draw()
        History2_bt.draw()
        History3_bt.draw()
        History4_bt.draw()
        History5_bt.draw()
        screen.fill(white,History1_bt.rect)
        screen.fill(white,History2_bt.rect)
        screen.fill(white,History3_bt.rect)
        screen.fill(white,History4_bt.rect)
        screen.fill(white,History5_bt.rect)
        draw_text(lists[0],history_font,color[0],screen,History1_bt.x+History1_bt.height/2,History1_bt.y+History1_bt.width/2)
        draw_text(lists[1],history_font,color[1],screen,History2_bt.x+History2_bt.height/2,History2_bt.y+History2_bt.width/2)
        draw_text(lists[2],history_font,color[2],screen,History3_bt.x+History3_bt.height/2,History3_bt.y+History3_bt.width/2)
        draw_text(lists[3],history_font,color[3],screen,History4_bt.x+History4_bt.height/2,History4_bt.y+History4_bt.width/2)
        draw_text(lists[4],history_font,color[4],screen,History5_bt.x+History5_bt.height/2,History5_bt.y+History5_bt.width/2)
        draw_text(str(page+1),name_font,black,screen,screen_size[0]/2,9*screen_size[1]/10)
        draw_text('username:'+user.username,name_font,black,screen,screen_size[0]/4,screen_size[1]/12)
        draw_text('Money:'+str(user.money),name_font,black,screen,screen_size[0]/4,screen_size[1]/6)
        pygame.display.flip()

def email():
    # Tạo cửa sổ giao diện
    window = tk.Tk()
    window.title("Xác thực bằng email")
    window.geometry('1280x720')

    # Tạo một đối tượng Canvas
    canvas = Canvas(window, width=1280, height=720)
    canvas.pack()

    # Tải hình ảnh và lưu trữ nó trong một biến
    image = ImageTk.PhotoImage(Image.open(r'MainGame\picture\background3.jpg'))

    # Vẽ hình ảnh trên Canvas
    canvas.create_image(0, 0, anchor=NW, image=image)

    # Thay đổi các giá trị dưới đây bằng thông tin của bạn
    sender_email = "carbet947@gmail.com"

    subject = "Car Bet"
    random_number = random.randint(100000,999999)
    message1 = "Your code is "
    message2 = random_number
    text = f"Subject: {subject}\n{message1}{message2}"

    # Tạo kết nối đến máy chủ email
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,"qvnceohsanbgfgns")


    def on_entry_focus_in(event):
        if entry_username.get() == "Tên đăng nhập":
            entry_username.delete(0, tk.END)

    def on_entry_focus_out(event):
        if entry_username.get() == "":
            entry_username.insert(0, "Tên đăng nhập")

    entry_username = tk.Entry(window, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_username.insert(0, "Tên đăng nhập")
    entry_username.bind("<FocusIn>", on_entry_focus_in)
    entry_username.bind("<FocusOut>", on_entry_focus_out)

    entry_username.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_username.place(x=442, y=184)


    def on_entry_focus_in(event):
        if entry_email.get() == "Email":
            entry_email.delete(0, tk.END)

    def on_entry_focus_out(event):
        if entry_email.get() == "":
            entry_email.insert(0, "Email")

    entry_email = tk.Entry(window, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_email.insert(0, "Email")
    entry_email.bind("<FocusIn>", on_entry_focus_in)
    entry_email.bind("<FocusOut>", on_entry_focus_out)

    entry_email.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_email.place(x=442, y=269)

    # Tạo button gửi mail
    image_sendmail = Image.open(r'MainGame\picture\button_sendmail.jpg')
    resize_sendmail_img = image_sendmail.resize((376,63))
    photo_sendmail = ImageTk.PhotoImage(resize_sendmail_img)


    #Quên mk, đăng nhập bằng mail
    def send_email(): 
        email = entry_email.get()

        # Mở file email.txt và đọc tất cả các email lưu trong đó
        with open("email.txt", "r") as file:
            emails = file.read().splitlines()

        # Kiểm tra email có trong file email.txt hay không
        for email in emails:
            username,receiver = email.strip().split(":")

            if username == entry_username.get() and receiver == entry_email.get():
                # Gửi email
                server.sendmail(sender_email, email, text)

    # Tạo button và chèn ảnh vào button 
    button_sendmail = Button(window, image=photo_sendmail, command=send_email)
    canvas.create_window(623, 373, anchor=CENTER, window=button_sendmail)

    entry_code = tk.Entry(window, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_code.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_code.place(x=442, y=459)

    image_checkcode = Image.open(r'MainGame\picture\button_checkcode.jpg')
    resize_checkcode_img = image_checkcode.resize((376,63))
    photo_checkcode = ImageTk.PhotoImage(resize_checkcode_img)

    # Gán một hàm xử lý sự kiện cho nút
    def button_checkcode():
        ma_so = entry_code.get()
        if float(ma_so) == message2:
            messagebox.showinfo("Thông báo","Mã số chính xác!")
        else:
            messagebox.showerror("Thông báo", "Mã số không chính xác")

    # Tạo button và chèn ảnh vào button 
    button_checkcode = Button(window, image=photo_checkcode, command=button_checkcode)
    canvas.create_window(623, 569, anchor=CENTER, window=button_checkcode)


    image_return = Image.open(r'MainGame\picture\button_return.jpg')
    resize_return_img = image_return.resize((130,50))
    photo_return = ImageTk.PhotoImage(resize_return_img)

    # Gán một hàm xử lý sự kiện cho nút
    def button_return():
        window.destroy()
        login()
        
    # Tạo button và chèn ảnh vào button 
    button_return = Button(window, image=photo_return, command=button_return)
    canvas.create_window(630, 650, anchor=CENTER, window=button_return)

    # Chạy chương trình
    window.mainloop()


def login():
    window = tk.Tk()
    window.title("Đăng nhập")
    window.geometry('1280x720')

        # Tạo một đối tượng Canvas
    canvas = Canvas(window, width=1280, height=720)
    canvas.pack()

    # Tải hình ảnh và lưu trữ nó trong một biến
    image = ImageTk.PhotoImage(Image.open(r'MainGame\picture\background1.jpg'))

    # Vẽ hình ảnh trên Canvas
    canvas.create_image(0, 0, anchor=NW, image=image)

    def on_entry_focus_in(event):
        if entry_username.get() == "Tên đăng nhập":
            entry_username.delete(0, tk.END)

    def on_entry_focus_out(event):
        if entry_username.get() == "":
            entry_username.insert(0, "Tên đăng nhập")

    entry_username = tk.Entry(window, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_username.insert(0, "Tên đăng nhập")
    entry_username.bind("<FocusIn>", on_entry_focus_in)
    entry_username.bind("<FocusOut>", on_entry_focus_out)

    entry_username.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_username.place(x=442, y=184)

    def on_entry_focus_in(event):
        if entry_password.get() == "Mật khẩu":
            entry_password.delete(0, tk.END)

    def on_entry_focus_out(event):
        if entry_password.get() == "":
            entry_password.insert(0, "Mật khẩu")

    entry_password = tk.Entry(window, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_password.insert(0, "Mật khẩu")
    entry_password.bind("<FocusIn>", on_entry_focus_in)
    entry_password.bind("<FocusOut>", on_entry_focus_out)

    entry_password.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_password.place(x=442, y=269)

    # Tạo button đăng ký
    image_login = Image.open(r'MainGame\picture\button_dangnhap.jpg')
    resize_login_img = image_login.resize((376,63))
    photo_login = ImageTk.PhotoImage(resize_login_img)


    image_signin = Image.open(r'MainGame\picture\button_dangky.jpg')
    resize_sigin_img = image_signin.resize((376,63))
    photo_signin = ImageTk.PhotoImage(resize_sigin_img)


    # Gán một hàm xử lý sự kiện cho nút
    def button_register():
        window.destroy()
        register()

    # Tạo button và chèn ảnh vào button 
    button_register = Button(window, image=photo_signin,command=button_register)
    canvas.create_window(623, 550, anchor=CENTER, window=button_register)

    # Tạo hàm kiểm tra tên đăng nhập và mật khẩu    
    def check_login():
        # Mở file accounts.txt và đọc tất cả các tài khoản
        with open("accounts.txt", "r") as f:
            accounts = f.readlines()

        # Kiểm tra tên đăng nhập và mật khẩu có trong file accounts.txt hay không
        for account in accounts:
            user1, passw = account.strip().split(":")
            if user1 == entry_username.get() and passw == entry_password.get():
                messagebox.showinfo("Thông báo", "Đăng nhập thành công.")
                window.destroy()
                main_menu(user1)          
        messagebox.showerror("Thông báo", "Tên đăng nhập hoặc mật khẩu không đúng!")

        # Tạo button và chèn ảnh vào button 
    button_login = Button(window, image=photo_login, command=check_login)
    canvas.create_window(623, 373, anchor=CENTER, window=button_login)

    image_forget = Image.open(r'MainGame\picture\button_forget.jpg')
    resize_forget_img = image_forget.resize((238,50))
    photo_forget = ImageTk.PhotoImage(resize_forget_img)

    # Gán một hàm xử lý sự kiện cho nút
    def button_forget():
        window.destroy()
        email()

    # Tạo button và chèn ảnh vào button 
    button_forget = Button(window, image=photo_forget,command=button_forget)
    canvas.create_window(738, 675, anchor=CENTER, window=button_forget)

    # Chạy chương trình
    window.mainloop()

def register():
    root = tk.Tk()
    root.title("Đăng ký tài khoản")
    root.geometry('1280x720')

    # Tạo một đối tượng Canvas
    canvas = Canvas(root, width=1280, height=720)
    canvas.pack()

    # Tải hình ảnh và lưu trữ nó trong một biến
    image = ImageTk.PhotoImage(Image.open(r'MainGame\picture\background2.jpg'))

    # Vẽ hình ảnh trên Canvas
    canvas.create_image(0, 0, anchor=NW, image=image)

    def on_entry_focus_in(event):
        if entry_username.get() == "Tên đăng nhập":
            entry_username.delete(0, tk.END)

    def on_entry_focus_out(event):
        if entry_username.get() == "":
            entry_username.insert(0, "Tên đăng nhập")

    entry_username = tk.Entry(root, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_username.insert(0, "Tên đăng nhập")
    entry_username.bind("<FocusIn>", on_entry_focus_in)
    entry_username.bind("<FocusOut>", on_entry_focus_out)

    entry_username.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_username.place(x=442, y=184)

    def on_entry_focus_in(event):
        if entry_password.get() == "Mật khẩu":
            entry_password.delete(0, tk.END)

    def on_entry_focus_out(event):
        if entry_password.get() == "":
            entry_password.insert(0, "Mật khẩu")

    entry_password = tk.Entry(root, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_password.insert(0, "Mật khẩu")
    entry_password.bind("<FocusIn>", on_entry_focus_in)
    entry_password.bind("<FocusOut>", on_entry_focus_out)

    entry_password.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_password.place(x=442, y=269)

    def on_entry_focus_in(event):
        if entry_email.get() == "Email":
            entry_email.delete(0, tk.END)

    def on_entry_focus_out(event):
        if entry_email.get() == "":
            entry_email.insert(0, "Email")

    entry_email = tk.Entry(root, width=19, font=("Times New Roman", 28), fg="black", bg="white")
    entry_email.insert(0, "Email")
    entry_email.bind("<FocusIn>", on_entry_focus_in)
    entry_email.bind("<FocusOut>", on_entry_focus_out)

    entry_email.pack()
    # Đặt vị trí của entry trên ảnh:
    entry_email.place(x=442, y=354)

    # Tạo button đăng nhập
    image_login = Image.open(r'MainGame\picture\button_dangnhap.jpg')
    resize_login_img = image_login.resize((376,63))
    photo_login = ImageTk.PhotoImage(resize_login_img)

    # Gán một hàm xử lý sự kiện cho nút
    def button_login():
        root.destroy()
        login()
        
    # Tạo button và chèn ảnh vào button 
    button_login = Button(root, image=photo_login, command=button_login)
    canvas.create_window(623, 620, anchor=CENTER, window=button_login)

    sender_email = "carbet947@gmail.com"
    subject = "Car Bet"
    random_number = random.randint(100000,999999)
    message1 = "Your code is "
    message2 = random_number
    text = f"Subject: {subject}\n{message1}{message2}"

    # Tạo kết nối đến máy chủ email
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,"qvnceohsanbgfgns")


    def check_register():
        username = entry_username.get()
        password = entry_password.get()
        email = entry_email.get()
 
        def check_code_and_save_account():

            # Tạo cửa sổ giao diện
            root = tk.Tk()
            root.title("Xác nhận tài khoản")
            root.geometry('1280x720')

            # Tạo một đối tượng Canvas
            canvas = Canvas(root, width=1280, height=720)
            canvas.pack()

            # Tải hình ảnh và lưu trữ nó trong một biến
            image = ImageTk.PhotoImage(Image.open(r'MainGame\picture\background4.jpg'))

            # Vẽ hình ảnh trên Canvas
            canvas.create_image(0, 0, anchor=NW, image=image)

            entry_code = tk.Entry(root, width=19, font=("Times New Roman", 28), fg="black", bg="white")
            entry_code.pack()
            # Đặt vị trí của entry trên ảnh:
            entry_code.place(x=440, y=269)

            image_checkcode = Image.open('MainGame/picture/button_checkcode.jpg')
            resize_checkcode_img = image_checkcode.resize((376,63))
            photo_checkcode = ImageTk.PhotoImage(resize_checkcode_img)

            # Gán một hàm xử lý sự kiện cho nút
            def button_check():
                ma_so = entry_code.get()
                if float(ma_so) == message2:
                    with open("accounts.txt", 'a') as file:
                        file.write(f"{username}:{password}\n")  
                    with open("email.txt",'a') as file:
                        file.write(f"{username}:{email}\n")
                    messagebox.showinfo("Thông báo", "Đăng ký tài khoản thành công!")
                else:
                    messagebox.showerror("Thông báo", "Mã số không chính xác!")
                

            # Tạo button và chèn ảnh vào button 
            button_checkcode = Button(root, image=photo_checkcode, command=button_check)
            canvas.create_window(621, 378, anchor=CENTER, window=button_checkcode)

            image_return = Image.open('MainGame/picture/button_return.jpg')
            resize_return_img = image_return.resize((130,50))
            photo_return = ImageTk.PhotoImage(resize_return_img)

            # Gán một hàm xử lý sự kiện cho nút
            def button_return():
                root.destroy()
                register()
    
            # Tạo button và chèn ảnh vào button 
            button_return = Button(root, image=photo_return, command=button_return)
            canvas.create_window(630, 460, anchor=CENTER, window=button_return)

            root.mainloop()


        with open("accounts.txt", "r") as f:
                accounts = f.readlines()
            # Kiểm tra tên đăng nhập và mật khẩu có trong file accounts.txt hay không
                for account in accounts:
                    username1, password1 = account.strip().split(":")
                    if username1 == entry_username.get() and password1 == entry_password.get():
                        messagebox.showinfo("Thông báo", "Tài khoản đã tồn tại.")
                    else: 
        # Kiểm tra xem tên đăng nhập và mật khẩu có hợp lệ không
                        if (entry_username.get() == "" or entry_password.get() == "" or entry_username.get() == "Tên đăng nhập" or entry_password.get()=="Mật khẩu"):
                            messagebox.showerror("Lỗi", "Vui lòng nhập tên đăng nhập và mật khẩu.")
                        else:  
                            if (entry_email.get()=="" or entry_email.get()=="Email"):
                                messagebox.showerror("Lỗi", "Vui lòng nhập email.")
                            else:
                                server.sendmail(sender_email, email, text)
                                root.destroy()
                                check_code_and_save_account()
                                
        

    image_signin = Image.open('MainGame/picture/button_dangky.jpg')
    resize_sigin_img = image_signin.resize((376,63))
    photo_signin = ImageTk.PhotoImage(resize_sigin_img)

    # Tạo button và chèn ảnh vào button 
    button_register = Button(root, image=photo_signin,command=check_register)
    canvas.create_window(623, 483, anchor=CENTER, window=button_register)


    if __name__ == "__main__":
        root.mainloop()