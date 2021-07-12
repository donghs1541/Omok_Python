import copy #깊은 복사를 하기위한 모듈 추가

from board import *
#from player import *
from iot6789_student import *
from stone import *
from iot12345_student import *

class omokgame:
    def __init__(self, sz): #생성자, size x size값을 sz로 받는다.
        self.__size=sz #사이즈 설정
        self.__bd = board(self.__size) #보드 객체 생성(사이즈 값 넘겨준다.)
        #self.__white = player(1) #컬러값을 생성자 매개변수로 넘겨준다.
        self.__black = iot6789_student(-1) #흙돌의 객체를 생성한다.
        self.__white = iot12345_student(1) #백돌의 객체를 생성한다.
        self.__turns=0 #몇수인지 턴값을 넣는 변수이다.
        self.__next= -1 #누구의 턴인지 넣는 변수이다.
        self.__draw = 0 #비겼을경우 1 이된다.
        self.__winner =0 #흙이 이기게되면 -1, 흰이 이기게되면 1 이 된다.
        self.__bd.display()
    def __del__(self): #소멸자
        #print("omok instanced is destroyed")
        pass
    
    def game_start(self):
        # do ~ while 을 대신해서 사용
        while True:
            self.__turns +=1  #턴을 지날수록 1씩 증가한다.
            self.msg_display()
            temp = copy.deepcopy(self.__bd.show())
            #temp = 오목판을 깊을 복사 진행
            #매 판마다 복사하기 때문에 여기서 복사해도 무관
            
            if (self.__next == -1): #흙돌차례이면 출력한다. 몇수인지와 함께
                print(" black Player: Turns = %5d" % self.__turns )
                time =0 
                # do while 을 대신해서 사용
                while True:
                    print(" black Player: time = %5d" % time )
                    #복사된 오목판을 매개변수로 전달, 흙돌 객체를 next메소드를 통해서 반환받는다.
                    stn_b = self.__black.next(temp, self.__size)
                    time +=1 
                    #time 값이 4이상일 경우이거나 보드에 돌이 없을경우에는 멈춘다.
                    if ((time >= 4) or (self.validCheck(stn_b))):
                        break
                #시간이 4이하이면 보드판을 업데이트한후 보드판을 출력해준다.
                if (time < 4):
                    self.__bd.update(stn_b) #보드판에 현재 흙돌 객체를 보내준다.
                else: #시간이 4이상이 될경우 잘못된 값이 넣어졌고 턴이 끝났음을 알려준다.
                    print("Too many wrong input, black's turn is over")
                #차례를 백돌로 바꿔준다.
                self.__next = self.__next * (-1)
                
            #백돌 차례이면 출력한다. 몇수인지와 함께
            #이하 흙돌과 패턴 같다.
            elif (self.__next == 1) :
                print(" white Player: Turns = %5d" % self.__turns )
                time =0
                # do while 
                while True:
                    print(" White Player: time = %5d" % time )
                    stn_w = self.__white.next(temp, self.__size)
                    #복사된 오목판을 매개변수로 전달
                    time += 1
                    if ((time >= 4) or (self.validCheck(stn_w))):
                        break
                if (time < 4):
                    self.__bd.update(stn_w)
                else:
                    print("Too many wrong input, white's turn is over")
                self.__next = self.__next * (-1)
            
            #백돌이나 흙돌중 어느한쪽이 돌을 두고난뒤 게임이 끝나는 각이 나오는지 체크해준다.
            #끝나는 각이 나오면 참이여서 게임을 끝낸다.
            #끝나지 않으면 계속 해서 while문 실행
            if (self.endCheck()):
                break
        self.__winner = self.__next * (-1) #이긴돌의 값을 넣어준다.
        self.msg_display() #게임진행 메세지를 출력
        
    def msg_display(self):
    		#턴이 진행중이고 이긴사람이 없다면 참
        if (self.__turns !=0 and self.__winner ==0):
        		#몇수째인지 출력과 누구차례인지 출력
            print("Turn " , self.__turns, ", ", end="")
            if (self.__next == -1):
                print("Black")
            elif (self.__next == 1):
                print("White")
        if (self.__draw ==1): #비겼을 경우 출력
            print()
            print("== No Winner : Game Result is draw ")
        elif (self.__winner !=0 ) : #이겼을 경우 출력
            print()
            print("Congraturation!")
            print("The winner is ", end="") 
            if (self.__winner == -1):
                print("Black!!")
            elif (self.__winner == 1):
                print("White!!")
            
        
    def endCheck(self):
        # 수평을 체크한다.
        for i  in range(0, self.__size): #0~14
            for j  in range(0, self.__size-4):
            	  #돌이 있다면은 참
                if (self.__bd.get(i,j)!=0):
                		#돌이 있는 위치로부터 오른쪽으로 5칸을 확인해 다 더해준다.
                    check=self.__bd.get(i,j)+self.__bd.get(i,j+1)+self.__bd.get(i,j+2)+self.__bd.get(i,j+3)+self.__bd.get(i,j+4)
                    #-5이면 참이다.
                    if (check == (5 * self.__bd.get(i,j))):
                        return True
                    
        # 수직을 체크한다.
        # 수평과 방식 똑같다.
        for i  in range(0, self.__size):
            for j  in range(0, self.__size-4):
                if (self.__bd.get(j,i)!=0):
                    check=self.__bd.get(j,i)+self.__bd.get(j+1,i)+self.__bd.get(j+2,i)+self.__bd.get(j+3,i)+self.__bd.get(j+4,i)
                    if (check == (5 * self.__bd.get(j,i))):
                        return True            
        
         
        #  대각선 체크한다. 오른쪽 위로
        for i  in range(0, self.__size-4):
            for j  in range(0, self.__size-4):
                if (self.__bd.get(i,j)!=0):
                    check=self.__bd.get(i,j)+self.__bd.get(i+1,j+1)+self.__bd.get(i+2,j+2)+self.__bd.get(i+3,j+3)+self.__bd.get(i+4,j+4)
                    if (check == (5 * self.__bd.get(i,j))):
                        return True        
                
        #  대각선 체크한다. 왼쪽 아래로
        for i  in range(0, self.__size-4):
            for j  in range(4, self.__size):
                if (self.__bd.get(i,j)!=0):
                    check=self.__bd.get(i,j)+self.__bd.get(i+1,j-1)+self.__bd.get(i+2,j-2)+self.__bd.get(i+3,j-3)+self.__bd.get(i+4,j-4)
                    if (check == (5 * self.__bd.get(i,j))):
                        return True         
        # draw check : turns >= max 
        if (self.drawCheck()): #비겼다면 겜이 끝났으므로 참을 반환
            return True
        # no match (no Omok)
            
        return False 

    def drawCheck(self):
        if (self.__turns >= self.__size * self.__size - 2):
            self.__draw=1
            return True
        else :
            self.__draw=0
            return False
        

    #돌이 있다면 false반환한다.
    def validCheck(self, stn):
        # 3 by3 check =>  not implemented
        # overlapped check
        
        #보드 판의 현재 돌 객체의 좌표에 0이 아닌값이 들어가있으면(돌이 있다면) false반환
        if (self.__bd.get(stn.getX(), stn.getY()) !=0):
            return False
        return True
