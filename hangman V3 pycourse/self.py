#bricks=input(" Enter three digits (each digit for one pig): ")
#s=int(bricks[0])+int(bricks[1])+int(bricks[2])
#print(s)
#print(s//3)
#shrt=s%3
#print(shrt)
#if shrt!=0:
 #   print(False)
#else:
#    print(True)
#print("\"Shuffle, Shuffle, Shuffle\", say it together! \n Change colors and directions, \n Don't back down and stop the player! \n \t Do you want to play Taki? \n \t Press y\\n")
#pilandrom=input("enter a word: ")
#pilandrom=pilandrom.replace(" ","")
#x=pilandrom[::-1]
#if x == pilandrom:
 #   print("ok")
#else:
 #   print("not")
temp_to_conv=input("input a temprature you want to convert: ")
if "c" in temp_to_conv or "C" in temp_to_conv:
    tmp=float(temp_to_conv[0:len(temp_to_conv)-1])
    C_TO_F=(tmp*9)/5 +32
    print("the temprature is: ", C_TO_F, "Farhenheit")
else:
    tmp=float(temp_to_conv[0:len(temp_to_conv)-1])
    F_TO_C=(tmp-32)/1.8
    print("the temprature is: ", F_TO_C, "Celsius")