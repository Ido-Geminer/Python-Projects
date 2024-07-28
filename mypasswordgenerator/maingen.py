import random
#banks
Alphabet_Bank = "abcdefghijklmnopqrstuvwxyz"
Alphabet_len = len(Alphabet_Bank)
Number_Bank = "6183209475"
Number_len = len(Number_Bank)
Special_Bank = "~!@#$%^&*()_+><?/"
Special_len = len(Special_Bank)
def chargen(bank,length_of_bank): #generator for a character of any kind
    Rand_Number = random.randint(0,length_of_bank-1)
    Generated_Char = bank[Rand_Number]
   # print("__________", Generated_Char, "_______________")
    return Generated_Char
def repedetion(Password_list): #to see if a character is in more than 2 times in the password
    repedetion=-1 #will count itself
    for char in Password_list:
        repedetion = 0
        for checker in Password_list:
            if char == checker:
                repedetion+=1
            if repedetion==2:
                return False
    return True

def consecutive_checks(Password_list): #checks if two letters are cosecutive by converting to ASCII, and checking if in the same bank
    for char0 in range(0,len(Password_list)-1):
        for char1 in range(1,len(Password_list)-1):
            first=Password_list[char0]
            second=Password_list[char1]
            if str(first) in Alphabet_Bank and str(second) in Alphabet_Bank or str(first) in Number_Bank and str(second) in Number_Bank:
                if ord(str(first)) == ord(str(second)) - 1:
                    return False
    return True
def main():
    Validation_checks=False #for starting the loop - the first loop is automatically false
    while Validation_checks == False:
        #banks
        Alphabet_Bank = "abcdefghijklmnopqrstuvwxyz"
        Alphabet_len = len(Alphabet_Bank)
        Number_Bank = "6183209475"
        Number_len = len(Number_Bank)
        Special_Bank = "~!@#$%^&*()><?"
        Special_len = len(Special_Bank)

        Password_Buildup=[] #will list all of the characters that will form the password
        for i in range(0,7): #letter generation
            Ps_Letter = chargen(Alphabet_Bank, Alphabet_len)
            Password_Buildup.append(Ps_Letter)
        Capital_letter = random.randint(0,5)
        Password_Buildup[Capital_letter] = Password_Buildup[Capital_letter].upper() #capitalizing a random letter
       # print("+++ capitaling", Password_Buildup,"####")
       # print("$$$$$$$$$$$$$$$$$$ end of letter gen $$$$$$$$$$$$")
        for j in range(0,3): #number generation
            Ps_Number = chargen(Number_Bank, Number_len)
            Password_Buildup.append(Ps_Number)
       # print("$$$$$$$$$$$$$$$$$$ end of number gen $$$$$$$$$$$$")
        Password_Buildup.append(chargen(Special_Bank, Special_len)) #special punctuation generation
       # print("$$$$$$$$$$$$$$$$$$ end of special char gen $$$$$$$$$$$$")
        random.shuffle(Password_Buildup) #mixing the password
        Final_Order=[]
        for char in Password_Buildup: #Final Buildup after mixing
            Final_Order.append(char)
       # print("after shuffle___",Final_Order)
        Final_Password = ""
        for char in Final_Order: #character gathering, then outputting the final product
            Correct_char = str(char)
            Final_Password = Final_Password+Correct_char
        if repedetion(Final_Order)==True and consecutive_checks(Final_Order)==True:
            print("SUCCESS FINAL PASSWORD : " + Final_Password)
            Validation_checks=True #Loop Killing
            return Final_Password #sending password to GUI
        else:
            print("Generating please wait")
main()