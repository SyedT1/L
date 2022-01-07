flag = True
for i in [1,2,33,4]:
    if i is int(3):
        print('found')
        flag = False
        break
if flag:
    print('not found')    