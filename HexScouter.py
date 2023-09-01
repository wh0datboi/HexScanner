import os
import sys
from os import path
from argparse import ArgumentParser
fileSignaturesDict = {"jpeg/jpg":["FF D8 FF DB","FF D8 FF EE", "FF D8 FF E1","FF D8 FF E0"], 
                  "pdf": "25 50 44 46",
                      "Microsoft Office (DOC, DOT, PPS, PPT, XLA, XLS, etc.)": "D0 CF 11 E0 A1 B1 1A E1", 
                  "mp4": "66 74 79 70 69 73 6F 6D", "DOS executable (exe, dll, etc.)": "4D 5A", 
                  "Zip based file format": ["50 4B 03 04", "50 4B 05 06", "50 4B 07 08"], 
                  "png": "89 50 4E 47" 
}

def signatureCheck(fileSignature):
    for key, val in fileSignaturesDict.items():
        if type(val) == list:
            if fileSignature in val:
                return key
        elif fileSignature == val:
            return key
    return False



def conversion(fileName):
    file = open(fileName, "rb").read(32) 

    fileHex = " ".join(['{:02X}'.format(byte) for byte in file])
    return fileHex[:11]

if __name__ == "__main__":
    fileName = sys.argv[1]
    #fileName = input("Name of the file: ")

    validPath = path.exists(fileName)
    validFile = path.isfile(fileName)
    
    if validPath and validFile:
        print()
        fileSignature = conversion(fileName)
        fileFormat = signatureCheck(fileSignature)
        if not fileFormat:
            print("File type unknown.")
        else: print("The format of the file is:", fileFormat)
    else:
        print("---- File cannot be found. ----")




