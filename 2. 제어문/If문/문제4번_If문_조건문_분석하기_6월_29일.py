a = "Life is too short, you need python"

if 'wife' in a:     # a에 wife라는 단어가 있으면 wife를 출력 
    print('wife')     # 근데 a에 wife없음
elif 'python' in a and 'you' not in a:   # a에 python이 있고, you단어가 없다면 python 출력
    print('python')     # a에 you가 있기 때문에 실행안함
elif 'shirt' not in a:   # shirt라는 단어가 없을 때 shirt출력
    print('shirt')     # shirt라는 단어가 없으니 출력
elif 'need' in a:     # need라는 단어가 a에 있으면 출력
    print('need')    # need라는 단어가 있으니 출력해야 하지만 앞에서 shirt가 먼저 작업을 수행하고 If문을 탈출함 == 출력안함.
else:
    print('none')
