def my_mp3_playlist(file_path):
    mscfl=open(file_path,"r") #opening the file and reading mode only
    mscopened=mscfl.read() #open content to read from
    #print(mscopened)
    mydict={"songs":[],"artists":[],"lengths":[]}
    individuals=mscopened.split("\n")
    print("individuals",individuals)
    mufradim=[]
    fnl=[]
    for element in individuals:
        mufradim.append(element.split(";",3))
        song=element.split(";",3)[0]
        artist=element.split(";",3)[1]
        lengths=element.split(";",3)[2]
        mydict["songs"].append(song)
        mydict["artists"].append(artist)
        mydict["lengths"].append(lengths)
    print(mydict)
    max=0
    cntr=-1
    for value in mydict["lengths"]:
        songtime=str(value)
        songtime=songtime.replace(":","")
        songtime=int(songtime)
        if songtime>max:
           max=songtime
           cntr+=1
    fnl.append(mydict["songs"][cntr])
    num_of_songs=len(mydict["songs"])
    fnl.append(num_of_songs)
    lst=[]
    maxin=1
    famous=""
    for value in mydict["artists"]:
        lst.append(value)
    for preformer in range(len(lst)):
        x=lst.count(lst[preformer])
        if x>maxin:
            x=maxin
            famous=lst[preformer]
    fnl.append(famous)

    return fnl

ans=my_mp3_playlist("txttomove")
print(ans)