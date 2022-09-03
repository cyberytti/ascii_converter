import ascii_magic
import os
path = input('''enter path
>>''')
col = eval(input('''enter columns
>>'''))
cha = str(input('''enter character
>>'''))
output = ascii_magic.from_image_file(path,columns =col,char=cha)
os.system('clear')
ascii_magic.to_terminal(output)
