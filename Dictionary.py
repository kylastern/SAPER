class Dictionary:
    "Słownik"

    records = []

    def __init__(self):
        dictionary = []
        try:
            dictionaryFile = open('dictionary.tsv', 'r')
            dictionary = dictionaryFile.readlines()
            dictionaryFile.close()
        except:
            print("Brak słownika w folderze programu!")
            exit(1)
        for i in range(len(dictionary)):
            dictionary[i] = dictionary[i].replace('\n', '').split('\t')
        Dictionary.records = dictionary

    def searchTypeAndMeaningForWord(self,word):
        "Zwraca tablicę znaczeń podanego słowa"
        meanings = []
        for i in Dictionary.records:
            if (i[0] == word):
                meanings.append([i[1],i[2]])
        if(len(meanings) == 0):
            meanings.append([word,'UNK'])
        return meanings
