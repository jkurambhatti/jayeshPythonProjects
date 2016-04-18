'''
    in this project 3 of Udacity we will changing the name of all the files in some directory
    using list comprehension
    we will need os module of python std library
'''

import os

def rename_files():
    # go to the destination directory
    cwd = (os.getcwd())
    print "current path is " + cwd
    os.chdir("/home/leena/PycharmProjects/Udacity/sample_dir/")
    destdir = os.getcwd()
    print (os.getcwd())
    # print all file names in cwd
    files_list =  os.listdir(destdir)
    print files_list
    # rename the files
    '''
    for i in files_list:
        i = str(i)
        os.rename(i,( i.translate(None,"0123456789")))
    '''
    names_list = [ (str(name)).translate(None,"0123456789")  for name in files_list  ]
    print names_list
    #os.listdir(os.getcwd())



rename_files()
s = "123asd"

