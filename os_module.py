import os
import time

# print('Текущая дериктория:', os.getcwd())
# # os.mkdir('module 7')
# print('Текущая дериктория:', os.getcwd())
# print(os.path.exists('module 7'))
# print(os.listdir())
# directory = “.”
directory = (r'C:\Users\user\PyCharm (raboty)\Новая папка')
# print(directory)
# print(os.path.join(directory))
# print(os.path.getmtime(directory))
# print(os.path.getsize(directory))
# print(os.path.dirname(directory))
# i =0
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(directory)
    filetime = os.path.getmtime(directory)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(directory)
    parent_dir = os.path.dirname(directory)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
    # i = i+1
    # print(i)

# Вот что вывела консоль:
#
# Обнаружен файл: chernovik.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: fake_math.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: main.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_4_1.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_4_2.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_5_1__.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_5_3.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_5_hard.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_6_1.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_6_2.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_6_3.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_6_hard.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_7_1.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_7_2.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: module_7_3.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: os_module.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: practika_5_1.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: products.txt.txt, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: products2.txt, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: proverka.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: sample2.txt, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: test.txt, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: test_file.txt, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: true_math.py, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
# Обнаружен файл: й.txt, Путь: C:\Users\user\PyCharm (raboty)\Новая папка, Размер: 8192 байт, Время изменения: 30.10.2024 22:23, Родительская директория: C:\Users\user\PyCharm (raboty)
#
# Process finished with exit code 0
