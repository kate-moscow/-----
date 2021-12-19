import os
import random
import pygame

pygame.init ()
queue=[]
pole=[]
field=[]
bomb_count=7
empty=0
otkrito=1
bomb=opclose =2
close=3
size= (615,615)
kontur = 6
W=10

pygame.display.set_caption("Saper")
okno= pygame.display.set_mode(size)
time= pygame.time.Clock()
cl1=pygame.image.load(os.path.join("blocks","op1.png"))
cl2=pygame.image.load(os.path.join("blocks","op2.png"))
cl3=pygame.image.load(os.path.join("blocks","op3.png"))
cl4=pygame.image.load(os.path.join("blocks","op4.png"))
cl5=pygame.image.load(os.path.join("blocks","op5.png"))
cl6=pygame.image.load(os.path.join("blocks","op6.png"))
cl7=pygame.image.load(os.path.join("blocks","op7.png"))
cl8=pygame.image.load(os.path.join("blocks","op8.png"))
openn=pygame.image.load(os.path.join("blocks","open.png"))
closee=pygame.image.load(os.path.join("blocks","close.png"))

scale_open= pygame.transform.scale(openn,(30,30))
scale_close = pygame.transform.scale(closee,(30,30))
scale_cl1 = pygame.transform.scale(cl1,(30,30))
scale_cl2 = pygame.transform.scale(cl2,(30,30))
scale_cl3 = pygame.transform.scale(cl3,(30,30))
scale_cl4 = pygame.transform.scale(cl4,(30,30))
scale_cl5 = pygame.transform.scale(cl5,(30,30))
scale_cl6 = pygame.transform.scale(cl6,(30,30))
scale_cl7 = pygame.transform.scale(cl7,(30,30))
scale_cl8 = pygame.transform.scale(cl8,(30,30))
closes=[scale_cl1,scale_cl2,scale_cl3,scale_cl4,scale_cl5,scale_cl6,scale_cl7,scale_cl8]

def set_bomb (bomb_count):
    ''' Принимает на вход bomb_count, переменную которая обозначает количество бомб на полею. Функция создает бомбы и
    области, которые помечают, что что бомба где-то рядом. Функция получает на вход количество бомб и создает цикл в котором присваевает
    нужному количеству бомб случайные координаты, после этого вокруг этого места выделяется область, обозначающая, что бомба рядом. после
    всех действий функция выводит измененное поле'''
    while bomb_count>0:
        q=random.randint(0,W-1)
        p=random.randint(0,W-1)
        if pole[q][p] != bomb:
            pole[q][p] = bomb
            bomb_count=bomb_count-1
            for i in range (3):
                for j in range(3):
                    l=q-i+1
                    n=p-j+1
                    if  l>=0 and n>=0 and l<W and n<W:
                        if  pole[l][n]!=bomb:
                            pole[l][n]=close
    return pole

def check_open ():
    ''' Функция основанная на очереди. перед ней в коде стол первый параметр, который войдет в эту очень и запустит цикл проверки соседей клетки на
    наличие соседей среди еще закрытых клеток. Если сосед будет найден то он будут добавлен в очередь для последующей проверки и будет добавлен на
    игровое поле как открытая ячейка. Очередь будет работать пока соседи не закончатся. В конце функция выводит обновленное поле'''
    while queue:
        X,Y= queue[0]
        queue.pop(0)
        if (X-1>=0 and X-1<W) and (Y>=0 and Y<W) and pole[X-1][Y]==empty:
            queue.append([X-1,Y])
            pole[X-1][Y] =otkrito

        if (X+1>=0 and X+1<W) and (Y>=0 and Y<W) and pole[X+1][Y]==empty:
            queue.append([X+1,Y])
            pole[X+1][Y] =otkrito

        if (X>=0 and X<W) and (Y-1>=0 and Y-1<W) and pole[X][Y-1]==empty:
            queue.append([X,Y-1])
            pole[X][Y-1] =otkrito

        if (X>=0 and X<W) and (Y+1>=0 and Y+1<W) and pole[X][Y+1]==empty:
            queue.append([X,Y+1])
            pole[X][Y+1] =otkrito
    return pole

def check_close():
    '''Функция определяет количество бомб в клетках рядом с бомбой и запоминает его в отдельном поле (field), после чего проверяет есть ли рядом с этой 
    клеткой открытое поле и  если оно есть, то это запоминается в отдельном поле (field). Функция возвращает измененное  поле (field)'''
    k=0
    c=0
    print (field)
    print (pole)
    for X in range (W):
        for Y in range(W):
            if pole[X][Y]==close or field[X][Y]==opclose :
                for i in range (3):
                    for j in range(3):
                        l=X-i+1
                        n=Y-j+1
                        if  l>=0 and n>=0 and l<W and n<W and pole[l][n]==bomb:
                            k+=1
                        elif l>=0 and n>=0 and l<W and n<W and pole[l][n]==otkrito:
                            c+=1
                if k!=0 and c!=0:
                    field[X][Y]=10+k
                k=0  
                c=0
    print (field)
    return field  

def run():
    '''Функция содержит бесконечный цикл, который позволяет команде работать почти постоянно. 
    1 мы проверяем события. если они случаться, то событие QUIT позволит нам закрыть окно, а  MOUSEBUTTONDOWN понять, когда нажимаются кнопки мЫшы
    2 позволяет постоянно отрисовывать поле'''
    set_bomb(bomb_count)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                col = x_mouse //(kontur+W)
                row= y_mouse//(kontur+W)
                if event.button == 1 :
                    if (pole [row][col]==empty or pole [row][col]==close) and (field [row][col]>18 or field [row][col]<11) :
                        pole [row][col]=otkrito
                        field[row][col]=opclose
                        queue.append([row,col])
                        queue.append([row,col])
                        check_open()
                        check_close()
                    elif pole [row][col]==bomb :
                        pygame.quit()

        for row in range (W):
            for col in range (W):
                x = col * W +(col)*kontur 
                y = row * W +(row)*kontur 
                if  pole[row][col]==empty or pole[row][col]==bomb or pole[row][col]==close:
                    okno.blit(scale_close,[x,y])
                elif pole[row][col]==otkrito:
                    okno.blit(scale_open,[x,y])
                if field [row][col]<=18 and field [row][col]>=11:
                    k=(field[row][col])%10 -1
                    okno.blit(closes[k],[x,y])

        pygame.display.flip()
        time.tick(60)

for i in range (W):
    a=[0]*W
    pole.append(a)
for i in range (W):
    a=[0]*W
    field.append(a)
run()




