from player import *
from stone import *
from random import *
import random


class iot6789_student(player):
    def __init__(self, clr):
        super().__init__(clr)
        self.__black_turn = 0
        self.__black_xy_list = []

    def __del__(self):  # destructor
        pass

    #########################################################################################################################################
    def Defense(self, board, length):
        xy = []
        # 3,3 방어
        for i in range(3, length - 3):
            for j in range(3, length - 3):
                if (board[i][j] == 0):
                    # print("좌표가 가지는 값 : ", board[i][j])
                    # 111111111111111111111111
                    if ((board[i + 1][j] == 1 and board[i + 2][j] == 1) and board[i + 3][j + 3] == 0):
                        if ((board[i + 1][j + 1] == 1 and board[i + 2][j + 2] == 1) and board[i + 3][j + 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i][j + 1] == 1 and board[i][j + 2] == 1) and board[i][j + 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i - 1][j + 1] == 1 and board[i - 2][j + 2] == 1) and board[i - 3][j + 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i - 1][j - 1] == 1 and board[i - 2][j - 2] == 1) and board[i - 3][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i][j - 1] == 1 and board[i][j - 2] == 1) and board[i][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1) and board[i + 3][j - 3] == 0):
                            xy = [i, j]
                            return xy
                    # 22222222222222222222222
                    if ((board[i + 1][j + 1] == 1 and board[i + 2][j + 2] == 1) and board[i + 3][j + 3] == 0):
                        if ((board[i][j + 1] == 1 and board[i][j + 2] == 1) and board[i][j + 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i - 1][j + 1] == 1 and board[i - 2][j + 2] == 1) and board[i - 3][j + 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i - 1][j] == 1 and board[i - 2][j] == 1) and board[i - 3][j] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i][j - 1] == 1 and board[i][j - 2] == 1) and board[i][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1) and board[i + 3][j - 3] == 0):
                            xy = [i, j]
                            return xy

                    # 33333333333333333333333
                    if ((board[i][j + 1] == 1 and board[i][j + 2] == 1) and board[i][j + 3] == 0):
                        if ((board[i - 1][j + 1] == 1 and board[i - 2][j + 2] == 1) and board[i - 3][j + 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i - 1][j] == 1 and board[i - 2][j] == 1) and board[i - 3][j] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i - 1][j - 1] == 1 and board[i - 2][j - 2] == 1) and board[i - 3][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1) and board[i + 3][j - 3] == 0):
                            xy = [i, j]
                            return xy

                    # 4444444444444444444444
                    if ((board[i - 1][j + 1] == 1 and board[i - 2][j + 2] == 1) and board[i - 3][j + 3] == 0):
                        if ((board[i - 1][j] == 1 and board[i - 2][j] == 1) and board[i - 3][j] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i - 1][j - 1] == 1 and board[i - 2][j - 2] == 1) and board[i - 3][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i][j - 1] == 1 and board[i][j - 2] == 1) and board[i][j - 3] == 0):
                            xy = [i, j]
                            return xy

                    # 555555555555555555555
                    if ((board[i - 1][j] == 1 and board[i - 2][j] == 1) and board[i - 3][j] == 0):
                        if ((board[i - 1][j - 1] == 1 and board[i - 2][j - 2] == 1) and board[i - 3][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i][j - 1] == 1 and board[i][j - 2] == 1) and board[i][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1) and board[i + 3][j - 3] == 0):
                            xy = [i, j]
                            return xy

                    # 666666666666666666666
                    if ((board[i - 1][j - 1] == 1 and board[i - 2][j - 2] == 1) and board[i - 3][j - 3] == 0):
                        if ((board[i][j - 1] == 1 and board[i][j - 2] == 1) and board[i][j - 3] == 0):
                            xy = [i, j]
                            return xy
                        if ((board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1) and board[i + 3][j - 3] == 0):
                            xy = [i, j]
                            return xy

                    # 777777777777777777777
                    if ((board[i][j - 1] == 1 and board[i][j - 2] == 1) and board[i][j - 3] == 0):
                        if ((board[i + 1][j - 1] == 1 and board[i + 2][j - 2] == 1) and board[i + 3][j - 3] == 0):
                            xy = [i, j]
                            return xy

        # 수평 / 오 / 5 / 필막
        for i in range(0, length):
            for j in range(0, length - 4):
                if (board[i][j] == 1):
                    check = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3] + board[i][j + 4]
                    if (check == (4 * board[i][j])):
                        for t in range(0, 5):
                            if (board[i][j + t] == 0):
                                xy = [i, j + t]
                                return xy

        # 수평 / 오 / 4 / 필막
        for i in range(0, length):
            for j in range(0, length - 3):
                if (board[i][j] == 1):
                    check = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3]
                    if (check == (3 * board[i][j]) and (board[i][j - 1] == 0 and board[i][j + 4] == 0)):
                        for t in range(0, 4):
                            if (board[i][j + t] == 0):
                                xy = [i, j + t]
                                return xy

        # 수평 / 오 / 4
        for i in range(0, length):
            for j in range(0, length - 3):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == 1):
                    check = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3]
                    if (check == (4 * board[i][j])):
                        if (board[i][j - 1] == 0 and board[i][j + 4] == 0):
                            for x in range(0, self.__black_turn):
                                sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                sum2y += abs((j + 4) - self.__black_xy_list[x][1])
                                if (sum1y <= sum2y):
                                    xy = [i, j - 1]
                                    return xy
                                else:
                                    xy = [i, j + 4]
                                    return xy
                        elif (board[i][j - 1] != 0 and board[i][j + 4] == 0):
                            xy = [i, j + 4]
                            return xy
                        elif (board[i][j - 1] == 0 and board[i][j + 4] != 0):
                            xy = [i, j - 1]
                            return xy

        # 수평 / 오 / 3
        for i in range(0, length):
            for j in range(0, length - 2):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == 1):
                    check = board[i][j] + board[i][j + 1] + board[i][j + 2]
                    if (check == (3 * board[i][j])):
                        if (board[i][j - 1] == 0 and board[i][j + 3] == 0):
                            for x in range(0, self.__black_turn):
                                sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                sum2y += abs((j + 3) - self.__black_xy_list[x][1])
                                if (sum1y <= sum2y):
                                    xy = [i, j - 1]
                                    return xy
                                else:
                                    xy = [i, j + 3]
                                    return xy

        # 수직 / 위 / 5 / 필막
        for i in range(0, length):
            for j in range(0, length - 4):
                if (board[j][i] == 1):
                    check = board[j][i] + board[j + 1][i] + board[j + 2][i] + board[j + 3][i] + board[j + 4][i]
                    if (check == (4 * board[j][i])):
                        for t in range(0, 5):
                            if (board[j + t][i] == 0):
                                xy = [j + t, i]
                                return xy

        # 수직 / 위 / 4 / 필막
        for i in range(0, length):
            for j in range(0, length - 4):
                if (board[j][i] == 1):
                    check = board[j][i] + board[j + 1][i] + board[j + 2][i] + board[j + 3][i]
                    if (check == (3 * board[j][i]) and (board[j - 1][i] == 0 and board[j + 4][i] == 0)):
                        for t in range(0, 4):
                            if (board[j + t][i] == 0):
                                xy = [j + t, i]
                                return xy

        # 수직 / 위 / 4
        for i in range(0, length):
            for j in range(0, length - 3):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[j][i] == 1):
                    check = board[j][i] + board[j + 1][i] + board[j + 2][i] + board[j + 3][i]
                    if (check == (4 * board[j][i])):
                        if (board[j - 1][i] == 0 and board[j + 4][i] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((j - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((j + 4) - self.__black_xy_list[x][0])
                                if (sum1x <= sum2x):
                                    xy = [j - 1, i]
                                    return xy
                                else:
                                    xy = [j + 4, i]
                                    return xy
                        elif (board[j - 1][i] != 0 and board[j + 4][i] == 0):
                            xy = [j + 4, i]
                            return xy
                        elif (board[j - 1][i] == 0 and board[j + 4][i] != 0):
                            xy = [j - 1, i]
                            return xy

        # 수직 / 위 / 3
        for i in range(0, length):
            for j in range(0, length - 2):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[j][i] == 1):
                    check = board[j][i] + board[j + 1][i] + board[j + 2][i]
                    if (check == (3 * board[j][i])):
                        if (board[j - 1][i] == 0 and board[j + 3][i] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((j - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((j + 3) - self.__black_xy_list[x][0])
                                if (sum1x <= sum2x):
                                    xy = [j - 1, i]
                                    return xy
                                else:
                                    xy = [j + 3, i]
                                    return xy

        # 대각선 / 오른위 / 5 / 필막
        for i in range(0, length - 4):
            for j in range(0, length - 4):
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3] + \
                            board[i + 4][j + 4]
                    if (check == (4 * board[i][j])):
                        for t in range(0, 5):
                            if (board[i + t][j + t] == 0):
                                xy = [i + t, j + t]
                                return xy

        # 대각선 / 오른위 / 4 / 필막
        for i in range(0, length - 3):
            for j in range(0, length - 3):
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3]
                    if (check == (3 * board[i][j]) and (board[i - 1][j - 1] == 0 and board[i + 4][j + 4] == 0)):
                        for t in range(0, 4):
                            if (board[i + t][j + t] == 0):
                                xy = [i + t, j + t]
                                return xy

        # 대각선 / 오른위 / 4
        for i in range(0, length - 3):
            for j in range(0, length - 3):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3]
                    if (check == (4 * board[i][j])):
                        if (board[i - 1][j - 1] == 0 and board[i + 4][j + 4] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 4) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j + 4) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            xy = [i - 1, j - 1]
                                            return xy
                                        else:
                                            xy = [i + 4, j + 4]
                                            return xy
                                elif (sum1x < sum2x):
                                    xy = [i - 1, j - 1]
                                    return xy
                                else:
                                    xy = [i + 4, j + 4]
                                    return xy
                        elif (board[i - 1][j - 1] != 0 and board[i + 4][j + 4] == 0):
                            xy = [i + 4, j + 4]
                            return xy
                        elif (board[i - 1][j - 1] == 0 and board[i + 4][j + 4] != 0):
                            xy = [i - 1, j - 1]
                            return xy

        # 대각선 / 오른위 / 3
        for i in range(0, length - 2):
            for j in range(0, length - 2):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2]
                    if (check == (3 * board[i][j])):
                        if (board[i - 1][j - 1] == 0 and board[i + 3][j + 3] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 3) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j + 3) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            xy = [i - 1, j - 1]
                                            return xy
                                        else:
                                            xy = [i + 3, j + 3]
                                            return xy
                                elif (sum1x < sum2x):
                                    xy = [i - 1, j - 1]
                                    return xy
                                else:
                                    xy = [i + 3, j + 3]
                                    return xy

        # 대각선 / 왼위 / 5 / 필막
        for i in range(0, length - 4):
            for j in range(4, length):
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3] + \
                            board[i + 4][j - 4]
                    if (check == (4 * board[i][j])):
                        for t in range(0, 5):
                            if (board[i + t][j - t] == 0):
                                xy = [i + t, j - t]
                                return xy

        # 대각선 / 왼위 / 4 / 필막
        for i in range(0, length - 3):
            for j in range(3, length):
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3]
                    if (check == (3 * board[i][j]) and (board[i - 1][j + 1] == 0 and board[i + 4][j - 4] == 0)):
                        for t in range(0, 4):
                            if (board[i + t][j - t] == 0):
                                xy = [i + t, j - t]
                                return xy

        # 대각선 / 왼위 / 4
        for i in range(0, length - 3):
            for j in range(3, length):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3]
                    if (check == (4 * board[i][j])):
                        if (board[i - 1][j + 1] == 0 and board[i + 4][j - 4] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 4) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j - 4) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            xy = [i - 1, j + 1]
                                            return xy
                                        else:
                                            xy = [i + 4, j - 4]
                                            return xy
                                elif (sum1x < sum2x):
                                    xy = [i - 1, j + 1]
                                    return xy
                                else:
                                    xy = [i + 4, j - 4]
                                    return xy
                        elif (board[i - 1][j + 1] != 0 and board[i + 4][j - 4] == 0):
                            xy = [i + 4, j - 4]
                            return xy
                        elif (board[i - 1][j + 1] == 0 and board[i + 4][j - 4] != 0):
                            xy = [i - 1, j + 1]
                            return xy

        # 대각선 / 왼위 / 3
        for i in range(0, length - 2):
            for j in range(2, length):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == 1):
                    check = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2]
                    if (check == (3 * board[i][j])):
                        if (board[i - 1][j + 1] == 0 and board[i + 3][j - 3] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 3) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j - 3) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            xy = [i - 1, j + 1]
                                            return xy
                                        else:
                                            xy = [i + 3, j - 3]
                                            return xy
                                elif (sum1x < sum2x):
                                    xy = [i - 1, j + 1]
                                    return xy
                                else:
                                    xy = [i + 3, j - 3]
                                    return xy

        print("방어에서 나감")

    #########################################################################################################################################
    def Attack(self, board, length):
        pri = []  # 공격 우선순위 리스트
        xy = []

        print("공격에 들어옴")
        # 수평 / 오 / 5 / 필공
        for i in range(0, length):
            for j in range(0, length - 4):
                if (board[i][j] == -1):
                    check = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3] + board[i][j + 4]
                    if (check == (4 * board[i][j])):
                        for t in range(0, 5):
                            if (board[i][j + t] == 0):
                                pri.append([-1, i, j + t])

        # 수평 / 오 / 4
        for i in range(0, length):
            for j in range(0, length - 3):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3]
                    if (check == (4 * board[i][j])):
                        if (board[i][j - 1] != 0 and board[i][j + 4] == 0):
                            pri.append([1, i, j + 4])
                        elif (board[i][j + 4] == 0 and board[i][j - 1] != 0):
                            pri.append([1, i, j - 1])
                        elif (board[i][j + 4] == 0 and board[i][j - 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                sum2y += abs((j + 4) - self.__black_xy_list[x][1])
                                if (sum1y <= sum2y):
                                    pri.append([0, i, j - 1])
                                else:
                                    pri.append([0, i, j + 4])
                    elif (check == (3 * board[i][j])):
                        if (board[i][j + 4] != 0 and board[i][j - 1] == 0):
                            for t in range(0, 4):
                                if (board[i][j + t] == 0):
                                    pri.append([1, i, j + t])
                        elif (board[i][j + 4] == 0 and board[i][j - 1] != 0):
                            for t in range(0, 4):
                                if (board[i][j + t] == 0):
                                    pri.append([1, i, j + t])
                        elif (board[i][j + 4] == 0 and board[i][j - 1] == 0):
                            for t in range(0, 4):
                                if (board[i][j + t] == 0):
                                    pri.append([0, i, j + t])

        # 수평 / 오 / 3
        for i in range(0, length):
            for j in range(0, length - 2):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i][j + 1] + board[i][j + 2]
                    if (check == (3 * board[i][j])):
                        if (board[i][j - 1] != 0 and board[i][j + 3] == 0):
                            pri.append([3, i, j + 3])
                        elif (board[i][j + 3] != 0 and board[i][j - 1] == 0):
                            pri.append([3, i, j - 1])
                        elif (board[i][j + 3] == 0 and board[i][j - 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                sum2y += abs((j + 3) - self.__black_xy_list[x][1])
                                if (sum1y <= sum2y):
                                    pri.append([2, i, j - 1])
                                else:
                                    pri.append([2, i, j + 3])
                    elif (check == (2 * board[i][j])):
                        if (board[i][j + 3] != 0 and board[i][j - 1] == 0):
                            for t in range(0, 3):
                                if (board[i][j + t] == 0):
                                    pri.append([3, i, j + t])
                        if (board[i][j + 3] == 0 and board[i][j - 1] != 0):
                            for t in range(0, 3):
                                if (board[i][j + t] == 0):
                                    pri.append([3, i, j + t])
                        if (board[i][j + 3] == 0 and board[i][j - 1] == 0):
                            for t in range(0, 3):
                                if (board[i][j + t] == 0):
                                    pri.append([2, i, j + t])
        # 수평 / 오 / 2
        for i in range(0, length):
            for j in range(0, length - 1):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i][j + 1]
                    if (check == (2 * board[i][j])):
                        if (board[i][j - 1] != 0 and board[i][j + 2] == 0):
                            pri.append([5, i, j + 2])
                        elif (board[i][j + 2] != 0 and board[i][j - 1] == 0):
                            pri.append([5, i, j - 1])
                        elif (board[i][j + 2] == 0 and board[i][j - 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                sum2y += abs((j + 2) - self.__black_xy_list[x][1])
                                if (sum1y <= sum2y):
                                    pri.append([4, i, j - 1])
                                else:
                                    pri.append([4, i, j + 2])

        ##########################################

        # 수직 / 위 / 5 / 필공
        for i in range(0, length):
            for j in range(0, length - 4):
                if (board[j][i] == -1):
                    check = board[j][i] + board[j + 1][i] + board[j + 2][i] + board[j + 3][i] + board[j + 4][i]
                    if (check == (4 * board[j][i])):
                        for t in range(0, 5):
                            if (board[j + t][i] == 0):
                                pri.append([-1, j + t, i])

        # 수직 / 위 / 4
        for i in range(0, length):
            for j in range(0, length - 3):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[j][i] == -1):
                    check = board[j][i] + board[j + 1][i] + board[j + 2][i] + board[j + 3][i]
                    if (check == (4 * board[j][i])):
                        if (board[j - 1][i] != 0 and board[j + 4][i] == 0):
                            pri.append([1, j + 4, i])
                        elif (board[j + 4][i] != 0 and board[j - 1][i] == 0):
                            pri.append([1, j - 1, i])
                        elif (board[j + 4][i] == 0 and board[j - 1][i] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((j - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((j + 4) - self.__black_xy_list[x][0])
                                if (sum1x <= sum2x):
                                    pri.append([0, j - 1, i])
                                else:
                                    pri.append([0, j + 4, i])
                    elif (check == (3 * board[j][i])):
                        if (board[j + 4][i] != 0 and board[j - 1][i] == 0):
                            for t in range(0, 4):
                                if (board[j + t][i] == 0):
                                    pri.append([1, j + t, i])
                        if (board[j + 4][i] == 0 and board[j - 1][i] != 0):
                            for t in range(0, 4):
                                if (board[j + t][i] == 0):
                                    pri.append([1, j + t, i])
                        if (board[j + 4][i] == 0 and board[j - 1][i] == 0):
                            for t in range(0, 4):
                                if (board[j + t][i] == 0):
                                    pri.append([0, j + t, i])

        # 수직 / 위 / 3
        for i in range(0, length):
            for j in range(0, length - 2):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[j][i] == -1):
                    check = board[j][i] + board[j + 1][i] + board[j + 2][i]
                    if (check == (3 * board[j][i])):
                        if (board[j - 1][i] != 0 and board[j + 3][i] == 0):
                            pri.append([3, j + 3, i])
                        elif (board[j + 3][i] != 0 and board[j - 1][i] == 0):
                            pri.append([3, j - 1, i])
                        elif (board[j + 3][i] == 0 and board[j - 1][i] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((j - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((j + 3) - self.__black_xy_list[x][0])
                                if (sum1x <= sum2x):
                                    pri.append([2, j - 1, i])
                                else:
                                    pri.append([2, j + 3, i])
                    elif (check == (2 * board[j][i])):
                        if (board[j + 3][i] != 0 and board[j - 1][i] == 0):
                            for t in range(0, 3):
                                if (board[j + t][i] == 0):
                                    pri.append([3, j + t, i])
                        if (board[j + 3][i] == 0 and board[j - 1][i] != 0):
                            for t in range(0, 3):
                                if (board[j + t][i] == 0):
                                    pri.append([3, j + t, i])
                        if (board[j + 3][i] == 0 and board[j - 1][i] == 0):
                            for t in range(0, 3):
                                if (board[j + t][i] == 0):
                                    pri.append([2, j + t, i])

        # 수직 / 위 / 2
        for i in range(0, length):
            for j in range(0, length - 1):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[j][i] == -1):
                    check = board[j][i] + board[j + 1][i]
                    if (check == (2 * board[j][i])):
                        if (board[j - 1][i] != 0 and board[j + 2][i] == 0):
                            pri.append([5, j + 2, i])
                        elif (board[j + 2][i] != 0 and board[j - 1][i] == 0):
                            pri.append([5, j - 1, i])
                        elif (board[j + 2][i] == 0 and board[j - 1][i] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((j - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((j + 2) - self.__black_xy_list[x][0])
                                if (sum1x <= sum2x):
                                    pri.append([4, j - 1, i])
                                else:
                                    pri.append([4, j + 2, i])
        ####################################

        # 대각선 / 오른위 / 5 / 필공
        for i in range(0, length - 4):
            for j in range(0, length - 4):
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3] + \
                            board[i + 4][j + 4]
                    if (check == (4 * board[i][j])):
                        for t in range(0, 5):
                            if (board[i + t][j + t] == 0):
                                pri.append([-1, i + t, j + t])

        # 대각선 / 오른위 / 4
        for i in range(0, length - 3):
            for j in range(0, length - 3):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3]
                    if (check == (4 * board[i][j])):
                        if (board[i - 1][j - 1] != 0 and board[i + 4][j + 4] == 0):
                            pri.append([1, i + 4, j + 4])
                        elif (board[i + 4][j + 4] != 0 and board[i - 1][j - 1] == 0):
                            pri.append([1, i - 1, j - 1])
                        elif (board[i + 4][j + 4] == 0 and board[i - 1][j - 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 4) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j + 4) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            pri.append([0, i - 1, j - 1])
                                        else:
                                            pri.append([0, i + 4, j + 4])
                                elif (sum1x < sum2x):
                                    pri.append([0, i - 1, j - 1])
                                else:
                                    pri.append([0, i + 4, j + 4])
                    elif (check == (3 * board[i][j])):
                        if (board[i + 4][j + 4] == 0 and board[i - 1][j - 1] != 0):
                            for t in range(0, 4):
                                if (board[i + t][j + t] == 0):
                                    pri.append([1, i + t, j + t])
                        if (board[i + 4][j + 4] != 0 and board[i - 1][j - 1] == 0):
                            for t in range(0, 4):
                                if (board[i + t][j + t] == 0):
                                    pri.append([1, i + t, j + t])
                        if (board[i + 4][j + 4] == 0 and board[i - 1][j - 1] == 0):
                            for t in range(0, 4):
                                if (board[i + t][j + t] == 0):
                                    pri.append([0, i + t, j + t])

        # 대각선 / 오른위 / 3
        for i in range(0, length - 2):
            for j in range(0, length - 2):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2]
                    if (check == (3 * board[i][j])):
                        if (board[i - 1][j - 1] != 0 and board[i + 3][j + 3] == 0):
                            pri.append([3, i + 3, j + 3])
                        elif (board[i + 3][j + 3] != 0 and board[i - 1][j - 1] == 0):
                            pri.append([3, i - 1, j - 1])
                        elif (board[i + 3][j + 3] == 0 and board[i - 1][j - 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 3) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j + 3) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            pri.append([2, i - 1, j - 1])
                                        else:
                                            pri.append([2, i + 3, j + 3])
                                elif (sum1x < sum2x):
                                    pri.append([2, i - 1, j - 1])
                                else:
                                    pri.append([2, i + 3, j + 3])
                    elif (check == (2 * board[i][j])):
                        if (board[i + 3][j + 3] != 0 and board[i - 1][j - 1] == 0):
                            for t in range(0, 3):
                                if (board[i + t][j + t] == 0):
                                    pri.append([3, i + t, j + t])
                        if (board[i + 3][j + 3] == 0 and board[i - 1][j - 1] != 0):
                            for t in range(0, 3):
                                if (board[i + t][j + t] == 0):
                                    pri.append([3, i + t, j + t])
                        if (board[i + 3][j + 3] == 0 and board[i - 1][j - 1] == 0):
                            for t in range(0, 3):
                                if (board[i + t][j + t] == 0):
                                    pri.append([2, i + t, j + t])

        # 대각선 / 오른위 / 2
        for i in range(0, length - 1):
            for j in range(0, length - 1):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j + 1]
                    if (check == (2 * board[i][j])):
                        if (board[i - 1][j - 1] != 0 and board[i + 2][j + 2] == 0):
                            pri.append([5, i + 2, j + 2])
                        elif (board[i + 2][j + 2] != 0 and board[i - 1][j - 1] == 0):
                            pri.append([5, i - 1, j - 1])
                        elif (board[i + 2][j + 2] == 0 and board[i - 1][j - 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 2) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j + 2) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            pri.append([4, i - 1, j - 1])
                                        else:
                                            pri.append([4, i + 2, j + 2])
                                elif (sum1x < sum2x):
                                    pri.append([4, i - 1, j - 1])
                                else:
                                    pri.append([4, i + 2, j + 2])
        ####################################

        # 대각선 / 왼위 / 5 / 필공
        for i in range(0, length - 4):
            for j in range(4, length):
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3] + \
                            board[i + 4][j - 4]
                    if (check == (4 * board[i][j])):
                        for t in range(0, 5):
                            if (board[i + t][j - t] == 0):
                                pri.append([-1, i + t, j - t])

        # 대각선 / 왼위 / 4
        for i in range(0, length - 3):
            for j in range(3, length):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3]
                    if (check == (4 * board[i][j])):
                        if (board[i - 1][j + 1] != 0 and board[i + 4][j - 4] == 0):
                            pri.append([1, i + 4, j - 4])
                        elif (board[i + 4][j - 4] != 0 and board[i - 1][j + 1] == 0):
                            pri.append([1, i - 1, j + 1])
                        elif (board[i + 4][j - 4] == 0 and board[i - 1][j + 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 4) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j - 4) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            pri.append([0, i - 1, j + 1])
                                        else:
                                            pri.append([0, i + 4, j - 4])
                                elif (sum1x < sum2x):
                                    pri.append([0, i - 1, j + 1])
                                else:
                                    pri.append([0, i + 4, j - 4])
                    elif (check == (3 * board[i][j])):
                        if (board[i + 4][j - 4] != 0 and board[i - 1][j + 1] == 0):
                            for t in range(0, 4):
                                if (board[i + t][j - t] == 0):
                                    pri.append([1, i + t, j - t])
                        if (board[i + 4][j - 4] == 0 and board[i - 1][j + 1] != 0):
                            for t in range(0, 4):
                                if (board[i + t][j - t] == 0):
                                    pri.append([1, i + t, j - t])
                        if (board[i + 4][j - 4] == 0 and board[i - 1][j + 1] == 0):
                            for t in range(0, 4):
                                if (board[i + t][j - t] == 0):
                                    pri.append([0, i + t, j - t])

        # 대각선 / 왼위 / 3
        for i in range(0, length - 2):
            for j in range(2, length):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2]
                    if (check == (3 * board[i][j])):
                        if (board[i - 1][j + 1] != 0 and board[i + 3][j - 3] == 0):
                            pri.append([3, i + 3, j - 3])
                        elif (board[i + 3][j - 3] != 0 and board[i - 1][j + 1] == 0):
                            pri.append([3, i - 1, j + 1])
                        elif (board[i + 3][j - 3] == 0 and board[i - 1][j + 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 3) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j - 3) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            pri.append([2, i - 1, j + 1])
                                        else:
                                            pri.append([2, i + 3, j - 3])
                                elif (sum1x < sum2x):
                                    pri.append([2, i - 1, j + 1])
                                else:
                                    pri.append([2, i + 3, j - 3])
                    elif (check == (2 * board[i][j])):
                        if (board[i + 3][j - 3] != 0 and board[i - 1][j + 1] == 0):
                            for t in range(0, 3):
                                if (board[i + t][j - t] == 0):
                                    pri.append([3, i + t, j - t])
                        if (board[i + 3][j - 3] == 0 and board[i - 1][j + 1] != 0):
                            for t in range(0, 3):
                                if (board[i + t][j - t] == 0):
                                    pri.append([3, i + t, j - t])
                        if (board[i + 3][j - 3] == 0 and board[i - 1][j + 1] == 0):
                            for t in range(0, 3):
                                if (board[i + t][j - t] == 0):
                                    pri.append([2, i + t, j - t])

        # 대각선 / 왼위 / 2
        for i in range(0, length - 1):
            for j in range(1, length):
                sum1x = 0
                sum2x = 0
                sum1y = 0
                sum2y = 0
                if (board[i][j] == -1):
                    check = board[i][j] + board[i + 1][j - 1]
                    if (check == (2 * board[i][j])):
                        if (board[i - 1][j + 1] != 0 and board[i + 2][j - 2] == 0):
                            pri.append([5, i + 2, j - 2])
                        elif (board[i + 2][j - 2] != 0 and board[i - 1][j + 1] == 0):
                            pri.append([5, i - 1, j + 1])
                        elif (board[i + 2][j - 2] == 0 and board[i - 1][j + 1] == 0):
                            for x in range(0, self.__black_turn):
                                sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                sum2x += abs((i + 2) - self.__black_xy_list[x][0])
                                if (sum1x == sum2x):
                                    for x in range(0, self.__black_turn):
                                        sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                        sum2y += abs((j - 2) - self.__black_xy_list[x][1])
                                        if (sum1y < sum2y):
                                            pri.append([4, i - 1, j + 1])
                                        else:
                                            pri.append([4, i + 2, j - 2])
                                elif (sum1x < sum2x):
                                    pri.append([4, i - 1, j + 1])
                                else:
                                    pri.append([4, i + 2, j - 2])

        if not pri:
            # 대각선 / 오른위 / 2 / 미ㅌ
            for i in range(0, length - 1):
                for j in range(0, length - 1):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[i][j] == -1):
                        check = board[i][j] + board[i + 1][j + 1]
                        if (check == (2 * board[i][j])):
                            if (board[i - 1][j + 1] != 0 and board[i][j + 2] == 0):
                                pri.append([0, i, j + 2])
                            elif (board[i][j + 2] != 0 and board[i - 1][j + 1] == 0):
                                pri.append([0, i - 1, j + 1])
                            elif (board[i][j + 2] == 0 and board[i - 1][j + 1] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                    sum2x += abs((i) - self.__black_xy_list[x][0])
                                    if (sum1x == sum2x):
                                        for x in range(0, self.__black_turn):
                                            sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                            sum2y += abs((j + 2) - self.__black_xy_list[x][1])
                                            if (sum1y < sum2y):
                                                pri.append([0, i - 1, j + 1])
                                            else:
                                                pri.append([0, i, j + 2])
                                    elif (sum1x < sum2x):
                                        pri.append([0, i - 1, j + 1])
                                    else:
                                        pri.append([0, i, j + 2])

            # 대각선 / 오른위 / 2 / 우ㅣㅅ
            for i in range(0, length - 1):
                for j in range(0, length - 1):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[i][j] == -1):
                        check = board[i][j] + board[i + 1][j + 1]
                        if (check == (2 * board[i][j])):
                            if (board[i + 1][j - 1] != 0 and board[i + 2][j] == 0):
                                pri.append([0, i + 2, j])
                            elif (board[i + 2][j] != 0 and board[i + 1][j - 1] == 0):
                                pri.append([0, i + 1, j - 1])
                            elif (board[i + 2][j] == 0 and board[i + 1][j - 1] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1x += abs((i + 1) - self.__black_xy_list[x][0])
                                    sum2x += abs((i + 2) - self.__black_xy_list[x][0])
                                    if (sum1x == sum2x):
                                        for x in range(0, self.__black_turn):
                                            sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                            sum2y += abs((j) - self.__black_xy_list[x][1])
                                            if (sum1y < sum2y):
                                                pri.append([0, i + 1, j - 1])
                                            else:
                                                pri.append([0, i + 2, j])
                                    elif (sum1x < sum2x):
                                        pri.append([0, i + 1, j - 1])
                                    else:
                                        pri.append([0, i + 2, j])

            # 대각선 / 왼위 / 2 / 미ㅌ
            for i in range(0, length - 1):
                for j in range(1, length):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[i][j] == -1):
                        check = board[i][j] + board[i + 1][j - 1]
                        if (check == (2 * board[i][j])):
                            if (board[i - 1][j - 1] != 0 and board[i][j - 2] == 0):
                                pri.append([0, i, j - 2])
                            elif (board[i][j - 2] != 0 and board[i - 1][j - 1] == 0):
                                pri.append([0, i - 1, j - 1])
                            elif (board[i][j - 2] == 0 and board[i - 1][j - 1] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                    sum2x += abs((i) - self.__black_xy_list[x][0])
                                    if (sum1x == sum2x):
                                        for x in range(0, self.__black_turn):
                                            sum1y += abs((j - 1) - self.__black_xy_list[x][1])
                                            sum2y += abs((j - 2) - self.__black_xy_list[x][1])
                                            if (sum1y < sum2y):
                                                pri.append([0, i - 1, j - 1])
                                            else:
                                                pri.append([0, i, j - 2])
                                    elif (sum1x < sum2x):
                                        pri.append([0, i - 1, j - 1])
                                    else:
                                        pri.append([0, i, j - 2])

            # 대각선 / 왼위 / 2 / 우ㅣㅅ
            for i in range(0, length - 1):
                for j in range(1, length):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[i][j] == -1):
                        check = board[i][j] + board[i + 1][j - 1]
                        if (check == (2 * board[i][j])):
                            if (board[i + 2][j] != 0 and board[i + 1][j + 1] == 0):
                                pri.append([0, i + 1, j + 1])
                            elif (board[i + 1][j + 1] != 0 and board[i + 2][j] == 0):
                                pri.append([0, i + 2, j])
                            elif (board[i + 1][j + 1] == 0 and board[i + 2][j] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1x += abs((i + 1) - self.__black_xy_list[x][0])
                                    sum2x += abs((i + 2) - self.__black_xy_list[x][0])
                                    if (sum1x == sum2x):
                                        for x in range(0, self.__black_turn):
                                            sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                            sum2y += abs((j) - self.__black_xy_list[x][1])
                                            if (sum1y < sum2y):
                                                pri.append([0, i + 1, j + 1])
                                            else:
                                                pri.append([0, i + 2, j])
                                    elif (sum1x < sum2x):
                                        pri.append([0, i + 1, j + 1])
                                    else:
                                        pri.append([0, i + 2, j])

            # 대각선 / 오른위 / 2 / 2수니
            for i in range(0, length - 1):
                for j in range(0, length - 1):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[i][j] == -1):
                        check = board[i][j] + board[i + 1][j + 1]
                        if (check == (2 * board[i][j])):
                            if (board[i][j + 1] != 0 and board[i + 1][j] == 0):
                                pri.append([1, i + 1, j])
                            elif (board[i + 1][j] != 0 and board[i][j + 1] == 0):
                                pri.append([1, i, j + 1])
                            elif (board[i + 1][j] == 0 and board[i][j + 1] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1x += abs((i) - self.__black_xy_list[x][0])
                                    sum2x += abs((i + 1) - self.__black_xy_list[x][0])
                                    if (sum1x == sum2x):
                                        for x in range(0, self.__black_turn):
                                            sum1y += abs((j + 1) - self.__black_xy_list[x][1])
                                            sum2y += abs((j) - self.__black_xy_list[x][1])
                                            if (sum1y < sum2y):
                                                pri.append([1, i, j + 1])
                                            else:
                                                pri.append([1, i + 1, j])
                                    elif (sum1x < sum2x):
                                        pri.append([1, i, j + 1])
                                    else:
                                        pri.append([1, i + 1, j])

            # 대각선 / 왼위 / 2 / 2수니
            for i in range(0, length - 1):
                for j in range(1, length):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[i][j] == -1):
                        check = board[i][j] + board[i + 1][j - 1]
                        if (check == (2 * board[i][j])):
                            if (board[i][j - 1] != 0 and board[i + 1][j] == 0):
                                pri.append([1, i + 1, j])
                            elif (board[i + 1][j] != 0 and board[i][j - 1] == 0):
                                pri.append([1, i, j - 1])
                            elif (board[i + 1][j] == 0 and board[i][j - 1] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1x += abs((i + 1) - self.__black_xy_list[x][0])
                                    sum2x += abs((i) - self.__black_xy_list[x][0])
                                    if (sum1x == sum2x):
                                        for x in range(0, self.__black_turn):
                                            sum1y += abs((j) - self.__black_xy_list[x][1])
                                            sum2y += abs((j - 1) - self.__black_xy_list[x][1])
                                            if (sum1y < sum2y):
                                                pri.append([1, i + 1, j])
                                            else:
                                                pri.append([1, i, j - 1])
                                    elif (sum1x < sum2x):
                                        pri.append([1, i + 1, j])
                                    else:
                                        pri.append([1, i, j - 1])

            # 수직 / 위 / 2 / 3수니
            for i in range(0, length):
                for j in range(0, length - 1):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[j][i] == -1):
                        check = board[j][i] + board[j + 1][i]
                        if (check == (2 * board[j][i])):
                            if (board[j][i + 1] != 0 and board[j][i - 1] == 0):
                                pri.append([2, j, i - 1])
                            elif (board[j][i - 1] != 0 and board[j][i + 1] == 0):
                                pri.append([2, j, i + 1])
                            elif (board[j][i - 1] == 0 and board[j][i + 1] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1y += abs((i - 1) - self.__black_xy_list[x][1])
                                    sum2y += abs((i + 1) - self.__black_xy_list[x][1])
                                    if (sum1y <= sum2y):
                                        pri.append([2, j, i - 1])
                                    else:
                                        pri.append([2, j, i + 1])

            # 수평 / 오 / 2 / 3수니
            for i in range(0, length):
                for j in range(0, length - 1):
                    sum1x = 0
                    sum2x = 0
                    sum1y = 0
                    sum2y = 0
                    if (board[i][j] == -1):
                        check = board[i][j] + board[i][j + 1]
                        if (check == (2 * board[i][j])):
                            if (board[i + 1][j + 1] != 0 and board[i - 1][j + 1] == 0):
                                pri.append([2, i - 1, j + 1])
                            elif (board[i - 1][j + 1] != 0 and board[i + 1][j + 1] == 0):
                                pri.append([2, i + 1, j + 1])
                            elif (board[i - 1][j + 1] == 0 and board[i + 1][j + 1] == 0):
                                for x in range(0, self.__black_turn):
                                    sum1x += abs((i - 1) - self.__black_xy_list[x][0])
                                    sum2x += abs((i + 1) - self.__black_xy_list[x][0])
                                    if (sum1x <= sum2x):
                                        pri.append([2, i - 1, j + 1])
                                    else:
                                        pri.append([2, i + 1, j + 1])

        print("pri :::: ", pri)
        pri_min = pri[0][0]
        for i in range(len(pri)):
            if (pri[i][0] <= pri_min):
                pri_min = pri[i][0]
                pri_index = i
                print("pri_min ::: ", pri_min)
                print("pri_index ::: ", pri_index)
                print("x ::: ", pri[pri_index][1])
                print("y ::: ", pri[pri_index][2])
        xy.append(pri[pri_index][1])
        xy.append(pri[pri_index][2])
        return xy
        print("공격에서 나감")

    #########################################################################################################################################

    def next(self, board, length):
        print(" **** Black player : My Turns **** ")

        stn = stone(self._color)  # 사이즈는 안줬기때문에 기본사이즈 19가 들어간다.
        x = 0  # 흙돌의 x좌표
        y = 0  # 흙돌의 y좌표
        xy = []

        # 첫턴일경우 / 좌표에 9,9 들어간다.
        if (self.__black_turn == 0):
            x = stn.getX()
            y = stn.getY()

        # 두번째 턴 일경우
        elif (self.__black_turn == 1):
            w_x = 0  # 백돌의 x좌표 넣을 변수
            w_y = 0  # 백돌의 y좌표 넣을 변수

            # 백돌의 좌표 읽어오기
            for i in range(0, length):  # 행, x
                for j in range(0, length):  # 열, y
                    if (board[i][j] == 1):
                        w_x = i
                        w_y = j

            # 흙돌 좌표 구하기
            while True:
                if (abs(w_x - 10) == abs(w_x - 8)):
                    x = random.choice([10, 8])
                    if (abs(w_y - 10) < abs(w_y - 8)):
                        y = 10
                    else:
                        y = 8
                elif (abs(w_x - 10) < abs(w_x - 8)):
                    x = 10
                    if (abs(w_y - 10) < abs(w_y - 8)):
                        y = 10
                    else:
                        y = 8

                    if (w_x == 10 and w_y == 10):
                        x = 8
                        y = 10
                    elif (w_x == 10 and w_y == 8):
                        x = 8
                        y = 8
                else:
                    x = 8
                    if (abs(w_y - 10) < abs(w_y - 8)):
                        y = 10
                    else:
                        y = 8

                    if (w_x == 8 and w_y == 8):
                        x = 10
                        y = 8
                    elif (w_x == 8 and w_y == 10):
                        x = 10
                        y = 10

                if (board[x][y] == 0):
                    break
        # 나머지 턴
        else:
            while True:
                xy = self.Defense(board, length)

                if not xy:
                    xy = self.Attack(board, length)
                    x = xy[0]
                    y = xy[1]
                    # print("공격에서 온 xy리스트 : ",xy)
                else:
                    x = xy[0]
                    y = xy[1]
                    # print("방어에서 온 xy리스트 : ",xy)

                if (board[x][y] == 0):
                    break

        stn.setX(x)
        stn.setY(y)
        print(x, ",,,,,,,", y)
        print(" === Black player was completed === ")
        self.__black_turn += 1  # 흙돌이 거쳐간 턴수를 저장한다.
        self.__black_xy_list.append([x, y])
        print(self.__black_xy_list)

        return stn