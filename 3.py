input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
data=data.split()
a=int(data[0])
b=int(data[1])
c=a+b-1
output_data = open('output.txt','w')# Открываем для записи файл
output_data.write(str(c-a)+' '+str(c-b))
input_data.close()
output_data.close()
                  