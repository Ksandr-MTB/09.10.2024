

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо !'
]
name = 'test.txt'
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings)):
        strings_positions = []
        ass = []
        q = []
        q.append(i+1)
        q.append(file.tell())
        ass.append(tuple(q))
        ass.append(strings[i])
        strings_positions.append(ass)
        print(dict(strings_positions))
        file.write(f"{strings[i]}\n")
    file.close()
    file = open(name, 'r', encoding='utf-8')
    # print(file.read())
    file.close()




result = custom_write(name, info)
