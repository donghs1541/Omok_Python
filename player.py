from stone import *

class player:
    def __init__(self, clr):
    		#컬러값을 저장
        self._color = clr   # proteced variable with single underscore
    
    #소멸자
    def __del__(self):
        pass
    
    #보드판 리스트와 길이를 매개변수로 받아서
    #돌 객체를 컬러기반으로 생성하고, 좌표를 각각 입력받는다.
    #지금은 보드 리스트를 쓰고 있지않다.
    def next(self, board, length):
        print (" **** Black player : My Turns **** ")
        #컬러값과 길이를 주어서 돌 객체 생성
        stn = stone(self._color, length)
        pos =int(input("Input position x for new stone : "))
        while ((pos < 0) or (pos >= length)):
            pos = input("Wrong position, please input again : ")
            
        stn.setX(pos) #돌 객체의 x좌표값을 셋팅해준다.
        pos =int(input("Input position y for new stone : "))
        while ((pos < 0) or (pos >= length)):
            pos = input("Wrong position, please input again : ")
            
        stn.setY(pos) #돌 객체의 y좌표값을 셋팅해준다.
        print (" === Black player was completed ==== ")
        return stn #돌 객체를 반환한다.