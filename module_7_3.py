class WordsFinder:
    file_names = []
    def __init__(self, *name_f):
        self.name_f = name_f
        for i in range(len(self.name_f)):
            self.file_names.append(self.name_f[i])

    def get_all_words(self):

        for i in range(len(self.file_names)):
            # all_words = {}
            list_tekst = []
            with open(self.file_names[i], encoding='utf-8') as file:
                for line in file:
                    tekst_fale = line.lower()
                    list_tekst = list_tekst + tekst_fale.split()
                all_words = {self.file_names[i]: list_tekst}
                for i in range(len(list_tekst)):
                    q = ''
                    for j in range(len(list_tekst[i])):
                        if list_tekst[i][j] not in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            q = q + list_tekst[i][j]
                    if q != '':
                        list_tekst[i] = q
                    else:
                        list_tekst.pop(i)
                print(all_words)
                # return all_words
            print()


    def find(self, word):

        for i in range(len(self.file_names)):
            q = self.file_names[i]
            d = 0
            all_words = {}
            list_tekst = []
            with open(self.file_names[i], encoding='utf-8') as file:
                for line in file:
                    tekst_fale = line.lower()
                    list_tekst = list_tekst + tekst_fale.split()
                for i in range(len(list_tekst)):
                    if word.lower() == list_tekst[i]:
                        d = i + 1
                        break
                    else:
                        pass
            all_words = {q: d}
            print(all_words)
        # return all_words


    def count(self, word):

        for i in range(len(self.file_names)):
            q = self.file_names[i]
            all_words = {}
            list_tekst = []
            with open(self.file_names[i], encoding='utf-8') as file:
                count = 0
                for line in file:
                    tekst_fale = line.lower()
                    list_tekst = list_tekst + tekst_fale.split()
                for i in range(len(list_tekst)):
                    if word.lower() == list_tekst[i]:
                        count += 1
                    else:
                        pass
            all_words = {q: count}
            print(all_words)
        # return all_words



finder2 = WordsFinder('products2.txt', 'sample2.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('texT'))