# fp = open("c:\\ubuntu-14.10-desktop-i386.iso")
count = 1
# for chunks in open("c:\\ubuntu-14.10-desktop-i386.iso", 'rb'):
#     count = count + 1
#     print(count)
#
# with open('myfile', mode='w', encoding='utf-8') as file:
#     count = 0
#     with open("c:\\ubuntu-14.10-desktop-i386.iso", 'rb') as fileptr:
#         for chunks in fileptr:
#             count = count + 1
#             print("rread counting {0}".format(count))


newfptr = open("D:\\ubuntu-14.10cpy-desktop-i386.iso", 'wb')
with open("C:\\ubuntu-14.10-desktop-i386.iso", 'rb') as fileptr:
    seekNew = 0
    while True:

       # newfptr.seek(seekNew)
        chunks = fileptr.read(1024000)
        newfptr.write(chunks)
       # oldSeek = seekNew
        #seekNew = newfptr.tell()
       # print(" Written bytes {xbytes}".format(xbytes=seekNew - oldSeek))

        if not chunks:
            break
