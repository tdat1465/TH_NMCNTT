import pygame, sys, time, random, os
import tkinter as tk
import tkinter.messagebox as messagebox
from pygame.locals import *
from tkinter import *
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(10)
FPS = 120
fpsClock = pygame.time.Clock()

#Cửa sổ games
screen_size=(1280,720)

#Thêm background
bg=pygame.transform.scale(pygame.image.load(r'MainGame\Image\bg3.jpg'),screen_size)
road=pygame.transform.scale(pygame.image.load(r'MainGame\Image\road.jpg'),(1280,400))
start_road=pygame.transform.scale(pygame.image.load(r'MainGame\Image\start_road.jpg'),(1280,400))
finish_road=pygame.transform.scale(pygame.image.load(r'MainGame\Image\finish_road.jpg'),(1280,400))
end_bg=1000
start_bg=200
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

#Ảnh nút
start_bt_img=pygame.image.load(r'MainGame\Image\start_bt.jpg')
buff_start_img=pygame.image.load(r'MainGame\Image\startbuff.jpg')
buff_start_ed_img=pygame.image.load(r'MainGame\Image\start_buff.jpg')

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
    def create_player_history(self):#tạo một lần duy nhất cho 1 user
        if os.path.exists(self.path) == False:
            os.mkdir(self.path)
    def history_saved(self,screen):
        self.image_file = self.path + '/history'+str(self.htr_in)+'.png'
        pygame.image.save(screen,self.image_file)
        self.htr_in +=1
    def money_update(self,player):
        if player.rank == 1:
            self.money += 5000
        if player.rank == 2:
            self.money += 2000
        else:
            self.money -= 1000
    def money_change(self,dif):
        self.money+=dif
