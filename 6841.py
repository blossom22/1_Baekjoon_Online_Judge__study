# Baekjoon_BRONZE4_6841: I Speak TXTMSG 

d = {"CU":"see you", ":-)":"I’m happy", ":-(":"I’m unhappy", ";-)":"wink", ":-P":"stick out my tongue", "(~.~)":"sleepy", "TA":"totally awesome", "CCC":"Canadian Computing Competition", "CUZ":"because", "TY":"thank-you", "YW":"you’re welcome", "TTYL":"talk to you later"}
while True:
    a = input()
    if a != 'TTYL' and (a in d):
        print(d[a])
    elif a == 'TTYL':
        print(d[a])
        break
    else:
        print(a)