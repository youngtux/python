# 함수 정의하기
# 정의한 함수를 동일 모듈내에서 호출

def ggdan():
    li = []
    for item in range(2,10):
        for each in range(1,10):             
            li.append(str(item).rjust(2)+' X '+str(each).rjust(2)+' = '+str(item*each).rjust(2))
    return li            


