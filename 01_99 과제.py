# 1회차 과제 : 19단_열맞추기
# for문, if문, 형변환 사용법 익히기

for item in range(2,20):
        for each in range(1,20):
            """ 숫자타입의 item을 문자열 str_item으로 형변환 한다
                10미만의 수는 앞에 공백을 붙여준다.
            """
            if item < 10 :
                str_item = ' ' + str(item)
            else :
                str_item = str(item)

            """ 숫자타입의 each를 문자열 str_each으로 형변환 한다
                10미만의 수는 앞에 공백을 붙여준다.
            """
            if each < 10 :
                str_each = ' ' + str(each)
            else :
                str_each = str(each)

            """ item*each의 결과값을 str_result로 형변환 한다.
                10미만의 결과값은 앞에 공백을 두자리 붙여준다.
                10이상 100미만의 결과값은 앞에 공백을 한자리 붙여준다.
            """
            if item * each < 10 :
                str_result = '  ' + str(item*each)
            else :
                if item * each < 100 :
                    str_result = ' ' + str(item*each)
                else :
                    str_result = str(item*each)

            print(str_item,' X ', str_each, ' = ', str_result)
