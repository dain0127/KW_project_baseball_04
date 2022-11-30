from tkinter import *
import base_ball as bb

__name__ = '__main__'

class MyFrame(Frame):
    def __init__(self, master):        
        img = PhotoImage(file='base_ball.gif')
        lbl = Label(image=img)
        lbl.image = img  # 레퍼런스 추가
        lbl.pack()


def main():
    root=Tk()
    root.title("base_ball_main")

    #윈도우 창의 너비와 높이
    #root.geometry("500x500+550+100")
    root.resizable(True, True) #윈도우 창 크기 조절 여부(상하, 좌우)

    #레이블 생성
    label = Label(root, text ='숫자 야구에 오신걸 환영합니다!', font = 200 )
    label.pack() #lebel을 화면에 배치

    # 야구 이미지 출력
    myframe = MyFrame(root)

    # 플레이 버튼
    play_button = Button(root,text='시작',bg='green',font=15,width=30,height=5,command=bb.play)
    play_button.pack(padx=10, pady=10)
    

    

    #메인 화면 표시
    root.mainloop()


if __name__ == '__main__' : 
    main()
