# File I/O Basics
# Two type of memory Volatile(RAM) and Nonvolatile(HardDisk)
# Mode
# "r" - Open file for reading - Default
# "w" - Open file for writing
# "x" - Create file if not exists
# "a" - Add more content to a file
# "t" - Text mode - Default
# "b" - Binary mode
# "+" - Read and Write


# read() - All content in that file
# f = open("Notes.txt")
# content = f.read() # OR f.read(30) - display starting 30 character in that file
# print(content)
# f.close()

# readable() - True/False
# f = open("Notes.txt")
# content = f.readable()
# print(content)
# f.close()

# readline() - print first line in that file
# f = open("Notes.txt")
# content = f.readline()
# print(content)
# f.close()

# Create new file - write
# f = open("Notes1.txt", 'w')  # 'w' - write mode for create file if not exists OR replace content with new content
# f.write('Hello')
# f.close()

# Add content in a file
# f = open("Notes1.txt", 'a')  # 'a' - append content in file
# content = f.write('\nSir')
# print(content)  # Return number of character in that file
# f.close()

# Handle read and write both
# f = open('Notes1.txt','r+')  # 'r+' for read and write mode
# print(f.read())  # read the content in a file
# c = f.write('\nThank you')  # add content in a file
# f.close()

# tell() and seek()
f = open('Notes.txt')
print(f.tell())  # print the starting index value
f.seek(3)  # print where we can start printing character on that line
print(f.readline())
f.close()

# Using with block to open file
# By using syntax we could not define close file syntax
with open('Notes1.txt') as f:
    a = f.read()
    print(a)
f = open('Notes1.txt')
f.read()
