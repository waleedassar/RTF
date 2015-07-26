import os, sys, time, hashlib




def IsNonHexChar(CharX):
    if CharX != "0" and CharX != "1" and CharX != "2" and CharX != "3" and CharX != "4" and CharX != "5" and CharX != "6" and CharX != "7" and CharX != "8" and CharX != "9" and CharX != "A" and CharX != "a" and CharX != "B" and CharX != "b" and CharX != "C" and CharX != "c" and CharX != "D" and CharX != "d" and CharX != "E" and CharX != "e" and CharX != "F" and CharX != "f":
        return True
    return False

def IsHexChar(CharX):
    if CharX != "0" and CharX != "1" and CharX != "2" and CharX != "3" and CharX != "4" and CharX != "5" and CharX != "6" and CharX != "7" and CharX != "8" and CharX != "9" and CharX != "A" and CharX != "a" and CharX != "B" and CharX != "b" and CharX != "C" and CharX != "c" and CharX != "D" and CharX != "d" and CharX != "E" and CharX != "e" and CharX != "F" and CharX != "f":
        return True
    return False

def IsWhiteSpace(inC):
    if inC == " " or inC == "\t" or inC == "\r" or inC == "\n":
        return True
    return False

def Hexify(contentX):
    if len(contentX)==0:
        print "Input content is empty\r\n"
        return ""
    else:
        Second = False
        SkipNext = False
        FinalStr = ""
        NewStr = ""
        for X in contentX:
            if SkipNext == True:
                SkipNext = False
                continue
            if IsHexChar(X)==True:
                SkipNext = True
                continue
            if Second == False:
                NewStr+=X
                Second = True
            else:
                NewStr+=X
                FinalStr += "\\x"
                FinalStr += NewStr
                NewStr = ""
                Second = False
        
        #print FinalStr + "\r\n"
        XXX = "\"" + FinalStr + "\""
        outputX =  eval(XXX)
        return outputX

        
def DumpRTFObjects(input_file):
    Min_Length = 20
    fIn = open(input_file,"r")
    fCon = fIn.read()
    fIn.close()
    Length = len(fCon)
    if Length == 0:
        print "Zero Length"
        return -1

    filecounter = 0
    Obj = ""
    for i in range(0,Length):
        if IsNonHexChar(fCon[i])==True and fCon[i]!="\r" and fCon[i]!="\n":
            if len(Obj)>Min_Length:
                print "---Starts Here---\r\n"
                print Obj
                print "---Ends Here---\r\n"
                outfile = str(filecounter)+".dmp"
                fOut = open(outfile,"w")
                fOut.write(Obj)
                fOut.close
                outfileX = str(filecounter)+".obj"
                fOutX = open(outfileX,"w")
                fOutX.write(Hexify(Obj))
                fOutX.close()
                filecounter = filecounter + 1
            Obj = ""
            continue
        else:
            if fCon[i]!="\r" and fCon[i]!="\n":
                Obj += fCon[i]

def main():
    if len(sys.argv)!=2:
        print "Usage: DumpRTFObjects.py input_rtf_here\r\n"
        sys.exit(-1)
    else:
        retX = DumpRTFObjects(sys.argv[1])
        sys.exit(retX)


if __name__ == "__main__":
    main()
