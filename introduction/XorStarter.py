from crypty import *

inputString = "label"
inputBytes = stringToBytes(inputString)

keyInt = 13
keyBytes = intToBytes(keyInt)

flag = bytesToString(xorBytes(inputBytes, keyBytes))

print(flag)

###
###	Flag: crypto{aloha}
###