class Car():
    name=''
    color=(0,0,0)
    def __init__(self,screen,image,lane,buff_speed=False,better_start=False):
        self.image=image
        self.y=280+(lane-1)*80
        self.buff_speed=buff_speed
        self.better_start=better_start
        self.screen=screen
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
        if self.finish() and self.rank==0:
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
    def affect(self,x):
        self.type=random.randint(0,4)
        if self.type==0 or self.type==2:
            x-=100
            pygame.mixer.Channel(4).play(back_sound)
        elif self.type==1 or self.type==3:
            x+=100
            pygame.mixer.Channel(5).play(flash_sound)
        else:
            pass
            pygame.mixer.Channel(6).play(tele_sound)
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
def run_game(map_index,player_pic,com1_pic,com2_pic,com3_pic,com4_pic,buff_speed,better_start,user,player_name,screen):
    #Phát âm thanh
    pygame.mixer.Channel(3).play(car_sound,-1)
    #Khởi tạo xe 
    player=Car(screen,player_pic,2,buff_speed,better_start)
    com1=Car(screen,com1_pic,1)
    com2=Car(screen,com2_pic,3)
    com3=Car(screen,com3_pic,4)
    com4=Car(screen,com4_pic,5)

    #Set tên
    player.name = player_name
    com1.name = 'com'
    com2.name ='com'
    com3.name ='com'
    com4.name ='com'
    
    #Map
    bg=maps[map_index]
    
    #Khởi tạo biến item
    item1=Item()
    item2=Item()
    enough_item=False
    num_item=0
    #Các tham số
    if player.better_start: 
        player_x=start_bg+100
    else:
        player_x=start_bg
    if player.buff_speed:
        max_speed=25
    else:
        max_speed=20
    max_com=20
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

    #Vòng lặp game
    start=False
    while running:
        fpsClock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                start=True
        #Vẽ background
        screen.blit(bg,(bg_x,0))
        screen.blit(bg,(bg_x+1280,0))
        #Vẽ đường
        if road_time==0:
            screen.blit(start_road,(road_x,240))
            screen.blit(road,(road_x+1280,240))
        elif road_time>=10:
            screen.blit(finish_road,(road_x,240))
        else:
            screen.blit(road,(road_x,240))
            screen.blit(road,(road_x+1280,240))
        road_speed=5

        #Vẽ xe
        player.draw(player_x,player_rank)
        com1.draw(com1_x,com1_rank)
        com2.draw(com2_x,com2_rank)
        com3.draw(com3_x,com3_rank)
        com4.draw(com4_x,com4_rank)

        #Cho đường, background chạy
        if start:
            if not(road_finish):
                road_x-=road_speed
                if road_x<-1280:
                    road_x=0
                    road_time+=1
                if road_time==10:
                    road_finish=True
                bg_x-=1
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
            if road_finish:
                if not(player.finish()):
                    player_x+=random.randint(0,max_speed)
                    if player_x>1100:
                        player_x=1100
                if not(com1.finish()):
                    com1_x+=random.randint(0,max_com)
                    if com1_x>1100:
                        com1_x=1100
                if not(com2.finish()):
                    com2_x+=random.randint(0,max_com)
                    if com2_x>1100:
                        com2_x=1100
                if not(com3.finish()):
                    com3_x+=random.randint(0,max_com)
                    if com3_x>1100:
                        com3_x=1100
                if not(com4.finish()):
                    com4_x+=random.randint(0,max_com)
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
                        player_x=item1.affect(player_x)
                        num_item-=1
                        item1.exist=False
                    if com1.is_in(item1_x,item1_y):
                        com1_x=item1.affect(com1_x)
                        num_item-=1
                        item1.exist=False
                    if com2.is_in(item1_x,item1_y):
                        com2_x=item1.affect(com2_x)
                        num_item-=1
                        item1.exist=False
                    if com3.is_in(item1_x,item1_y):
                        com3_x=item1.affect(com3_x)
                        num_item-=1
                        item1.exist=False
                    if com4.is_in(item1_x,item1_y):
                        com4_x=item1.affect(com4_x)
                        num_item-=1
                        item1.exist=False
                
                #Tương tự với item 2
                if not(item2.exist):
                    lane_item2=random.randint(1,5)
                    item2_y=280+(lane_item2-1)*80
                    item2_x=random.randint(600,1000)
                    if item2_x<end_bg and item2_y!=item1_y:
                        item2.exist=True
                        num_item+=1
                if item2.exist:
                    item2.draw(item2_x,item2_y,screen)
                    item2_x-=road_speed
                    if item2_x<0:
                        item2.exist=False
                        num_item-=1

                    if player.is_in(item2_x-50,item2_y):
                        player_x=item2.affect(player_x)
                        num_item-=1
                        item2.exist=False
                    if com1.is_in(item2_x-50,item2_y):
                        com1_x=item2.affect(com1_x)
                        num_item-=1
                        item2.exist=False
                    if com2.is_in(item2_x-50,item2_y):
                        com2_x=item2.affect(com2_x)
                        num_item-=1
                        item2.exist=False
                    if com3.is_in(item2_x-50,item2_y):
                        com3_x=item2.affect(com3_x)
                        num_item-=1
                        item2.exist=False
                    if com4.is_in(item2_x-50,item2_y):
                        com4_x=item2.affect(com4_x)
                        num_item-=1
                        item2.exist=False
                
                #Nếu đã đủ 2 item -> không thêm item nữa
                if num_item>2:
                    enough_item=True
                else:
                    enough_item=False
        
            #Xếp hạng
            if player.check_ranked():
                player_rank=rank
                rank+=1
            if com1.check_ranked():
                com1_rank=rank
                rank+=1
            if com2.check_ranked():
                com2_rank=rank
                rank+=1
            if com3.check_ranked():
                com3_rank=rank
                rank+=1
            if com4.check_ranked():
                com4_rank=rank
                rank+=1
            
            #Kết thúc
            if (player.finish() and com1.finish() and com2.finish() and com3.finish() and com4.finish()) and road_finish:
                start=False
                ranked=True
            # bảng xếp hạng
        if ranked:
            check_rank = ranked_rs(r'MainGame\Image\item.png',screen_size[0]/2,4*screen_size[1]/5,player,com1,com2,com3,com4,user,screen)

        pygame.display.update()
        
        #thoát ra menu
        if check_rank ==False:
            break
    return player_rank
