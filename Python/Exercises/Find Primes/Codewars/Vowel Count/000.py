def getCount(x):
    vw_count = 0
    for i in x:
        vw_count += (1 if i in 'aeiouAEIOU' else 0)
    return vw_count
print(getCount('main'))
