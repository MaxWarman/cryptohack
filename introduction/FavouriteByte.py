from crypty import *

cipherTextHex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipherTextBytes = hexToBytes(cipherTextHex)

for key in range(256):
	stringResult = bytesToString(xorBytes( cipherTextBytes, intToBytes(key) ))
	if "crypto{" in stringResult:
		print(stringResult)
		break

###
###	Flag: crypto{0x10_15_my_f4v0ur173_by7e}
###