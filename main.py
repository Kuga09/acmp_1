input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла

output_data = open('output.txt','w')# Открываем для записи файл
output_data.write(c) # Записываем результат сложения output_data.write(str(int(data[0])+int(data[1])))

input_data.close()
output_data.close()