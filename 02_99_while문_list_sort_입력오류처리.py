# 5개의 수를 입력받아서 크기순으로 출력
# while문, list사용법, try exception

n_list = []
cnt = 1

while cnt<6 :
    try:
        n = int(input(str(cnt)+"번째 정수를 입력하세요.:"))
        n_list.append(n)
        cnt = cnt + 1
    except ValueError as Exception:
        print("정수를 입력해 주세요.")
        pass
        
n_list.sort()    

print(n_list)



