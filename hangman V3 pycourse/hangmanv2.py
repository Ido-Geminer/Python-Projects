HANGMAN_ASCII_ART="""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """
MAX_TRIES=6
print(HANGMAN_ASCII_ART ,"\n", "your maximum tries are:", MAX_TRIES)
secret_word=input("enter a word to guess:")
status=len(secret_word)*" _ "
print(status)
guess_char=input("guess a letter: ")
guess_char=guess_char.lower()
old_letters_guessed=['d', 'g', 'e', 'i', 's', 'k', 'y']
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if letter_guessed.isalpha()==True and letter_guessed not in old_letters_guessed:
        old_letters_guessed+=letter_guessed
        print(old_letters_guessed)
        return True
    else:
        print("X")
        old_letters_guessed=sorted(old_letters_guessed)
        print("->".join(old_letters_guessed[::]))
        return False
validcheck=try_update_letter_guessed(guess_char,old_letters_guessed)
print("validcheck",validcheck)
def show_hidden_word(secret_word, old_letters_guessed):
    for letter in range(len(secret_word)):
        if secret_word[letter] not in old_letters_guessed:
            secret_word = secret_word.replace(secret_word[letter], "_")
    return secret_word
wordcheck = show_hidden_word(secret_word, old_letters_guessed)
print(wordcheck)
def check_win(secret_word, old_letters_guessed):
    cnt=0
    for letter in range(len(secret_word)):
        if secret_word[letter] in old_letters_guessed:
            cnt+=1
    if cnt==len(secret_word):
        return True
    else:
        return False
wincheck=check_win(secret_word,old_letters_guessed)
print("wincheck",wincheck)

def print_hangman(num_of_tries):
    num_of_tries=str(num_of_tries)
    return HANGMAN_PHOTOS[num_of_tries]
HANGMAN_PHOTOS={
"1":"x-------x",
"2":"""x-------x
|
|
|
|
|
""",
"3":"""
x-------x
|       |
|       0
|
|
|""",
"4":"""
x-------x
|       |
|       0
|       |
|
|""",
"5":"""
x-------x
|       |
|       0
|      /|\\
|
|""",
"6":"""
x-------x
|       |
|       0
|      /|\\
|      /
|""",
"7":"""
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""
}
triesdone=7
piccheck=print_hangman(triesdone)
print(piccheck)
def choose_word(file_path,index):
    openfile=open(file_path,"r")
    readingfile=openfile.readlines()
    wordlist=[]
    without_doubles=[]
    for line in readingfile:
        wordlist.append(line.split(" "))
    for line in range(len(wordlist)):
        for word in range(len(wordlist[line])):
            if wordlist[line][word] not in without_doubles:
                without_doubles.append(wordlist[line][word])
    diffrent_words=len(without_doubles)
    if index>len(wordlist[line][word]):
        index=index%len(wordlist[line])
        chosen_secret_word = wordlist[0][index]
    else:
        chosen_secret_word=wordlist[0][index]
    print("index check " ,index)
    openfile.close()
    return diffrent_words,chosen_secret_word
indx_scrt_wrd=int(input("enter a number: "))
indx_scrt_wrd=indx_scrt_wrd-1
wordstochoose=choose_word("hngmnwrds", indx_scrt_wrd)
print(wordstochoose)
