def shopping(screen,user,buff_speed,buff_start):
    #Khởi tạo nút
    buy_buff_speed=Buttons(200,100,item_pic,340,360,screen)
    buy_better_start=Buttons(200,100,buff_start_img,740,360,screen)
    quit_bt=Buttons(200,100,item_pic,540,570,screen)
    #Vòng lặp
    running_shop=True
    while running_shop:
        spot = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                new_screen_size = event.dict["size"]
                screen_resize(new_screen_size)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if buy_buff_speed.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    if not(buff_speed):
                        user.money_change(-2000)
                    buff_speed=True
                    buy_buff_speed.img=item_pic
                if buy_better_start.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    if not(buff_start):
                        user.money_change(-2000)
                    buff_start=True
                    buy_better_start.img=item_pic
                if quit_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    running_shop=False
            if buy_buff_speed.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif buy_better_start.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            elif quit_bt.is_in(spot[0],spot[1]):
                pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        if buff_speed:
            buy_buff_speed.img=car_pic1
        if buff_start:
            buy_better_start.img=pygame.transform.scale(buff_start_ed_img,(200,100))
        screen.fill(black)
        buy_better_start.draw()
        buy_buff_speed.draw()
        quit_bt.draw()
        pygame.display.update()
    return (buff_speed,buff_start)

def pick_map(buff_speed,buff_start,current_user,player_name,char,screen):
    pick_bt=Buttons(200,100,item_pic,540,570,screen)
    next_bt=Buttons(100,100,item_pic,980,340,screen)
    back_bt=Buttons(100,100,item_pic,200,340,screen)
    index=0
    run_map=True
    while run_map:
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
                    run_game(index,car_pic2,car_pic2,car_pic2,car_pic2,car_pic2,buff_speed,buff_start,current_user,player_name,screen)
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
        pick_bt.draw()
        next_bt.draw()
        back_bt.draw()
        screen.blit(pick_maps[index],(440,210))
        pygame.display.update()

