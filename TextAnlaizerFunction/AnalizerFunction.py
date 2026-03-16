import re
import string
speCar = set(string.punctuation)


# Untuk melihat list dan jumlah kalimat
def SeeOfSentence(word):
    try:
        sentence = re.findall(r"\w+(?:\s\w+)*[.!?]",word)
        lenSentence = len(sentence)
        return lenSentence,sentence
    
    except TypeError:
        return "Masukkan Kalimat yang Benar"



# Untuk melihat jumlah karakter di dalam string
def SeelenOfChar(word):
    try:
        # len string with whitespace:
        lenWithSpace = len(word)
        # len string without whitespace
        lenWithOutSpace = len(word.replace(" ",""))

        return lenWithSpace,lenWithOutSpace

    except TypeError:
        return "Masukkan Kalimat yang Benar "
    

# Untuk melihat Jumlah Kata 
def seeCountOfWord(word):
    try:
        # Bersihkan String dari tanda baca
        cleanWord = "".join(w for w in word if w not in speCar)
        cleanWordSplit = cleanWord.split()
        return len(cleanWordSplit),cleanWordSplit
    
    except TypeError:
        return "Masukkan Kalimat yang Benar"



def seeUniquesCharacter(word):
    try:
        #Bersihkan Kalimat dari tanda baca
        cleanWord = "".join(w for w in word if w not in speCar)
        cleanWordSplit = cleanWord.split()

        # Menghilangkan karakter duplikat
        nonDuplicateWord = sorted(set(cleanWordSplit))

        # List Character yang ada
        listChar = dict()
        for i in nonDuplicateWord:
            listChar[i] = 0

        # Mengecek dan menghitung jumlah kata yang muncul
        for x in cleanWordSplit:
            if x in list(listChar):
                listChar[x] +=1

        # Menghasilkan Dictionary Kata unik diurut berdasarkan jumlah nya
        listUniqeCharOrder = sorted(listChar.items(),key = lambda item : item[1],reverse = True)
        return listUniqeCharOrder
    

    except TypeError:
        return "Masukkan Kalimat yang benar"