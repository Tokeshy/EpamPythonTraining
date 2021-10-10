### Task 1.4
#Write a Python program to sort a dictionary by key.
DefDict = {1: 2, 3: 4, 2: 9, 4:8} # as ex
SortedDict = {}
KeyList = []
for key, value in DefDict.items() :
    if key not in KeyList:
        KeyList.append(key)
for SortedKey in sorted(KeyList):
    SortedDict[SortedKey] = DefDict[SortedKey]
print(SortedDict) # as chk