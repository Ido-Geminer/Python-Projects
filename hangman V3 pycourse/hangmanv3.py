def valid_word(chosen_word):
    for char in range(len(chosen_word)):
        validation_status=chosen_word[char].isalpha()
        if validation_status==False and chosen_word[char]!=" ":
            print("INVALID TEXT TRY AGAIN")
            return False
    return True
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
   # print("index check " ,index)
    #print(wordlist)

    openfile.close()
    return chosen_secret_word
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
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if letter_guessed.isalpha()==True and letter_guessed not in old_letters_guessed and len(guessed_letter)==1 and letter_guessed in wordstochoose:
        old_letters_guessed+=letter_guessed
        #print(old_letters_guessed)
        return True
    elif letter_guessed in old_letters_guessed or len(letter_guessed)>1 or letter_guessed.isalpha()==False:
        print("X")
        print("INVALID CHARACTER TRY AGAIN")
        old_letters_guessed = sorted(old_letters_guessed)
        print("->".join(old_letters_guessed[::]))
        return True
    else:
        print("X")
        old_letters_guessed += letter_guessed
        old_letters_guessed=sorted(old_letters_guessed)
        print("->".join(old_letters_guessed[::]))
        return False
def show_hidden_word(secret_word, old_letters_guessed):
    for letter in range(len(secret_word)):
        if secret_word[letter] not in old_letters_guessed:
            secret_word = secret_word.replace(secret_word[letter], "_")
    return secret_word
def check_win(secret_word, old_letters_guessed):
    cnt=0
    for letter in range(len(secret_word)):
        if secret_word[letter] in old_letters_guessed:
            cnt+=1
    if cnt==len(secret_word):
        return True
    else:
        return False
HANGMAN_ASCII_ART="""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """
print(HANGMAN_ASCII_ART)
to_txt_of_scrt_wrds = str(input("enter words and bewtween spaces: "))
to_txt_of_scrt_wrds=to_txt_of_scrt_wrds.lower()
valid_input= valid_word(to_txt_of_scrt_wrds)
while valid_input==False:
    #print("INVALID CHARACTERS ENTERED")
    to_txt_of_scrt_wrds = str(input("enter words and bewtween spaces: "))
    to_txt_of_scrt_wrds = to_txt_of_scrt_wrds.lower()
    valid_input=valid_word(to_txt_of_scrt_wrds)
num_from_user=int(input("enter an integer number: "))
insert_words=open("hngmnwrds", "a")
insert_words.write(" "+to_txt_of_scrt_wrds)
insert_words.close()
num_from_user=num_from_user-1
wordstochoose=choose_word("hngmnwrds", num_from_user)
#print(wordstochoose)
old_letters_guessed=[]
tries=1
max_tries=6
#print("made it here")
while tries<=max_tries:
    guessed_letter = input("enter a letter: ")
    bank = try_update_letter_guessed(guessed_letter, old_letters_guessed)
    if bank==True:
        word_status = show_hidden_word(wordstochoose, old_letters_guessed)
        print(word_status)
    if bank==False:
        tries = tries + 1
        word_status = show_hidden_word(wordstochoose, old_letters_guessed)
        print(word_status)
        status_picture = print_hangman(tries)
        print(status_picture)
    win_check=check_win(wordstochoose,old_letters_guessed)
    if win_check==True:
        print("CONGRADULATIONS, YOU WON :)")
        break
    else:
        continue
if tries==max_tries:
    print("YOU LOST :(")
