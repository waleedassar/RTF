import os,sys,time
from _winreg import *


input_file = ""
subKey = "SOFTWARE\\Classes\\CLSID\\"
subKeyWow64 = "SOFTWARE\\Wow6432Node\\Classes\\CLSID\\"
listMapX = ["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f"]



if len(sys.argv)==2:
    input_file = sys.argv[1]
else:
    print "shit"
    sys.exit(-1)


MainHive = ConnectRegistry(None,HKEY_LOCAL_MACHINE)


fIn = open(input_file,"rb")
fCon = fIn.read()
fIn.close()

Length = len(fCon)
if Length == 0:
    print "Zero Length"
    sys.exit(-1)

CLSID = "{"
for i in range(0,Length):
    if i+16 <= Length:
        XX =  ord(fCon[i+3])
        if XX < 0x10:
            CLSID += listMapX[XX]
        else:
            XXX = str(hex(XX))
            CLSID += XXX[2:4]
        YY =  ord(fCon[i+2])
        if YY < 0x10:
            CLSID += listMapX[YY]
        else:
            YYY = str(hex(YY))
            CLSID += YYY[2:4]
        ZZ =  ord(fCon[i+1])
        if ZZ < 0x10:
            CLSID += listMapX[ZZ]
        else:
            ZZZ = str(hex(ZZ))
            CLSID += ZZZ[2:4]
        AA =  ord(fCon[i])
        if AA < 0x10:
            CLSID += listMapX[AA]
        else:
            AAA = str(hex(AA))
            CLSID += AAA[2:4]
        CLSID += "-"
        BB =  ord(fCon[i+5])
        if BB < 0x10:
            CLSID += listMapX[BB]
        else:
            BBB = str(hex(BB))
            CLSID += BBB[2:4]
        CC =  ord(fCon[i+4])
        if CC < 0x10:
            CLSID += listMapX[CC]
        else:
            CCC = str(hex(CC))
            CLSID += CCC[2:4]
        CLSID += "-"
        DD =  ord(fCon[i+7])
        if DD < 0x10:
            CLSID += listMapX[DD]
        else:
            DDD = str(hex(DD))
            CLSID += DDD[2:4]
        EE =  ord(fCon[i+6])
        if EE < 0x10:
            CLSID += listMapX[EE]
        else:
            EEE = str(hex(EE))
            CLSID += EEE[2:4]
        CLSID += "-"
        FF =  ord(fCon[i+8])
        if FF < 0x10:
            CLSID += listMapX[FF]
        else:
            FFF = str(hex(FF))
            CLSID += FFF[2:4]
        GG =  ord(fCon[i+9])
        if GG < 0x10:
            CLSID += listMapX[GG]
        else:
            GGG = str(hex(GG))
            CLSID += GGG[2:4]
        CLSID += "-"
        HH = fCon[i+10:i+16]
        for ii in range(0,6):
            JJ = ord(HH[ii])
            if JJ < 0x10:
                CLSID += listMapX[JJ]
            else:
                JJJ = str(hex(JJ))
                CLSID+= JJJ[2:4]
        CLSID += "}"
        #print CLSID
        try:
            KeyX = OpenKey(MainHive,subKey + CLSID)
            print "CLSID Found: " + CLSID
            CloseKey(KeyX)
        except WindowsError:
            Err = "Windows Error"

        try:
            KeyWow64X = OpenKey(MainHive,subKeyWow64 + CLSID)
            print "CLSID (Wow64) found: " + CLSID
            CloseKey(KeyWow64X)
        except WindowsError:
            ErrWow64 = "Windows Error"
                
        CLSID = "{"
