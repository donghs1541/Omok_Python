# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:37:40 2020
Maker : bychoi@deu.ac.kr 

@author: Com
"""

# sample player file which must be made by student 

from player import *
from stone import *
from random import *

class iot12345_student(player):
     def __init__(self, clr):
          super().__init__( clr)  # call constructor of super class
          self.__max_x= 9
          self.__max_y= 9
       
     
        
     def __del__(self):  # destructor
         pass


     def ai_calculate(self,board):
        score = 0   # ai가 돌상태를 수치화 했을 때의 값
        total_score = 0   # ai가 오목보드상태를 수치화 했을 때의 값
        enemy = -1
        team = 1
        stone = []
        for i in range(0,22):
            stone.append([])
            for j in range(0,22):
                try:
                    stone[i].append(board[i][j])
                except:
                    stone[i].append(3)

        for i in range(0, 19):
            for k in range(0, 19):
                ####/가로####/
                if (stone[i][k - 2] ==  team and stone[i][k - 1] ==  team and stone[i][k] ==  team and stone[i][k + 1] ==  team and
                        stone[i][k + 2] ==  team):
                    score = 990000 
                    total_score = total_score + score 
                # ooooo 승리시
                if (stone[i][k - 2] ==  team and stone[i][k - 1] ==  team and stone[i][k] ==  team and stone[i][
                    k + 1] ==  team and stone[i][k + 2] == 0):
                    score = 50 
                    total_score = total_score + score 
                # oooo 4개 연속
                if (stone[i][k - 2] ==  team and stone[i][k - 1] ==  team and stone[i][k] ==  team and stone[i][
                    k + 1] ==  team and stone[i][k + 2] ==  enemy):
                    score = 40 
                    total_score = total_score + score 
                # oooox 4개 연속 막힘
                if (stone[i][k - 2] ==  enemy and stone[i][k - 1] ==  team and stone[i][k] ==  team and stone[i][k + 1] ==  team and
                      stone[i][k + 2] ==  team):
                    score = 40 
                    total_score = total_score + score 
                # xoooo 4개 연속 막힘
                if (stone[i][k - 2] == 0 and stone[i][k - 1] ==  team and stone[i][k] ==  team and stone[i][k + 1] ==  team and
                      stone[i][k + 2] == 0):
                    score = 6 
                    total_score = total_score + score 
                # ooo 3개 연속
                if (stone[i][k - 2] == 0 and stone[i][k - 1] ==  team and stone[i][k] ==  team and stone[i][k + 1] ==  team and
                      stone[i][k + 2] ==  enemy):
                    score = 4 
                    total_score = total_score + score 
                # ooox 3개 연속 막힘
                if (stone[i][k - 2] ==  enemy and stone[i][k - 1] ==  team and stone[i][k] ==  team and stone[i][k + 1] ==  team and
                      stone[i][k + 2] == 0):
                    score = 4 
                    total_score = total_score + score 
                # xooo 3개 연속 막힘
                if (stone[i][k - 1] == 0 and stone[i][k] ==  team and stone[i][k + 1] ==  team and stone[i][k + 2] == 0):
                    score = 2 
                    total_score = total_score + score 
                # oo 2개 연속
                if (stone[i][k - 1] == 0 and stone[i][k] ==  team and stone[i][k + 1] ==  team and stone[i][k + 2] ==  enemy):
                    score = 1 
                    total_score = total_score + score 
                # oox 2개 연속 막힘
                if (stone[i][k - 1] ==  enemy and stone[i][k] ==  team and stone[i][k + 1] ==  team and stone[i][k + 2] == 0):
                    score = 1 
                    total_score = total_score + score 
                # xoo 2개 연속 막힘

                ####/세로####/
                if (stone[i - 2][k] ==  team and stone[i - 1][k] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k] ==  team and stone[i + 2][k] ==  team):
                    score = 990000 
                    total_score = total_score + score 
                # ooooo 승리시
                if (stone[i - 2][k] ==  team and stone[i - 1][k] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k] ==  team and stone[i + 2][k] == 0):
                    score = 50 
                    total_score = total_score + score 
                # oooo 4개 연속
                if (stone[i - 2][k] ==  team and stone[i - 1][k] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k] ==  team and stone[i + 2][k] ==  enemy):
                    score = 40 
                    total_score = total_score + score 
                # oooox 4개 연속 막힘
                if (stone[i - 2][k] ==  enemy and stone[i - 1][k] ==  team and stone[i][k] ==  team and stone[i + 1][k] ==  team and
                      stone[i + 2][k] ==  team):
                    score = 40 
                    total_score = total_score + score 
                # xoooo 4개 연속 막힘
                if (stone[i - 2][k] == 0 and stone[i - 1][k] ==  team and stone[i][k] ==  team and stone[i + 1][k] ==  team and
                      stone[i + 2][k] == 0):
                    score = 6 
                    total_score = total_score + score 
                # ooo 3개 연속
                if (stone[i - 2][k] == 0 and stone[i - 1][k] ==  team and stone[i][k] ==  team and stone[i + 1][k] ==  team and
                      stone[i + 2][k] ==  enemy):
                    score = 4 
                    total_score = total_score + score 
                # ooox 3개 연속 막힘
                if (stone[i - 2][k] ==  enemy and stone[i - 1][k] ==  team and stone[i][k] ==  team and stone[i + 1][k] ==  team and
                      stone[i + 2][k] == 0):
                    score = 4 
                    total_score = total_score + score 
                # xooo 3개 연속 막힘
                if (stone[i - 1][k] == 0 and stone[i][k] ==  team and stone[i + 1][k] ==  team and stone[i + 2][k] == 0):
                    score = 2 
                    total_score = total_score + score 
                # oo 2개 연속
                if (stone[i - 1][k] == 0 and stone[i][k] ==  team and stone[i + 1][k] ==  team and stone[i + 2][k] ==  enemy):
                    score = 1 
                    total_score = total_score + score 
                # oox 2개 연속 막힘
                if (stone[i - 1][k] ==  enemy and stone[i][k] ==  team and stone[i + 1][k] ==  team and stone[i + 2][k] == 0):
                    score = 1 
                    total_score = total_score + score 
                # xoo 2개 연속 막힘

                ####/대각선####/
                if (stone[i - 2][k + 2] ==  team and stone[i - 1][k + 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] ==  team):
                    score = 990000 
                    total_score = total_score + score 
                # ooooo 승리시
                if (stone[i - 2][k + 2] ==  team and stone[i - 1][k + 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] == 0):
                    score = 50 
                    total_score = total_score + score 
                # oooo 4개 연속
                if (stone[i - 2][k + 2] ==  team and stone[i - 1][k + 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] ==  enemy):
                    score = 40 
                    total_score = total_score + score 
                # oooox 4개 연속 막힘
                if (stone[i - 2][k + 2] ==  enemy and stone[i - 1][k + 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] ==  team):
                    score = 40 
                    total_score = total_score + score 
                # xoooo 4개 연속 막힘
                if (stone[i - 2][k + 2] == 0 and stone[i - 1][k + 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] == 0):
                    score = 7 
                    total_score = total_score + score 
                # ooo 3개 연속
                if (stone[i - 2][k + 2] == 0 and stone[i - 1][k + 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] ==  enemy):
                    score = 5 
                    total_score = total_score + score 
                # ooox 3개 연속 막힘
                if (stone[i - 2][k + 2] ==  enemy and stone[i - 1][k + 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] == 0):
                    score = 5 
                    total_score = total_score + score 
                # xooo 3개 연속 막힘
                if (stone[i - 1][k + 1] == 0 and stone[i][k] ==  team and stone[i + 1][k - 1] ==  team and stone[i + 2][
                    k - 2] == 0):
                    score = 3 
                    total_score = total_score + score 
                # oo 2개 연속
                if (stone[i - 1][k + 1] == 0 and stone[i][k] ==  team and stone[i + 1][k - 1] ==  team and stone[i + 2][
                    k - 2] ==  enemy):
                    score = 1 
                    total_score = total_score + score 
                # oox 2개 연속 막힘
                if (stone[i - 1][k + 1] ==  enemy and stone[i][k] ==  team and stone[i + 1][k - 1] ==  team and stone[i + 2][
                    k - 2] == 0):
                    score = 1 
                    total_score = total_score + score 
                # xoo 2개 연속 막힘

                ####/반대 대각선####/
                if (stone[i - 2][k - 2] ==  team and stone[i - 1][k - 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] ==  team):
                    score = 990000 
                    total_score = total_score + score 
                # ooooo 승리시
                if (stone[i - 2][k - 2] ==  team and stone[i - 1][k - 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] == 0):
                    score = 50 
                    total_score = total_score + score 
                # oooo 4개 연속
                if (stone[i - 2][k - 2] ==  team and stone[i - 1][k - 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] ==  enemy):
                    score = 40 
                    total_score = total_score + score 
                # oooox 4개 연속 막힘
                if (stone[i - 2][k - 2] ==  enemy and stone[i - 1][k - 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] ==  team):
                    score = 40 
                    total_score = total_score + score 
                # xoooo 4개 연속 막힘
                if (stone[i - 2][k - 2] == 0 and stone[i - 1][k - 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] == 0):
                    score = 7 
                    total_score = total_score + score 
                # ooo 3개 연속
                if (stone[i - 2][k - 2] == 0 and stone[i - 1][k - 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] ==  enemy):
                    score = 5 
                    total_score = total_score + score 
                # ooox 3개 연속 막힘
                if (stone[i - 2][k - 2] ==  enemy and stone[i - 1][k - 1] ==  team and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] == 0):
                    score = 5 
                    total_score = total_score + score 
                # xooo 3개 연속 막힘
                if (stone[i - 1][k - 1] == 0 and stone[i][k] ==  team and stone[i + 1][k + 1] ==  team and stone[i + 2][
                    k + 2] == 0):
                    score = 3 
                    total_score = total_score + score 
                # oo 2개 연속
                if (stone[i - 1][k - 1] == 0 and stone[i][k] ==  team and stone[i + 1][k + 1] ==  team and stone[i + 2][
                    k + 2] ==  enemy):
                    score = 1 
                    total_score = total_score + score 
                # oox 2개 연속 막힘
                if (stone[i - 1][k - 1] ==  enemy and stone[i][k] ==  team and stone[i + 1][k + 1] ==  team and stone[i + 2][
                    k + 2] == 0):
                    score = 1 
                    total_score = total_score + score 
                # xoo 2개 연속 막힘

                ####/수비!!####/
                if (stone[i][k - 4] ==  enemy and stone[i][k - 2] ==  enemy and stone[i][k-3] ==  enemy and stone[i][k -1] ==  enemy and
                      stone[i][k] ==  team):
                    score = 1000
                    total_score = total_score + score
                if (stone[i][k - 2] ==  enemy and stone[i][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i][k + 1] ==  enemy and
                      stone[i][k + 2] ==  team):
                    score = 1000
                    total_score = total_score + score 
                # oooox 가로 수비시
                if (stone[i][k - 2] ==  team and stone[i][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i][k + 1] ==  enemy and
                      stone[i][k + 2] ==  enemy):
                    score = 1000
                    total_score = total_score + score 
                # xoooo 가로 수비시
                if (stone[i - 2][k] ==  enemy and stone[i - 1][k] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][k] ==  enemy and
                      stone[i + 2][k] ==  team):
                    score = 1000 
                    total_score = total_score + score 
                # oooox 세로 수비시
                if (stone[i - 2][k] ==  team and stone[i - 1][k] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][k] ==  enemy and
                      stone[i + 2][k] ==  enemy):
                    score = 1000 
                    total_score = total_score + score 
                # xoooo 세로 수비시
                if (stone[i - 2][k - 2] ==  enemy and stone[i - 1][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k + 1] ==  enemy and stone[i + 2][k + 2] ==  team):
                    score = 1000 
                    total_score = total_score + score 
                # oooox 반대 대각선 수비시
                if (stone[i - 2][k - 2] ==  team and stone[i - 1][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k + 1] ==  enemy and stone[i + 2][k + 2] ==  enemy):
                    score = 1000 
                    total_score = total_score + score 
                # xoooo 반대 대각선 수비시
                if (stone[i - 2][k + 2] ==  enemy and stone[i - 1][k + 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k - 1] ==  enemy and stone[i + 2][k - 2] ==  team):
                    score = 1000 
                    total_score = total_score + score 
                # oooox 대각선 수비시
                if (stone[i - 2][k + 2] ==  team and stone[i - 1][k + 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k - 1] ==  enemy and stone[i + 2][k - 2] ==  enemy):
                    score = 1000 
                    total_score = total_score + score 
                # xoooo 대각선 수비시

                if (stone[i][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i][k + 1] ==  enemy and stone[i][k + 2] ==  team):
                    if (stone[i][k - 2] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 30 

                    total_score = total_score + score
                # ooox 가로 수비시
                if (stone[i][k - 2] ==  team and stone[i][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i][k + 1] ==  enemy):
                    if (stone[i][k + 2] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 250

                    total_score = total_score + score
                # xooo 가로 수비시
                if (stone[i - 1][k] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][k] ==  enemy and stone[i + 2][k] ==  team):
                    if (stone[i - 2][k] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 250

                    total_score = total_score + score 
                # ooox 세로 수비시
                if (stone[i - 2][k] ==  team and stone[i - 1][k] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][k] ==  enemy):
                    if (stone[i + 2][k] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 250

                    total_score = total_score + score 
                # xooo 세로 수비시
                if (stone[i - 1][k + 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][k - 1] ==  enemy and stone[i + 2][
                    k - 2] ==  team):
                    if (stone[i - 2][k + 2] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 250

                    total_score = total_score + score 
                # ooox 대각선 수비시
                if (stone[i - 2][k + 2] ==  team and stone[i - 1][k + 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k - 1] ==  enemy):
                    if (stone[i + 2][k - 2] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 250

                    total_score = total_score + score 
                # xooo 대각선 수비시
                if (stone[i - 1][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][k + 1] ==  enemy and stone[i + 2][
                    k + 2] ==  team):
                    if (stone[i - 2][k - 2] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 250

                    total_score = total_score + score 
                # ooox 반대 대각선 수비시
                if (stone[i - 2][k - 2] ==  team and stone[i - 1][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k + 1] ==  enemy):
                    if (stone[i + 2][k + 2] ==  team):
                        score = 3   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        score = 250

                    total_score = total_score + score 
                # xooo 반대 대각선 수비시

        return total_score

     '''
         if (stone[i][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i][k + 1] ==  enemy and stone[i][k + 2] == 0 and stone[i][k-2] == 0):  # ooo 수비
             score = 400
             total_score = total_score + score
         if (stone[i-1][k] ==  enemy and stone[i][k] ==  enemy and stone[i+1][k] ==  enemy and stone[i+2][k] == 0 and stone[i-2][k] == 0):
             score = 400
             total_score = total_score + score
         if (stone[i-1][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i+1][k + 1] ==  enemy and stone[i+2][k + 2] == 0 and stone[i-2][k-2] == 0): #대각선
             score = 400
             total_score = total_score + score
         if (stone[i-1][k +1] ==  enemy and stone[i][k] ==  enemy and stone[i+1][k -1] ==  enemy and stone[i+2][k -2] == 0 and stone[i-2][k+2] == 0):
             score = 400
             total_score = total_score + score
     '''

     def next(self, board,length):  # override
             print (" **** White player : My Turns **** ")

             stn = stone(self._color)
             temp = 0   # 수치화된 오목보드의 상태를 잠시 저장하는 변수
             AI = 0
             count = 0
             for i in range(0, 19):
                 for k in range(0, 19):
                     if(board[i][k] == -1):
                         count = count +1
                     if (board[i][k] == 0):
                         board[i][k] = 1  # stone함수의 값이 0(돌이 없는 상태)일때 임의의 돌을 삽입

                         AI = self.ai_calculate(board)  # 그 결과 얼마나 유리한 수 인지 수치값으로 반환
                         if (temp <AI):  # temp에는 이전의 수치값 저장! , 이전의 수치값보다 좋은 수 일때

                             temp = AI
                             self.__max_x = i
                             self.__max_y=  k
                         board[i][k] = 0 
             if count == 1:
                 self.__max_x = self.__max_x+1
             print("white:",AI)

             stn.setX(self.__max_x)
             stn.setY(self.__max_y)
             return stn
        
     def check33(self,stone,i,k):
        count =0
        if (i - 4 >= 0 and i + 4 < 19 and k - 4 >= 0 and k + 4 < 19):
            if ((stone[i][k - 3] == 0 and stone[i][k - 2] == -1 and stone[i][
                k - 1] == -1 and stone[
                     i][k + 1] == 0) or
                    (stone[i][k - 2] == 0 and stone[i][k - 1] == -1 and stone[i][
                        k + 1] == -1 and stone[
                         i][k + 2] == 0) or
                    (stone[i][k - 1] == 0 and stone[i][k + 1] == -1 and stone[i][
                        k + 2] == -1 and stone[
                         i][k + 3] == 0) or
                    (stone[i][k - 4] == 0 and stone[i][k - 3] == -1 and stone[i][
                        k - 2] == -1 and stone[
                         i][k - 1] == 0 and stone[i][k + 1] == 0) or
                    (stone[i][k + 4] == 0 and stone[i][k + 3] == -1 and stone[i][
                        k + 2] == -1 and stone[
                         i][k + 1] == 0 and stone[i][k - 1] == 0) or
                    (stone[i][k - 2] == 0 and stone[i][k - 1] == -1 and stone[i][
                        k + 1] == 0 and stone[
                         i][k + 2] == -1 and stone[i][k + 3] == 0) or
                    (stone[i][k + 2] == 0 and stone[i][k + 1] == -1 and stone[i][
                        k - 1] == 0 and stone[
                         i][k - 2] == -1 and stone[i][k - 3] == 0)):
                count = count +1

            if ((stone[i - 3][k] == 0 and stone[i - 2][k] == -1 and stone[i - 1][
                k] == -1 and stone[
                     i + 1][k] == 0) or
                    (stone[i - 2][k] == 0 and stone[i - 1][k] == -1 and stone[i + 1][
                        k] == -1 and stone[
                         i + 2][k] == 0) or
                    (stone[i - 1][k] == 0 and stone[i + 1][k] == -1 and stone[i + 2][
                        k] == -1 and stone[
                         i + 3][k] == 0) or
                    (stone[i - 4][k] == 0 and stone[i - 3][k] == -1 and stone[i - 2][
                        k] == -1 and stone[
                         i - 1][k] == 0 and stone[i + 1][k] == 0) or
                    (stone[i + 4][k] == 0 and stone[i + 3][k] == -1 and stone[i + 2][
                        k] == -1 and stone[
                         i + 1][k] == 0 and stone[i - 1][k] == 0) or
                    (stone[i - 2][k] == 0 and stone[i - 1][k] == -1 and stone[i + 1][
                        k] == 0 and stone[
                         i + 2][k] == -1 and stone[i + 3][k] == 0) or
                    (stone[i + 2][k] == 0 and stone[i + 1][k] == -1 and stone[i - 1][
                        k] == 0 and stone[
                         i - 2][k] == -1 and stone[i - 3][k] == 0)):
                count = count +1

            if ((stone[i - 3][k - 3] == 0 and stone[i - 2][k - 2] == -1 and stone[i - 1][
                k - 1] == -1 and stone[
                     i + 1][k + 1] == 0) or
                    (stone[i - 2][k - 2] == 0 and stone[i - 1][k - 1] == -1 and stone[
                        i + 1][k + 1] == -1 and stone[i + 2][k + 2] == 0) or
                    (stone[i - 1][k - 1] == 0 and stone[i + 1][k + 1] == -1 and stone[
                        i + 2][k + 2] == -1 and stone[i + 3][k + 3] == 0) or
                    (stone[i - 3][k - 3] == 0 and stone[i - 2][k - 2] == -1 and stone[
                        i - 1][k - 1] == 0 and stone[i + 1][k + 1] == -1 and stone[i + 2][
                         k + 2] == 0) or
                    (stone[i + 3][k + 3] == 0 and stone[i + 2][k + 2] == -1 and stone[
                        i + 1][k + 1] == 0 and stone[i - 1][k - 1] == -1 and stone[i - 2][
                         k - 2] == 0) or
                    (stone[i - 4][k - 4] == 0 and stone[i - 3][k - 3] == -1 and stone[
                        i - 2][k - 2] == -1 and stone[i - 1][k - 1] == 0 and stone[i + 1][
                         k + 1] == 0) or
                    (stone[i + 4][k + 4] == 0 and stone[i + 3][k + 3] == -1 and stone[
                        i + 2][k + 2] == -1 and stone[i + 1][k + 1] == 0 and stone[i - 1][
                         k - 1] == 0)):
                count = count +1

            if ((stone[i - 3][k + 3] == 0 and stone[i - 2][k + 2] == -1 and stone[i - 1][
                k + 1] == -1 and stone[
                     i + 1][k - 1] == 0) or
                    (stone[i - 2][k + 2] == 0 and stone[i - 1][k + 1] == -1 and stone[
                        i + 1][k - 1] == -1 and stone[i + 2][k - 2] == 0) or
                    (stone[i - 1][k + 1] == 0 and stone[i + 1][k - 1] == -1 and stone[
                        i + 2][k - 2] == -1 and stone[i + 3][k - 3] == 0) or
                    (stone[i - 3][k + 3] == 0 and stone[i - 2][k + 2] == -1 and stone[
                        i - 1][k + 1] == 0 and stone[i + 1][k - 1] == -1 and stone[i + 2][
                         k - 2] == 0) or
                    (stone[i + 3][k - 3] == 0 and stone[i + 2][k - 2] == -1 and stone[
                        i + 1][k - 1] == 0 and stone[i - 1][k + 1] == -1 and stone[i - 2][
                         k + 2] == 0) or
                    (stone[i - 4][k + 4] == 0 and stone[i - 3][k + 3] == -1 and stone[
                        i - 2][k + 2] == -1 and stone[i - 1][k + 1] == 0 and stone[i + 1][
                         k - 1] == 0) or
                    (stone[i + 4][k - 4] == 0 and stone[i + 3][k - 3] == -1 and stone[
                        i + 2][k - 2] == -1 and stone[i + 1][k - 1] == 0 and stone[i - 1][
                         k + 1] == 0)):
                count = count +1
            if count > 1:
                return False
            return True
    
        
    
