# Baekjoon_CLASS0_2744: 대소문자 바꾸기

a = input()
b = [(chr(ord(i)-32)) if ord(i) > 96 else (chr(ord(i)+32)) for i in a]      # 아스키코드표를 이용한다
print(''.join(b))
