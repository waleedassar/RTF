import os,sys,time,struct

def IsNum(X):
    if X!='0' and X!='1' and X!='2' and X!='3' and X!='4' and X!='5' and X!='6' and X!='7' and X!='8' and X!='9':
        return False
    return True

def IsNonHexChar(CharX):
    if CharX != "0" and CharX != "1" and CharX != "2" and CharX != "3" and CharX != "4" and CharX != "5" and CharX != "6" and CharX != "7" and CharX != "8" and CharX != "9" and CharX != "A" and CharX != "a" and CharX != "B" and CharX != "b" and CharX != "C" and CharX != "c" and CharX != "D" and CharX != "d" and CharX != "E" and CharX != "e" and CharX != "F" and CharX != "f":
        return True
    return False

def Hexify(Sequence):
    contentX = Sequence
    if len(contentX)==0:
        print "Can't hexify zero-length input\r\n"
        return 0
    else:
        Second = False
        FinalStr = ""
        NewStr = ""
        for X in contentX:
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
        retX = eval(XXX)
        return retX

                    
def ExtractRTFsid(inputX):
    Length = os.path.getsize(inputX)
    if Length == 0:
        print "File of zero length\r\n"
        return -1
    fIn = open(inF,"r")
    fOut = open("Unicodes.bin","wb")
    fCon = fIn.read()

    NumX = ""
    Still = True
    i = 0
    while i < Length:
        if Still == False:
            if NumX != "":
                ret = Hexify(NumX)
                if ret != 0:
                    fOut.write(ret)
                    fOut.write("--------")
                    fOut.flush()
                NumX = ""
        if i + 2 <= Length:
            if fCon[i:i+2] != "\\'":
                Still = False
            elif fCon[i:i+2] == "\\'":
                c = i + 2
                if c + 1 >= Length:
                    Still = False
                else:
                    if IsNonHexChar(fCon[c])==False and IsNonHexChar(fCon[c+1])==False:
                        NumX += fCon[c]
                        NumX += fCon[c+1]
                        c = c + 2
                        Trimmed = False
                        while fCon[c]=="\r" or fCon[c]=="\n":
                            Trimmed = True
                            c = c + 1
                        i = i + 3
                        if Trimmed == True:
                            i = c - 1
                        Still = True
                    else:
                        Still = False
        i = i + 1

    fOut.close()
    fIn.close()
    return 0

if len(sys.argv) != 2:
    print "Usage: ExtractRTFsid.py input.rtf\r\n"
    sys.exit(-1)
else:
    inF = sys.argv[1]
    if os.path.exists(inF) == False:
        print "File does not exist\r\n"
        sys.exit(-1)
    ret = ExtractRTFsid(inF)
    sys.exit(ret)
