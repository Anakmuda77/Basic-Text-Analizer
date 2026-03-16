from TextAnlaizerFunction import AnalizerFunction

while True:
    try:
        Text = input("Masukkan Kalimat Yang akan dimasukkan : ")

        # Jumlah Kata dan List Kata (NON UNIK)
        countWord,listWord = AnalizerFunction.seeCountOfWord(Text)
        print("="*5,"TEXT ANALYZER","="*5)
        print("Total Kata   : ",countWord)
        print("List Kata    : ",listWord)

        # Jumlah Kalimat 
        countSentence,listSentence = AnalizerFunction.SeeOfSentence(Text)
        print("Total Kalimat    : ", countSentence)
        print("List Kalimat     : ", listSentence)


        # Jumlah Karakter
        countCharWithSpace, countCharWithoutSpace = AnalizerFunction.SeelenOfChar(Text)
        print("Jumlah Karakter  :")
        print("-"*10)
        print("-"*3,"> Dengan Spasi : ",countCharWithSpace)
        print("-"*3,"> Tanpa Spasi  : ",countCharWithoutSpace)

        # Jumlah Kata Unik
        UniqueWord = AnalizerFunction.seeUniquesCharacter(Text)
        print("Kata Unik    :",len(UniqueWord))
        print("-"*10)
        for word, count in UniqueWord:
            print(f"{word:<10} : {count}")

        inputUser = input(str("Apakah Masih Ingin Melanjutkan YES/NO : "))
        if(inputUser.lower() == "yes"):
            continue

        else:
            break


    except:
        print("Masukkan Kalimat dengan baik dan benar")
        continue


 


    