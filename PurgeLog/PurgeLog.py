#!/bin/python3


# This script by Dmitriy Morozov
#
#   _________________________________
#   Version 1
#
#   2020
#
#   _________________________________


import shutil  # FOR CopyFile
import os  # FOR CHECK IF FILE EXIST and GETFILESIZE
import sys  # FOR CLI

# filename    size number of file
# python PurgeLor.py logfilename.log 10 5


if len(sys.argv) != 4:
    print("You need run this script with 3 parameters.")
    print("Example: PurgeLog.py logfile.txt 10 5")
    print("logfile.txt <- this name of file with logs,")
    print("10 <- this maxsize of logfile, and 5 <- is number of files, which will make when copping is will finished.")
    sys.exit(1)
else:
    print("Script is starting...")

filename = sys.argv[1]
filesize = int(sys.argv[2])
num_of_files = int(sys.argv[3])

print(filename, filesize, num_of_files)

if os.path.isfile(filename) == False:  # check if file exist
    print("Error. File is not exists.")
    sys.exit(1)
elif os.path.getsize(filename) / 1024 < 10:  # check if current size of file has normally value (<10 kbytes)
    print("Size of file is normally. Dont need change it.")
    sys.exit(1)
else:

    if num_of_files == 0:
        file1 = open(filename, 'w')
        file1.close()
    else:
        for current_num_of_file in range(num_of_files, 1, -1):
            scr = filename + "_" + str(current_num_of_file - 1)
            dst = filename + "_" + str(current_num_of_file)

            if os.path.isfile(scr) == True:
                print(scr)
                print(dst)
                shutil.copy(scr, dst)
    shutil.copy(filename, filename + "_1")
    file1 = open(filename, 'w')
    file1.close()

print("Script is finished succesfully.")
