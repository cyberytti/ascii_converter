import os
import time
i = 1

try:
  import ascii_magic
except Exception :
  print ('downloading requerments.....')
  os.system('pip install ascii_magic')
  os.system('clear')
  time.sleep ("2")
  print ('please restart this tool')
  print ('enter this command >> python3 ascii.py')
print ("=====wellcome========")
path = input('''enter path
>>''')
col = eval(input('''enter columns(recomended=50)
>>'''))
cha = str(input('''enter character(recomended=0)
>>'''))
output = ascii_magic.from_image_file(path,columns =col,char=cha)
os.system('clear')
ascii_magic.to_terminal(output)
try:
    print ('Good bye')
    print ('Have a nice day...')
    time.sleep (i)
except Exception:
    time.sleep (i)
    print (' ')

