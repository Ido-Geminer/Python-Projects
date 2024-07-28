def usrfilereq(file,op):
    to_op_on=open(file,"r")
    to_op_txt=to_op_on.read()
    if op=="sort":
        wrdlst=to_op_txt.split(" ")
        wrdlst1=[]
        for word in range(len(wrdlst)):
            if wrdlst[word] not in wrdlst1:
                wrdlst1.append(wrdlst[word])
        wrdlst1.sort()
        return wrdlst1
    elif op=="rev":
        fnl=""
        x=to_op_txt.split("\n")
        for sent in range(len(x)):
            rev=x[sent][::-1]
            fnl=fnl+rev+"\n"
        return fnl
    elif op=="last":
        fnl=""
        x=to_op_txt.split("\n")
        num=int(input("enter a number: "))
        for sent in range(num):
            fnl=fnl+x[-sent]+"\n"
        return fnl

usrflie=input("enter a path file: ")
usrop=input("enter an operation: ")
ans=usrfilereq(usrflie,usrop)
print(ans)