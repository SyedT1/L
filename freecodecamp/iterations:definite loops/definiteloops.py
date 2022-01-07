sum = 0
for i in [1,2,3,"hello"]:
    sum += (i if isinstance(i,int) else 0)
print(sum)