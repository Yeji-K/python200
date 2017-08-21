names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly':7855}

while True:
    try:
        k = input('input name: ')
        if k in names:
            print('이름이 <%s>인 출생아 수는 <%d>명 입니다.'%(k,names[k]))
        else:
            print('자료에 <%s>인 이름이 존재하지 않습니다.'%k)

    except KeyboardInterrupt:
        print("Exit")
