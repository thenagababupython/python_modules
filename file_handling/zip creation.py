from zipfile import *
f=ZipFile("files3.zip",'w',ZIP_DEFLATED)
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")
f.close()
print("the zip file created successfully!!!!")