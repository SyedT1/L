primes = []
n = int(input('check upto = '))
for i in range(2,n+1):
    check = False
    for j in range(2,i):
        if i%j==0:
            check = True
            break
        
    if(check==False):
        primes.append(i)
nums_init = 1
for i in primes:
    print("Prime no {0} is = {1}".format(nums_init,i))
    nums_init = nums_init + 1    
