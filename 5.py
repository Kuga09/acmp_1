input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
s=int(data)
x=int(s/6)
output_data = open('output.txt','w')# Открываем для записи файл
output_data.write(str(x)+' '+str(x*4)+' '+str(x))