def pick_char(screen,username):
    pick1=Buttons(200,200,item_pic,280,160,screen)
    pick2=Buttons(200,200,item_pic,540,160,screen)
    pick3=Buttons(200,200,item_pic,800,160,screen)
    pick4=Buttons(200,200,item_pic,410,400,screen)
    pick5=Buttons(200,200,item_pic,670,400,screen)
    return_bt=Buttons(150,150,item_pic,0,0,screen)
    accept=0
    index=0
    run_map=True
    while run_map:
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
            pick1.img=pygame.transform.scale(item_pic,(pick1.height,pick1.width))
            pick2.img=pygame.transform.scale(item_pic,(pick2.height,pick2.width))
            pick3.img=pygame.transform.scale(item_pic,(pick3.height,pick3.width))
            pick4.img=pygame.transform.scale(item_pic,(pick4.height,pick4.width))
            pick5.img=pygame.transform.scale(item_pic,(pick5.height,pick5.width))
        if index==1:
            pick1.img=car_pic1
            pick2.img=car_pic1
            pick3.img=car_pic1
            pick4.img=car_pic1
            pick5.img=car_pic1
        if index==2:
            pick1.img=car_pic1
            pick2.img=car_pic1
            pick3.img=car_pic1
            pick4.img=car_pic1
            pick5.img=car_pic1
        if index==3:
            pick1.img=car_pic1
            pick2.img=car_pic1
            pick3.img=car_pic1
            pick4.img=car_pic1
            pick5.img=car_pic1
        if index==4:
            pick1.img=car_pic1
            pick2.img=car_pic1
            pick3.img=car_pic1
            pick4.img=car_pic1
            pick5.img=car_pic1
        if index==5:
            pick1.img=car_pic1
            pick2.img=car_pic1
            pick3.img=car_pic1
            pick4.img=car_pic1
            pick5.img=car_pic1
        screen.fill(black)
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
    profile_bt = Buttons(200,100,item_pic,20,20,screen)
    start_bt=Buttons(200,100,start_bt_img,540,570,screen)
    shop_bt=Buttons(100,100,item_pic,50,570,screen)
    minigame_bt=Buttons(100,100,item_pic,50,310,screen)
    next_music_bt=Buttons(30,30,item_pic,1000,100,screen)
    back_music_bt=Buttons(30,30,item_pic,1050,100,screen)
    stop_music_bt=Buttons(30,30,item_pic,940,100,screen)

    #Nhạc
    ms_index=0
    is_play=False
    stop=False

    #Tham số của người chơi
    buff=(False,False)
    char=-1
    player_name='2'
    running_menu=True
    #Vòng lặp
    while running_menu:
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
                    running_menu=False
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    char=pick_char(screen,username)
                    if char>=0:
                        pick_map(buff[0],buff[1],current_user,player_name,char,screen)
                    running_menu=True
                #Nút shop
                if shop_bt.is_in(spot[0],spot[1]):
                    running_menu=False
                    #đổi lại hình dạng chuột ban đầu sau khi click
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    buff=shopping(screen,current_user,buff[0],buff[1])
                    running_menu=True
                #Nút show profile
                if profile_bt.is_in(spot[0],spot[1]):
                    running_menu=False
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    profile_display(current_user,screen)
                    running_menu=True
                #Nút minigame
                if minigame_bt.is_in(spot[0],spot[1]):
                    running_menu=False
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    score=snakeGame(screen)
                    current_user.money_change(score*100)
                    running_menu=True
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
                    musics[ms_index].stop()
                    stop=True
                elif stop_music_bt.is_in(spot[0],spot[1]) and stop:
                    musics[ms_index].play()
                    stop=False


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
            else:
                pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        screen.fill(black)
        #Vẽ nút
        profile_bt.draw()
        shop_bt.draw()
        start_bt.draw()
        minigame_bt.draw()
        next_music_bt.draw()
        back_music_bt.draw()
        stop_music_bt.draw()
        #Phát nhạc
        if not(is_play) and not(stop):
            musics[ms_index].play()
            is_play=True
        #Tên Nhạc
        draw_text(musics[ms_index].name,ms_font,white,screen,1040,75)
        pygame.display.update()

def ranked_rs(image,width,height,player,com1,com2,com3,com4,user,screen):
    rank_img = pygame.transform.scale(pygame.image.load(image),(width,height))
    rank_rect = rank_img.get_rect(topleft=(screen_size[0]/4,screen_size[1]/10))
    running_rank = True
    home_bt = Buttons(screen_size[0]/16,screen_size[1]/8,item_pic,screen_size[0]/4,9*screen_size[1]/10,screen)
    save_bt = Buttons(screen_size[0]/16,screen_size[1]/8,item_pic,3*screen_size[0]/4,9*screen_size[1]/10,screen)
    lt = [player,com1,com2,com3,com4]
    #Cập nhật tiền 
    user.money_update(player)
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
        spot=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
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


        screen.blit(rank_img,rank_rect)
        #vẽ nút
        home_bt.draw()
        save_bt.draw()
        draw_text('1',new_font,black,screen,screen_size[0]/4+screen_size[0]/40,3*screen_size[1]/20)
        draw_text('2',new_font,black,screen,screen_size[0]/4+screen_size[0]/40,6*screen_size[1]/20)
        draw_text('3',new_font,black,screen,screen_size[0]/4+screen_size[0]/40,9*screen_size[1]/20)
        draw_text('4',new_font,black,screen,screen_size[0]/4+screen_size[0]/40,12*screen_size[1]/20)
        draw_text('5',new_font,black,screen,screen_size[0]/4+screen_size[0]/40,15*screen_size[1]/20)
        draw_text(lt[0].name,new_font,lt[0].color,screen,screen_size[0]/4+screen_size[0]/5,3*screen_size[1]/20)
        draw_text(lt[1].name,new_font,lt[1].color,screen,screen_size[0]/4+screen_size[0]/5,6*screen_size[1]/20)
        draw_text(lt[2].name,new_font,lt[2].color,screen,screen_size[0]/4+screen_size[0]/5,9*screen_size[1]/20)
        draw_text(lt[3].name,new_font,lt[3].color,screen,screen_size[0]/4+screen_size[0]/5,12*screen_size[1]/20)
        draw_text(lt[4].name,new_font,lt[4].color,screen,screen_size[0]/4+screen_size[0]/5,15*screen_size[1]/20)
        pygame.display.flip()
    return False

