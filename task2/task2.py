import wikipediaapi
from collections import Counter

class Firstletter():
    def __init__(self, language='ru', title='Категория:Животные_по_алфавиту'):
        self.__wiki_wiki = wikipediaapi.Wikipedia(language)
        # zoo_list = []
        self.__cat = self.__wiki_wiki.page(title)

    def sava(self):
        f = open('./text.txt', 'w')
        for p in self.__cat.categorymembers.values():
            if p.namespace == wikipediaapi.Namespace.CATEGORY:
                pass
            elif p.namespace == wikipediaapi.Namespace.MAIN:
                f.write(str(p.title) + '\n')

    def print_dict(self):
        f = open('./text.txt', 'r')
        first_letter = Counter(s[0] for s in f)

        list_keys = list(first_letter.keys())
        list_keys.sort()
        for i in list_keys:
            print(i, ':', first_letter[i])


a = Firstletter()
# a.sava()
a.print_dict()


