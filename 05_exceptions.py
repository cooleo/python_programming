while True:
  try:
    x = int(input('Please enter a number'))
    break
  except ValueError:
    print('Opps!, That was no valid number. Try again!')


while True:
  try:
    x = int(input('Please input a number'))
    break
  except (RunTimeError, TypeError, NameError):
    pass
   
class D(C):
    pass
for cls in [A, B, C, D]:
   try:
       raise cls()
   except D:
    print('D')
   except C:
    print('C')
   except B:
    print('B')
    
   
   
 import sys
 
 try:
   f = open('file_name.txt')
   s = f.readline()
   i = int(s.strip())
 except OSError as err:
   print('OS error {0}'.format(err))
 except:
   print('Unexpected error:', sys.exc_info()[0])
   raise
