#!/usr/bin/python

import os
import sys
import re
import shutil
from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        frame.master.title("My Test")

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.text_button = Button(frame, text="Print", command=self.print_text)
        self.text_button.pack(side=RIGHT)
        
        self.text_entry = Entry(frame)
        self.text_entry.pack(side=RIGHT)        

    def say_hi(self):
        print "hi there, everyone!"

    def print_text(self):
        entstr = self.text_entry.get()
        print entstr

root = Tk()

app = App(root)
root.mainloop()


# args = sys.argv
# # Check arguments
# if len(args) == 1 or args[1] is ('-h' or '--help'):
#     print """\
#     usage: testcp src dst [suffix]
#       Copys all files from location (if specified) in SRC and having a name
#       containing of the type specified in SRC to the location (if specified)
#       in DST with the SRC matching filename portion replaced by the name 
#       portion specified in DST. If SUFFIX is given, only files with that
#       suffix will be copied.

#      Example: testcp ../trainAll/train_mu5 ./test5_mu5 ss
#       Copys all .ss files in the trainAll directory with train_mu5
#       in their filename to the current directory with new names which
#       have the train_mu5 portion of the name replaced with test5_mu5
#     """
#     sys.exit()
# elif len(args) < 3:
#     print " ERROR! Need at least 2 args"
#     print " usage: testcp src dst [suffix]\n"
#     print args
#     sys.exit()
# elif len(args) > 4:
#     print " ERROR! At most 3 args"
#     print " usage: testcp src dst [suffix]\n"
#     print args
#     sys.exit()
# ## Process suffix
# if len(args)==4:
#     suf = '.*'+args[3]+'$'
# else: # If no suffix, leave blank to match all
#     suf =  ''
# ## Process SRC
# # Separate path info and Filename root
# [srcPath, srcTemp] = os.path.split(args[1])
# srcFiles = [] # Empty list to fill
# if not srcPath: # If no SRC dir given, assume current
#     srcPath = '.'
# for currFile in os.listdir(srcPath): # for each file in SRC dir
#     if re.search(srcTemp+suf,currFile): # Check for root match
#         srcFiles.append(currFile) # Keep list of matches
#         # Recreate original filename with path
#         src = os.path.join(srcPath,currFile)
#         # Create new filename with SRC root replaced with DST root
#         newFile = currFile.replace(srcTemp,args[2])
#         # If no DST dir given, assume current
#         if not os.path.dirname(args[2]):
#             dst =  os.path.join('.',newFile)
#         else:
#             dst =  newFile
#         # Copy Files
#         shutil.copy(src,dst)
#         # Print report of what was done
#         print 'shutil.copy(%s, %s)'% (src, dst)
        
