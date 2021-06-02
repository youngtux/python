# 함수 정의하기

def ggdan():
    print(‘구구단 출력’)
    for item in range(2,10):
        for each in range(1,10):             
            print(str(item).rjust(2),' X ',str(each).rjust(2),' = ',str(item*each).rjust(3))

ggdan()
