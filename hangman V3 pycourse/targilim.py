def my_mp4_playlist(file_path, new_song):
    opfil=open(file_path,"r")
    readfl=opfil.readlines()
    print(readfl)
    newlst=[]
    for line in readfl:
        newlst.append(line.split(";"))
    opfil.close()
    print("newlist",newlst)
    newlst[2][0]=new_song
    stri=""
    for line in range(len(newlst)):
            stri=stri+";".join(newlst[line])
    print("stri\n",stri)
    newfl=open(file_path,"w")
    newfl.write(stri)
    newfl.close()









my_mp4_playlist("txttoreceive", "Python Love Story")
kria=open("txttoreceive", "r")
print("ans\n",kria.read())