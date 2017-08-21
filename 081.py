msg = input('임의의 문장을 입력하세요:')
char = input('찾는 문자열을 입력하세요:')
if char in msg:
    print('당신이 입력한 문장에는 %s가 있습니다.'%char)
else:
    print('당신이 입력한 문장에는 %s가 없습니다.'%char)
