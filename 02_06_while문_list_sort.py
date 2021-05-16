# 5개의 값을 입력받아서 크기순으로 출력
# while문, list사용법

d_list = []
cnt = 1

while cnt<6 :
    d = input(str(cnt)+"번째 값을 입력하세요.:")
    d_list.append(d)
    cnt = cnt + 1

d_list.sort()
print(d_list)
