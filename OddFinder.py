# -*- coding:utf-8 -*-

import os
import shutil

def typeupperize(filename):
    filedec = filename.split(".")
    filenameup = ".".join(filedec[:-1]) + "." + filedec[-1].upper()
    return filenameup

def isodd(filename, filenamelist):
    odd_file_types = ["NEF", "CRW", "ARW", "ORF", "RAF", "RAW", "RW2", "TIFF"]
    cos_file_type = "JPG"
    filenameuplist = [typeupperize(fn) for fn in filenamelist]
    if (typeupperize(filename).split(".")[-1] in odd_file_types) and ((".".join(filename.split(".")[:-1]) + "." + cos_file_type) not in filenameuplist):
        return True
    else:
        return False

odd_dir = "odd"
while True:
    pro_dir = input("Please input the directory that you would like to process.\nInvalid input will be ignored and the current directory will be processed.\nPath: ")
    try:
        os.chdir(pro_dir)
    except:
        pass
    pro_dir = os.getcwd()
    print("Directory {} will be processed.\n".format(pro_dir))
    try:
        try:
            os.mkdir(odd_dir)
        except FileExistsError:
            pass
    except:
        print("Making directory error!\n")
        exit()
    files = []
    for item in os.listdir(pro_dir):
        if os.path.isfile(item) and "." in item:
            files.append(item)
        else:
            pass
    i = 0
    for file in files:
        if isodd(file, files):
            try:
                print("Moving file {} ...".format(file))
                shutil.move(file, odd_dir)
            except:
                print("Moving file {} error!\n".format(file))
                i += 1
        else:
            pass
    if i == 0:
        print("Successful!\n")
    else:
        print(str(i) + " files have not been moved.\n")
