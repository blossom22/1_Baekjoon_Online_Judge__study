# Baekjoon_BRONZE4_5358: Football Team 

table = {'i':'e', 'e':'i', 'I':'E', 'E':'I'}
table_key = ''.join(list(table.keys()))
table_value = ''.join(list(table.values()))
while True:
    try: 
        a = input()
        new_a = a.translate(str.maketrans(table_key,table_value))
        print(new_a)
    except:
        break