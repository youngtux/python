# 구구단을 파일로 출력하기

import couma

f = open('C:\\Users\\young\\source\\couma\\python\\ggdan.txt','w',encoding='utf-8')

r_li = couma.ggdan()
f.write("구구단 파일출력!!!\n")		
f.writelines('\n'.join(r_li))

f.close()
