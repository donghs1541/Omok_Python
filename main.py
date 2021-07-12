from omokgame import *

def main():    
    game = omokgame(19) #대국시 쓸 코드
    game.game_start() #오목게임 객체 게임 시작
    return 0

if __name__ =="__main__": #이 파일을 직접 실행을 시키면 main이 실행된다. 아닐경우 실행되지 않는다.
    main()

#self.__bd.show() #왜있는지 모르겠다.