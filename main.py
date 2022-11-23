from random import randint

def generate_number():
    numbers = []#비어있는 list 생성
    while len(numbers) < 3:
        num = randint(0,9)
        if num not in numbers: #중복체크
            numbers.append(num) #list에 숫자 덧붙이기
    print("숫자 세팅 완료.")
    return numbers


def take_number():
    numbers = [] #비어있는 list 생성
    print("숫자 3개를 입력해주세요")
    while len(numbers) < 3 :
        #{0}, {1} .. 순으로 인자 값이 문자열 안으로 대입됨.
        num = int(input("{}번째 숫자 입력 : ".format(len(numbers)+1)))
        if num < 0 and num > 9:
            print("범위에서 벗어났습니다.")
        elif num in numbers:
            print("중복된 숫자가 존재합니다.")
        else:
            numbers.append(num)
        
    print("입력받은 숫자 :", numbers)
    return numbers

def get_result(answer_numbers, guess_numbers):
    S = 0;
    B = 0;

    #이중 for문으로 두 list 전체 순회
    for i in range(0,3):
        for j in range(0,3):
            #자리도 같으면 strike
            if(guess_numbers[i] == answer_numbers[j] and i == j):
                S += 1
            #아니면 ball
            elif(guess_numbers[i] == answer_numbers[j]) :
                B += 1
    return S, B


print("숫자야구 게임에 오신걸 환영합니다")
print("계속하기를 원하시면 go를 입력해주세요.")
print("종료를 원하시면 quit을 입력해주세요.")
count = 0
answer_numbers = generate_number()

#테스트용
print("answer_numbers : ",answer_numbers)
while True :
    command = input("command :")
    if command == "go" :
        guess_numbers = take_number()
        #S와 B에 각각 반환값으로 초기화
        S, B = get_result(answer_numbers, guess_numbers)
        print(S,"S ",B,"B")
        count += 1
        if S == 3:
            print("축하합니다. ", count, "번만에 통과했습니다.")
            break
    elif command == "quit" :
        break

