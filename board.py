from stone import *
from os import system, name 

class board:
    def __init__(self, size=19): #기본사이즈 15지만 사이즈 넘겨받는걸로 생성자와 함께 셋팅
        self.__size=size
        #게임보드 리스트 생성
        self.__game_board=[[0 for i in range(self.__size)] for j in range(self.__size)]
    def __del__(self):  # 소멸자 
        #print("board instance is destroyed")
        pass
    
    #보드를 업데이트하여 형재 진행중인 보드 게임판을 출력한다.
    def update(self,st):
        x = st.getX()
        y = st.getY()
        stone = st.getStone() #돌컬러를 stone에 저장
        print(x,",", y,":",stone) #좌표값과 돌컬러값을 출력한다.
        self.__game_board[x][y]=stone #돌컬러를 게임보드판에 입력한다.
        self.display()
    
    #15x15 보드판 리스트 출력한다.
    def show(self) :
        return self.__game_board
        
    #좌표를 넣어주어서 그 좌표에 있는 돌이 무엇인지 출력해준다.
    def get(self,x, y):
        return self.__game_board[x][y]
    
    #사용자가 볼 진행중인 게임 화면을 출력해준다.
    def display(self) :
    		#화면 클리어
        # for windows 
        if name == 'nt':
            _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else:
            _ = system('clear')
        #문자열을 가운데로 정리 3칸 공백 왼쪽 최상단 모서리를 채운다.
        print("{0:^3}".format(" "), end="") # no newline 
        #0~14까지 가운데정렬로 숫자 출력
        for i  in range(0, self.__size):
            print("{0:^3}".format(i), end="") # no newline
        print()  # 새줄
        #14~0까지 1씩 줄여가면서 가운데정렬로 숫자출력
        for i  in range(self.__size-1,-1, -1):
            print("{0:^3}".format(i), end="") # no newline
            #0~14까지 game_boar좌표에 들어있는 값을 val에 넣어서 출력
            for j  in range(0, self.__size):
               val=self.write_char(self.__game_board[i][j])
               print("{0:^3}".format(val), end="") # no newline
            print()  # new line 
            
    #백돌차례이면 W, 흙돌차례이면 B를 반환한다. 아직 게임시작전이면 .을 반환한다.
    def write_char(self,stn):
        if (stn == 1):
            return 'W'
        elif (stn == -1):
            return 'B'
        elif (stn == 0):
            return '.' # '+'
        else:
            return '.' # '+'
