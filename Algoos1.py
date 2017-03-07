# Anagram problem
str1 = "Doog"
str2 = "God"
str1 = str1.lower()
str1 = sorted(str1)
#str1 = str(str1)

str2 = str2.lower()
str2 = sorted(str2)
#str2 = str(str2)
print(str2)

if str1 == str2:
    print(True)

