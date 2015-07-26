import os,sys,time,struct

def IsNum(X):
    if X!='0' and X!='1' and X!='2' and X!='3' and X!='4' and X!='5' and X!='6' and X!='7' and X!='8' and X!='9':
        return False
    return True


def DecodeUnicodesRTF(inputX):
    Length = os.path.getsize(inputX)
    if Length == 0:
        print "File of zero length\r\n"
        return -1
    fIn = open(inF,"r")
    fOut = open("Unicodes.bin","wb")
    fCon = fIn.read()
    for i in range(0,Length):
        if i + 3 <= Length:
            if fCon[i:i+3] == "\\u-":
                NumX = ""
                iX = i + 3
                for c in range(iX,Length):
                    if IsNum(fCon[c]):
                        NumX += fCon[c]
                    else:
                        break
                if NumX != "":
                    #print NumX
                    Num = int(NumX)
                    if Num > 65535:
                        Num_ = struct.pack("I",Num)
                    else:
                        Num_ = struct.pack("H",Num)
                    #print Num_
                    fOut.write(Num_)
    return 0

if len(sys.argv) != 2:
    print "Usage: DecodeRTFUnicodes.py input.rtf\r\n"
    sys.exit(-1)
else:
    inF = sys.argv[1]
    if os.path.exists(inF) == False:
        print "File does not exist\r\n"
        sys.exit(-1)
    ret = DecodeUnicodesRTF(inF)
    sys.exit(ret)
