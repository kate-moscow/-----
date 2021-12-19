import os
import random
import pygame
import unittest

class set_bomb(unittest.TestCase):
    def test_set_bomb_1(self):
        W=4
        pole=[]
        for i in range (W):
            a=[0]*W
            pole.append(a)
        bomb_count= count= 2
        bomb=1
        O=0
        while count>0:
            q=random.randint(0,W-1)
            p=random.randint(0,W-1)
            if pole[q][p] != bomb:
                pole[q][p] = bomb
                count=count-1

        for i in range (W):
            for j in range(W):
                if pole [i][j] == bomb:
                    O+=1

        self.assertEqual(O,bomb_count)

    def test_set_bomb_2(self):
        W=14
        pole=[]
        for i in range (W):
            a=[0]*W
            pole.append(a)
        bomb_count=count= 19
        bomb=1
        O=0
        while count>0:
            q=random.randint(0,W-1)
            p=random.randint(0,W-1)
            if pole[q][p] != bomb:
                pole[q][p] = bomb
                count=count-1

        for i in range (W):
            for j in range(W):
                if pole [i][j] == bomb:
                    O+=1

        self.assertEqual(O,bomb_count)

    def test_set_bomb_3(self):
        W=22
        pole=[]
        for i in range (W):
            a=[0]*W
            pole.append(a)
        bomb_count=count= 99
        bomb=1
        O=0
        while count>0:
            q=random.randint(0,W-1)
            p=random.randint(0,W-1)
            if pole[q][p] != bomb:
                pole[q][p] = bomb
                count=count-1

        for i in range (W):
            for j in range(W):
                if pole [i][j] == bomb:
                    O+=1

        self.assertEqual(O,bomb_count)

class check_open(unittest.TestCase):
    def test_check_open_1(self):
        queue=[]
        X=0
        Y=0
        W=8
        otkrito=1
        empty=0
        pole=   [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 3, 3, 3, 0, 0, 0, 0],
                [0, 3, 2, 3, 0, 3, 3, 3],
                [0, 3, 2, 3, 3, 3, 2, 3],
                [0, 3, 3, 2, 3, 3, 3, 2],
                [0, 0, 3, 3, 3, 0, 3, 3]]

        pole2=  [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 3, 3, 3, 1, 1, 1, 1],
                [1, 3, 2, 3, 1, 3, 3, 3],
                [1, 3, 2, 3, 3, 3, 2, 3],
                [1, 3, 3, 2, 3, 3, 3, 2],
                [1, 1, 3, 3, 3, 0, 3, 3]]
        queue.append([X,Y])
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
       
        self.assertEqual(pole,pole2)
        
    def test_check_open_2(self):
        queue=[]
        X=4
        Y=4
        W=5
        otkrito=1
        empty=0
        pole=   [[3, 2, 3, 3, 2],
                [3, 2, 3, 3, 3],
                [3, 3, 3, 0, 0],
                [0, 3, 3, 3, 0],
                [0, 3, 2, 3, 0]]

        pole2=  [[3, 2, 3, 3, 2],
                [3, 2, 3, 3, 3],
                [3, 3, 3, 1, 1],
                [0, 3, 3, 3, 1],
                [0, 3, 2, 3, 1]]

        queue.append([X,Y])
        pole [X][Y]=otkrito
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
       
        self.assertEqual(pole,pole2)

class check_close(unittest.TestCase):
    def test_check_close_1(self):
        W=10
        close=3
        opclose =2
        bomb=2
        otkrito=1
        field=  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        pole =      [[1, 1, 1, 3, 3, 3, 1, 1, 1, 1],
                    [1, 1, 1, 3, 2, 3, 1, 1, 1, 1],
                    [1, 1, 1, 3, 3, 3, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 3, 3, 3, 1, 1, 1, 1], 
                    [1, 1, 1, 3, 2, 3, 1, 1, 1, 1], 
                    [1, 3, 3, 3, 3, 3, 1, 3, 3, 3],
                    [1, 3, 2, 3, 3, 3, 3, 3, 2, 3],
                    [1, 3, 2, 3, 3, 2, 3, 3, 3, 3], 
                    [1, 3, 2, 3, 3, 3, 3, 0, 0, 0]]

        field2 =    [[0, 0, 0, 11, 0, 11, 0, 0, 0, 0],
                    [0, 0, 0, 11, 0, 11, 0, 0, 0, 0],
                    [0, 2, 0, 11, 11, 11, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 11, 11, 11, 0, 0, 0, 0],
                    [0, 0, 0, 11, 0, 11, 0, 0, 0, 0], 
                    [0, 11, 11, 12, 0, 11, 0, 11, 11, 11], 
                    [0, 12, 0, 0, 0, 11, 11, 11, 0, 0], 
                    [0, 13, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 12, 0, 0, 0, 0, 0, 0, 0, 0]]

        k=0
        c=0
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
        self.assertEqual(field,field2)


    

if __name__ == "__main__":
    unittest.main() 