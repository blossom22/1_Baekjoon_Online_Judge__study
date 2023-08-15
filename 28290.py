# Baekjoon_BRONZE4_28290: 안밖? 밖안? 계단? 역계단?     

dic = {'fdsajkl;':'in-out','jkl;fdsa':'in-out','asdf;lkj':'out-in',';lkjasdf':'out-in','asdfjkl;':'stairs',';lkjfdsa':'reverse'}
s = input()
try: 
    print(dic[s])
except:
    print('molu')