#!/usr/bin/python3
import linecache ,sys
intvar=[]#list to store variables
intval=[]#list to store variable values
strvar=[]
strval=[]
start=False
x = 1
File = sys.argv[1]
def tokeniser(file,line):
        text=linecache.getline(file,line)
        text=text.strip()
        token = text.split()
        return token

def compute(tokens):
        global start
        if tokens == []:
                pass#do nothing for blank line :)
        elif tokens[0] =="//":
                pass#do nothing for comments
        elif tokens[0] == "print" and start == True:
                for i in range(1,len(tokens)):
                        if tokens[i] in strvar:
                                indx = strvar.index(tokens[i])
                                print(strval[indx],end="")
                        elif tokens[i] in intvar:
                                indx = intvar.index(tokens[i])
                                print(intval[indx],end="")
                        else:
                                print(tokens[i],end=" ")
                print()
        elif tokens[0] == "end":
                exit()
        elif tokens[0] == "jump" and start == True:
                a=tokeniser(File,int(tokens[1]))
                compute(a)
        elif tokens[0] == "loop" and start == True:
                count = 1
                while count <= int(tokens[3]):
                        start_line=int(tokens[1])
                        line_num=int(tokens[2])-int(tokens[1])
                        end_line=int(tokens[1])+line_num
                        for i in range(start_line,end_line+1):
                                tok=tokeniser(File,i)
                                compute(tok)
                        count +=1
        elif tokens[0] == "add" and start == True:
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])+eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])+eval(tokens[2])
                        print(temp)
        elif tokens[0] == "diff" and start == True:
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])-eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])-eval(tokens[2])
                        print(temp)
        elif tokens[0] == "div" and start == True:
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])/eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])/eval(tokens[2])
                        print(temp)
        elif tokens[0] =="mul" and start == True:
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])*eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])*eval(tokens[2])
                        print(temp)
        elif tokens[0] == "var":
                if tokens[2].startswith("$"):
                        if tokens[1] == "int":
                                intvar.append(tokens[2])
                                if len(tokens)==4:
                                        intval.append(int(tokens[3]))
                                else:
                                        intval.append(0)
                        elif tokens[1] == "str":
                                strvar.append(tokens[2])
                                if len(tokens)>=3:
                                        strval.append('')
                                        indx=strvar.index(tokens[2])
                                        for i in range(3,len(tokens)):
                                                strval[indx]+=tokens[i]+' '
                                        string=strval[indx]
                                        strval[indx]=string.rstrip()
                                else:
                                        strval.append('')
                        else:
                                print("Error:Unkown data type please check your code :(")
                                exit()

                else:
                        print("Error:variable should start with '$' !!!!!")
                        exit()
        elif tokens[0] == "assign":
                if tokens[1] in intvar:
                        indx=intvar.index(tokens[1])
                        intval[indx]=eval(tokens[2])
                elif tokens[1] in strvar:
                        indx=strvar.index(tokens[1])
                        for i in range(2,len(tokens)):
                                strval[indx]+=tokens[i]
                                strval[indx]+=' '
                                string=strval[indx]
                        strval[indx] = string.rstrip(' ')
                else:
                        print("Error:Variable not found!!!!")
                        exit()
        elif tokens[0] == "inc":
                if tokens[1] in intvar:
                        indx=intvar.index(tokens[1])
                        intval[indx]+=eval(tokens[2])
                else:
                        print("ERROR:Variable not found")
                        exit()
        elif tokens[0] =="start":
                start =True
                #print(start)
while True:
        token = tokeniser(File,x)
        compute(token)
        x +=1
        #print(intvar,intval,sep="\n") #just for debugging int variable implementation :)
        #print(strvar,strval,sep="\n") #just for debugging str variable implementation :)
