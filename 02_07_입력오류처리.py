# 입력오류처리
# try ~ exception 문

try:
    n = int(input("정수입력:"))
    print(n)
except ValueError as Exception:
    print("정수를 입력해 주세요.")
    pass
