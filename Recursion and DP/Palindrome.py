def ifpalindrome(x):
     if len(x)>1:
         if len(x)==2:
             return x[0].lower()==x[1].lower();
         else:
             if x[0].lower()==x[len(x)-1].lower():
                 return (x[1:len(x)-1]);
             else:
                 return False;
     else:
         return True;
             
n = input('Enter: ')
print('it''s a palindrome' if ifpalindrome(n) else 'it''s not a palindrome')
