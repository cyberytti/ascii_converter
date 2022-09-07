import os
import time
i = 1
r = "\033[1;31m"
b = "\033[1;34m"
def install():
    os.system('pip install ascii_magic')
    os.system('pip install tqdm')
    os.system('clear')
    os.system('python ascii.py')
try:
  import ascii_magic
  from tqdm import *
except Exception:
    print (b+str('[#]'),"",r+str('downloading requerments')+b+str('.....'))
    install()
print ("=====wellcome========")
path = input('''enter path
>>''')
col = eval(input('''enter columns(recomended=50)
>>'''))
cha = str(input('''enter character(recomended=0)
>>'''))
output = ascii_magic.from_image_file(path,columns =col,char=cha)
os.system('clear')
for i in tqdm(range(40)):
    time.sleep(0.1)
os.system('clear')
ascii_magic.to_terminal(output)
try:
    print ('Good bye')
    print ('Have a nice day...')
    time.sleep (1)
except Exception:
    time.sleep (i)
    print (' ')

