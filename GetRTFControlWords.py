import os,sys,time



def IsWhiteSpace(inC):
    if inC == " " or inC == "\t" or inC == "\r" or inC == "\n":
        return True
    return False



            
def GetRTFControlWords(input_file):
    fIn = open(input_file,"r")
    fCon = fIn.read()
    fIn.close()
    Length = len(fCon)
    if Length == 0:
        print "Zero Length"
        return -1

    for i in range(0,Length):
        if fCon[i]=="\\":
            if i +1 < Length:
                if fCon[i+1]=="*":
                    continue
            Start = i
            CC = 0
            for c in range(i+1,Length):
                if IsWhiteSpace(fCon[c])==True or fCon[c]=="{" or fCon[c]=="\\":
                    CC = c-1
                    break
            if CC != 0:
                CtrlWrd = fCon[Start:CC+1]
                print CtrlWrd

            
def main():
    if len(sys.argv)!=2:
        print "Usage: GetRTFControlWords.py input_rtf_here\r\n"
        sys.exit(-1)
    else:
        retX = GetRTFControlWords(sys.argv[1])
        sys.exit(retX)


if __name__ == "__main__":
    main()
