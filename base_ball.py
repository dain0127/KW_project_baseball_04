from random import randint
from tkinter import *

__name__ = '__base_ball__'

#코드 전체를 지배하는 변수는 전역 변수로 설정
global count
count = 0

global result_label

def generate_number():
    numbers = []#비어있는 list 생성
    while len(numbers) < 3:
        num = randint(0,9)
        if num not in numbers: #중복체크
            numbers.append(num) #list에 숫자 덧붙이기
    print("숫자 세팅 완료.")
    return numbers

def go_game(root,input_text,answer_numbers,label):
    try :
        #1) 숫자를 입력받는다.
        numbers = [] #비어있는 list 생성
        input_num = int(input_text.get())
        while len(numbers) < 3 :
            num = input_num % 10
            #{0}, {1} .. 순으로 인자 값이 문자열 안으로 대입됨.
            if num < 0 and num > 9:
                label['text'] = "범위에서 벗어났습니다."
                break
            elif num in numbers:
                label['text'] = "중복된 숫자가 존재합니다."
                break
            else:
                numbers.append(num)
                input_num //= 10

        #역순으로 다시 저장 
        numbers.reverse()
        global count
        count += 1

        #테스트 용    
        print("입력받은 숫자 :", numbers)
        
        #2) strike와 ball을 계산한다.
        S = 0;
        B = 0;

        #이중 for문으로 두 list 전체 순회
        for i in range(0,3):
            for j in range(0,3):
                #자리도 같으면 strike
                if(numbers[i] == answer_numbers[j] and i == j):
                    S += 1
                #아니면 ball
                elif(numbers[i] == answer_numbers[j]) :
                    B += 1

        #3)결과를 출력한다 
        #스트라이크와 볼의 결과를 gui에 띄워주는 label list
        global result_label

        #각 guess case 별로 하나씩 결과를 라인별로 출력
        #gird의 row와 column을 통해서 row를 count에 대해서 하나씩 늘려 계산
        result_label=Label(root, text="입력받은 숫자 : {2}, S : {0}, B : {1}".format(S, B, numbers), font = 200)
        result_label.grid(column=0, row=count+1)

        if S == 3:
            label.configure(text = "축하합니다! {0}번만에 통과했습니다.".format(count))
            
    except Exception as err:
        print("예외가 발생했습니다. go_game() : ({0})".format(err))


def play() :
    try:
        root=Tk()
        root.title("base_ball")
        root.geometry('320x500')
        
        #안내문 label 생성
        label = Label(root, text ='숫자를 입력하고 확인을 눌러주세요.', font = 200 )
        label.grid(column=0, row=0)


        #정답 생성
        count = 0
        answer_numbers = generate_number()

        #테스트용
        print("answer_numbers : ",answer_numbers)

        #숫자 입력 창 생성
        input_text = Entry(root, width=30)
        input_text.grid(column=0, row=1)

        #버튼 클릭시 입력받은 숫자를 가지고 결과 출력
        go_button = Button(root, text="확인", command = lambda : go_game(root,input_text,answer_numbers,label))
        go_button.grid(column=1, row=1)

        root.mainloop()
    except Exception as err:
        print("예외가 발생했습니다. play() : ({0})".format(err))
        

if __name__ == '__main__' :
    play()