def profile_display(user,screen):
    run = True
    return_bt = Buttons(screen_size[0]/24,screen_size[0]/24,item_pic,23*screen_size[0]/24,screen_size[1]-screen_size[0]/24,screen)
    while run:
        spot=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == MOUSEBUTTONDOWN:
                if return_bt.is_in(spot[0],spot[1]):
                    pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                    run = False
        if return_bt.is_in(spot[0],spot[1]):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
    #vẽ màn hình, nút
        screen.fill((0,0,0))
        return_bt.draw()
        draw_text('username:'+user.username,font,white,screen,screen_size[0]/4,screen_size[1]/4)
        draw_text('Money:'+str(user.money),font,white,screen,screen_size[0]/4,screen_size[1]/3)
        pygame.display.flip()

def login():
    # Tạo cửa sổ đăng nhập
    root = Tk()
    root.title("Đăng nhập")

    # Tạo các label và entry cho tên đăng nhập và mật khẩu
    tk.Label(root, text="Tên đăng nhập").grid(row=0, column=0)
    username_entry = tk.Entry(root)
    username_entry.grid(row=1, column=0)

    tk.Label(root, text="Mật khẩu").grid(row=2, column=0)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=3, column=0)

    # Tạo hàm kiểm tra tên đăng nhập và mật khẩu    
    def check_login():
        # Mở file accounts.txt và đọc tất cả các tài khoản
        with open("accounts.txt", "r") as f:
            accounts = f.readlines()

        # Kiểm tra tên đăng nhập và mật khẩu có trong file accounts.txt hay không
        for account in accounts:
            username, password = account.strip().split(":")
            if username == username_entry.get() and password == password_entry.get():
            #chuyển màn hình chỗ này
                root.destroy()        
                main_menu(username)
            else:
                messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")
                

    # Tạo nút đăng nhập và nút thoát
    tk.Button(root, text="Đăng nhập", command=check_login).grid(row=4, column=0)

    # Chạy chương trình
    root.mainloop()

def register():
    root = Tk()
    root.title("Đăng ký tài khoản")

    label_username = Label(root, text="Tên đăng nhập:")
    label_username.pack()
    entry_username = Entry(root)
    entry_username.pack()

    label_password = Label(root, text="Mật khẩu:")
    label_password.pack()
    entry_password = Entry(root, show="*")
    entry_password.pack()

    button_register = Button(root, text="Đăng ký")
    button_login = Button(root, text="Đăng nhập")

    def check_register():
        username = entry_username.get()
        password = entry_password.get()
    # Kiểm tra xem tên đăng nhập và mật khẩu có hợp lệ không
        if len(username) == 0 or len(password) == 0:
            messagebox.showerror("Lỗi", "Vui lòng nhập tên đăng nhập và mật khẩu.")
        else:
            # Lưu tài khoản vào file accounts.txt
            with open("accounts.txt", "a") as file:
                file.write(f"{username}:{password}\n")
            messagebox.showinfo("Thông báo", "Đăng ký thành công.")
    button_register.config(command=check_register)
    button_register.pack()
    def turn_to_login():
        root.destroy()
        login()
    #khúc này tui tạo button đăng nhập, ông chuyển màn hình khúc này
    button_login.config(command=turn_to_login)
    button_login.pack()
    root.mainloop()

    if __name__ == "__main__":
        root.mainloop()
register()