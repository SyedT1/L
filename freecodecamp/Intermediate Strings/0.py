s = 'hello'
print(s[0:len(s)], end='\n')  # printing 0 <= len < length of the string
# printing len/2 <= len < length of the string
print(s[len(s)//2:len(s)], end='\n')

vdl = '12345678'
print(vdl[:3])  # prints the first 3 characters
print(vdl[1:])  # prints indices greater than 1

# checking substring
for i in ['solute', 'absolute', 'blunder']:
    print('substring ' + i + ' exists' if i in 'absolute' else i+' doesn''t exist')
# comparing strings
for i in 'abcdef':
   print(i+' is ','smaller' if i<'f' else 'greater or equal',' than f')

# string library
print('abcde'.upper())
print('PQRS'.lower())

# all string libraries
print(dir('hallo'))