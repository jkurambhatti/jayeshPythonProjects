'''
    here we will study how to
        create a new file
        write to a file
        read from a file
'''

# write into a file

fw = open('sample.txt', 'w')        # name = sample.txt mode = write
fw.write("hey new file i am writing into you\n")
fw.write('''
        you are a multiline
        string which is
        written using 3 quotes
''')
print fw.name
print fw.mode
print fw.closed
print fw.tell()
fw.seek( 13 , 0)   # point to start 13th charc   0 = start , 1 = end
fw.seek( 13 , 1)   # point to last + 13th charc
fw.seek( -13 , 1)   # point to last 13th charc
print fw.tell()
fw.close()

# read from a file

fr = open('sample.txt', 'r')
buffer = fr.read(15)
print buffer
buffer = fr.read()      # read whole file from the current position indicator to end
print buffer
