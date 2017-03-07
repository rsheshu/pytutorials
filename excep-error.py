
try:
    fpt = open("fileame",w)
    fpt.read(100)
except:
    print('Reading error')
else:
    print('Read this')
finally:
    print("some file operation is odonw")

try:
    lt = [1,3,45,5]
    for var in lt:
        print(lt **2)
except:
    print("Excepriont Raised!!!")