import os,sys,time,struct,ctypes

#Split streams that were saved in the "OleSaveToStream" format


def SplitStreams(inFile):
    fIn = open(inFile,"rb")
    fCon = fIn.read()
    fIn.close()

    Length = len(fCon)
    print "File Length: " + str(Length)
    if Length == 0:
        print "Zero Length"
        return -1
    filecounter = 0
    i = 0
    while i < Length:
       if i+0xC <=Length:
          Field0 = fCon[i:i+4]
          Flags = (struct.unpack("i",Field0))[0]
          print "Flags: " + str(Flags)
          Field1 = fCon[i+4:i+8]
          Type = (struct.unpack("i",Field1))[0]
          print "Type: " + str(Type)
          Field2 = fCon[i+8:i+12]
          Size = (struct.unpack("i",Field2))[0]
          print "Size: " + str(Size)
          if Size == 0:
              i = i + 12
          else:
              Offset = i + 12
              Endset = Offset + Size
              print "Offset: " + str(Offset)
              print "Endset: " + str(Endset)
              DataX = fCon[i+12:i+12+Size]
              fOut = open(str(filecounter)+".obj","wb")
              fOut.write(DataX)
              fOut.close()
              filecounter = filecounter + 1
              i = i + 12 + Size
                

if len(sys.argv)!=2:
    print "Usage: SplitStreams.py input_file\r\n"
    sys.exit(-1)
else:
    retX = SplitStreams(sys.argv[1])
    sys.exit(retX)
