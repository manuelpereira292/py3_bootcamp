import os

curDir = os.getcwd()
print(curDir)
os.mkdir('newDir')
os.rename('newDir', 'newDir2')
os.rmdir('newDir2')


os.chdir("D:\Dropbox\Share2CodingBootcampPython\Day 07\code_pack_22")
curDir = os.getcwd()
print(curDir)

os.chdir("D:/Dropbox/Share2CodingBootcampPython/Day 07/code_pack_21")
curDir = os.getcwd()
print(curDir)


os.chdir("../code_pack_22")
curDir = os.getcwd()
print(curDir)
