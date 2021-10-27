def find_smallest_int(x):
    mn = x[0]
    for i in x:
        mn = min(mn,i)
    return mn
