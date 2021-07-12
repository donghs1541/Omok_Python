from board import *


class stone:
    def __init__(self): #매개변수 없는 생성자 15크기와 7,7 좌표를 준다.
        self.__size=19  # private
        self.__x = 9 
        self.__y = 9
        self.__bw=0
    
    #매개변수 있는 생성자 크기와 좌표를 넣어서 돌 객체를 만든다.
    def __init__(self, stn, sz=19):
        self.__size=sz #사이즈 저장
        self.__x = (self.__size-1)//2 #사이즈의 중간좌표를 찾아 저장한다.
        self.__y = (self.__size-1)//2
        self.__bw=stn #컬러값을 저장한다.
        
    def __del__(self):  # 소멸자
        #print(" stone 객체가 소멸합니다.") 
        pass

    def set(self, posX, posY, stn):
        self.__x = posX % self.__size #나머지연산자를 통해서 처음 설정한 좌표값이 저장된다.
        self.__y = posX % self.__size
        self.__bw= stn #컬러값을 저장한다.
        
    def setStone(self, stn):
        self.__bw = stn #컬러값을 저장한다.
    
    #나머지연산자를 통해서 처음 설정한 좌표값이 저장된다.
    def setX (self, posX):
        self.__x = posX % self.__size
        
    def setY (self, posY):
        self.__y = posY % self.__size
        
    def get(self):
        ret = stone() #매개변수없는 돌 객체 생성
        ret.set(self.__x, self.__y, self.__bw) #7,7,15 값을 셋팅한다.
        return ret #돌 객체를 반환한다.
    
    def getStone(self):
        return self.__bw #돌컬러를 반환한다.
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

