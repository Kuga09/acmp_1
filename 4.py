from decimal import Decimal as dec

input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.read() # Читаем в другую переменную содержимое всего файла
n=int(data)
E= dec("2.7182818284590452353602875")
E1=round(E,n)
output_data = open('output.txt','w')# Открываем для записи файл
output_data.write(str(E1)) 
input_data.close()
output_data.close()