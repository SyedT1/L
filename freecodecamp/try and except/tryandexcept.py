def inp():
    x = input()
    try:
        s = int(x)
        return s
    except:
        print('wrong input. Please take the correct form of input [0-9]*')
        return inp()


val = inp()
print('odd' if val % 2 else 'even')
